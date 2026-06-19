import React, { useState, useCallback, useRef, useEffect } from "react";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";
import Map from "./components/Map";
import Sidebar from "./components/Sidebar";
import ThematicMap from "./components/ThematicMap";
import Toolbar from "./components/Toolbar";
import thematicMapConfigs from "./config/thematicMapConfigs";
import "./styles/Sidebar.css";
import "./styles/ThematicMap.css";
import "./styles/Toolbar.css";

mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_ACCESS_TOKEN;

const App = () => {
  const [mapboxMap, setMapboxMap] = useState(null);
  const mapContainerRef = useRef(null);
  const drawRef = useRef(null);

  const [activeLayers, setActiveLayers] = useState({});
  const [drawnGeometry, setDrawnGeometry] = useState(null);
  const [highlightedFeatures, setHighlightedFeatures] = useState(null);
  const [spatialQueryResults, setSpatialQueryResults] = useState(null);
  const [isThematicMode, setIsThematicMode] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const handleLayerToggle = useCallback((layerId, isSelected) => {
    setActiveLayers(prev => ({ ...prev, [layerId]: isSelected }));
  }, []);

  const handleThematicModeToggle = useCallback(() => {
    setIsThematicMode(prevMode => !prevMode);
    setDrawnGeometry(null);
    setHighlightedFeatures(null);
    setSpatialQueryResults(null);
    setActiveLayers({});
  }, []);

  const toggleSidebar = useCallback(() => {
    setIsSidebarOpen(prev => !prev);
  }, []);

  useEffect(() => {
    if (mapboxMap && mapContainerRef.current) {
      const resizeMap = () => { mapboxMap.resize(); };
      const id = requestAnimationFrame(resizeMap);
      return () => cancelAnimationFrame(id);
    }
  }, [mapboxMap, isThematicMode, isSidebarOpen]);

  const handleDrawnGeometry = useCallback(async (geometry) => {
    setDrawnGeometry(geometry);
    if (geometry) {
      const userSelectedLayers = Object.keys(activeLayers).filter(key => activeLayers[key] === true);
      if (userSelectedLayers.length === 0) {
        console.warn("No active layers to perform spatial query against.");
        return;
      }
      try {
        const response = await fetch('http://localhost:8000/api/spatial-query', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ drawn_boundary: geometry, target_layers: userSelectedLayers }),
        });
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        const queriedFeatures = data.features || [];
        setSpatialQueryResults(queriedFeatures);
        setHighlightedFeatures(queriedFeatures);
      } catch (error) {
        console.error('Error during spatial query:', error);
        setSpatialQueryResults(null);
        setHighlightedFeatures(null);
      }
    } else {
      setSpatialQueryResults(null);
      setHighlightedFeatures(null);
    }
  }, [activeLayers]);

  const handleSearch = useCallback(async (query) => {
    if (!query || !mapboxMap) return;
    try {
      const res = await fetch(`http://localhost:8000/api/geocode?query=${encodeURIComponent(query)}`);
      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.detail || `HTTP error! Status: ${res.status}`);
      }
      const data = await res.json();
      if (data && data.lat && data.lon) {
        const { lat, lon, bounds } = data;
        const globalSpanThreshold = 100;
        let longitudeSpan = 0;
        let useFitBounds = false;
        if (bounds && bounds.length === 4) {
          longitudeSpan = Math.abs(parseFloat(bounds[2]) - parseFloat(bounds[0]));
          if (longitudeSpan < globalSpanThreshold) useFitBounds = true;
        }
        if (useFitBounds) {
          mapboxMap.fitBounds(bounds, { padding: 50, duration: 1000, maxZoom: 15, minZoom: 5 });
        } else {
          const zoom = (bounds && longitudeSpan >= globalSpanThreshold) ? 3.5 : 10;
          mapboxMap.flyTo({ center: [lon, lat], zoom, duration: 1000 });
        }
      } else {
        alert("Location not found. Please try a different query.");
      }
    } catch (error) {
      console.error("Search failed:", error);
      alert(`Search failed: ${error.message || error}`);
    }
  }, [mapboxMap]);

  useEffect(() => {
    if (mapContainerRef.current && !mapboxMap) {
      const map = new mapboxgl.Map({
        container: mapContainerRef.current,
        style: "mapbox://styles/mapbox/streets-v11",
        center: [-160, 75],
        zoom: 3.35,
        projection: "globe",
      });
      map.on('load', () => {
        map.setFog({
          "color": "rgba(255,255,255,0)",
          "high-color": "rgba(255,255,255,0)",
          "space-color": "rgba(0,0,0,0)",
          "star-intensity": 0,
          "horizon-blend": 0,
        });
        setMapboxMap(map);
      });
      return () => {
        if (map) { map.remove(); setMapboxMap(null); }
      };
    }
  }, []);

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100vh", width: "100vw", overflow: 'hidden' }}>

      <Toolbar
        isThematicMode={isThematicMode}
        onThematicModeToggle={handleThematicModeToggle}
        drawRef={drawRef}
        onDrawGeometry={handleDrawnGeometry}
        onSearch={handleSearch}
        mapboxMap={mapboxMap}
      />

      <div style={{ display: "flex", flex: 1, overflow: 'hidden' }}>

        {!isThematicMode && (
          <Sidebar
            onLayerToggle={handleLayerToggle}
            isThematicMode={isThematicMode}
            onThematicModeToggle={handleThematicModeToggle}
            isSidebarOpen={isSidebarOpen}
          />
        )}

        <div style={{ flexGrow: 1, height: '100%', position: 'relative' }}>
          <div
            ref={mapContainerRef}
            style={{ width: '100%', height: '100%', position: 'absolute', top: 0, left: 0 }}
          />

          {!isThematicMode && (
            <div
              className={`sidebar-toggle-button ${isSidebarOpen ? 'is-open' : 'is-closed'}`}
              onClick={toggleSidebar}
            >
              {isSidebarOpen ? '◀' : '▶'}
            </div>
          )}

          {!mapboxMap ? (
            <div style={{
              position: 'absolute', top: 0, left: 0, right: 0, bottom: 0,
              display: 'flex', justifyContent: 'center', alignItems: 'center',
              backgroundColor: 'rgba(255,255,255,0.69)', zIndex: 999,
              color: 'black', fontSize: '1.5em',
            }}>
              Loading map...
            </div>
          ) : (
            <>
              {!isThematicMode ? (
                <Map
                  mapboxMap={mapboxMap}
                  activeLayers={activeLayers}
                  onDrawGeometry={handleDrawnGeometry}
                  highlightedFeatures={highlightedFeatures}
                  isSidebarOpen={isSidebarOpen}
                  drawRef={drawRef}
                />
              ) : (
                <ThematicMap mapboxMap={mapboxMap} />
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;