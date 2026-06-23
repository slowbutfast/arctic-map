import logoDark from '../assets/logo.png';
import logoLight from '../assets/logo-light.png';
import React, { useState } from 'react';
import '../styles/Toolbar.css';

const MapIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6" />
    <line x1="8" y1="2" x2="8" y2="18" />
    <line x1="16" y1="6" x2="16" y2="22" />
  </svg>
);

const ThematicIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <rect x="3" y="3" width="7" height="7" rx="1" fill="currentColor" opacity="0.8"/>
    <rect x="14" y="3" width="7" height="7" rx="1" fill="currentColor" opacity="0.5"/>
    <rect x="3" y="14" width="7" height="7" rx="1" fill="currentColor" opacity="0.3"/>
    <rect x="14" y="14" width="7" height="7" rx="1" fill="currentColor" opacity="0.65"/>
  </svg>
);

const PolygonIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <path d="M12 2.5 L20.5 7.25 L20.5 16.75 L12 21.5 L3.5 16.75 L3.5 7.25 Z" />
  </svg>
);

const LineIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" aria-hidden="true">
    <path d="M4 20L20 4" />
  </svg>
);

const PointIcon = () => (
  <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
    <circle cx="12" cy="12" r="5" />
  </svg>
);

const ClearIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <path d="M3 6h18" /><path d="M8 6V4h8v2" />
    <path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6" />
    <path d="M10 11v6" /><path d="M14 11v6" />
  </svg>
);

const SearchIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <circle cx="11" cy="11" r="8" />
    <path d="M21 21l-4.35-4.35" />
  </svg>
);

const SettingsIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <circle cx="12" cy="12" r="3" />
    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" />
  </svg>
);

const Toolbar = ({ isThematicMode, onThematicModeToggle, drawRef, onDrawGeometry, onSearch, mapboxMap }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTool, setActiveTool] = useState(null);
  const [showAboutPopup, setShowAboutPopup] = useState(false);
  const [showSettingsPopup, setShowSettingsPopup] = useState(false);
  const [projection, setProjection] = useState('globe');
  const [atmosphereOn, setAtmosphereOn] = useState(false);

  const handleAtmosphereToggle = () => {
    const newValue = !atmosphereOn;
    setAtmosphereOn(newValue);
    if (mapboxMap) {
      if (newValue) {
        mapboxMap.setFog({
          color: "white",
          "high-color": "#add8e6",
          "horizon-blend": 0.2,
          "space-color": "#000000",
          "star-intensity": 0.15,
        });
      } else {
        mapboxMap.setFog({
          "color": "rgba(255,255,255,0)",
          "high-color": "rgba(255,255,255,0)",
          "space-color": "rgba(0,0,0,0)",
          "star-intensity": 0,
          "horizon-blend": 0,
        });
      }
    }
  };

  const PROJECTIONS = [
    { id: 'globe', label: 'Globe' },
    { id: 'mercator', label: 'Mercator' },
    { id: 'naturalEarth', label: 'Natural Earth' },
    { id: 'equalEarth', label: 'Equal Earth' },
    { id: 'albers', label: 'Albers (USA)' },
    { id: 'winkelTripel', label: 'Winkel Tripel' },
  ];

  const handleProjectionChange = (id) => {
    setProjection(id);
    if (mapboxMap) {
      mapboxMap.setProjection(id);
    }
  };

  const activateTool = (mode) => {
    if (drawRef && drawRef.current) {
      drawRef.current.changeMode(mode);
    }
    setActiveTool(mode);
  };

  const clearDrawing = () => {
    if (drawRef && drawRef.current) {
      drawRef.current.deleteAll();
      drawRef.current.changeMode('simple_select');
    }
    setActiveTool(null);
    if (onDrawGeometry) onDrawGeometry(null);
  };

  const handleSearch = async () => {
    if (!searchQuery.trim() || !onSearch) return;
    onSearch(searchQuery);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') handleSearch();
  };

  return (
    <>
    <div className="toolbar" role="toolbar" aria-label="Map toolbar">

      <div className="toolbar-logo">
         <img src={logoDark} alt="ArcticMap" className="toolbar-logo-img toolbar-logo-img--dark" />
        <img src={logoLight} alt="ArcticMap" className="toolbar-logo-img toolbar-logo-img--light" />
      </div>

      <div className="toolbar-divider" aria-hidden="true" />

      <div className="toolbar-section">
        <span className="toolbar-section-label">INFO</span>
        <div className="toolbar-buttons">
          <button
            className="toolbar-btn"
            onClick={() => setShowAboutPopup(true)}
            aria-label="About Arctic Map"
          >
            <span className="toolbar-btn-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="16" x2="12" y2="12" />
                <line x1="12" y1="8" x2="12.01" y2="8" />
              </svg>
            </span>
            <span className="toolbar-btn-label">About</span>
          </button>
        </div>
      </div>

      <div className="toolbar-divider" aria-hidden="true" />

      <div className="toolbar-section">
        <span className="toolbar-section-label">MAP</span>
        <div className="toolbar-buttons">
          <button
            className={`toolbar-btn ${!isThematicMode ? 'toolbar-btn--active' : ''}`}
            onClick={() => isThematicMode && onThematicModeToggle()}
            aria-label="Switch to Main Map"
            aria-pressed={!isThematicMode}
          >
            <span className="toolbar-btn-icon"><MapIcon /></span>
            <span className="toolbar-btn-label">Main Map</span>
          </button>
          <button
            className={`toolbar-btn ${isThematicMode ? 'toolbar-btn--active' : ''}`}
            onClick={() => !isThematicMode && onThematicModeToggle()}
            aria-label="Switch to Thematic Map"
            aria-pressed={isThematicMode}
          >
            <span className="toolbar-btn-icon"><ThematicIcon /></span>
            <span className="toolbar-btn-label">Thematic</span>
          </button>
        </div>
      </div>

      <div className="toolbar-divider" aria-hidden="true" />

      <div className="toolbar-section">
        <span className="toolbar-section-label">DRAW</span>
        <div className="toolbar-buttons">
          <button
            className={`toolbar-btn ${activeTool === 'draw_polygon' ? 'toolbar-btn--active' : ''}`}
            onClick={() => activateTool('draw_polygon')}
            aria-label="Draw polygon"
            aria-pressed={activeTool === 'draw_polygon'}
          >
            <span className="toolbar-btn-icon"><PolygonIcon /></span>
            <span className="toolbar-btn-label">Polygon</span>
          </button>
          <button
            className={`toolbar-btn ${activeTool === 'draw_line_string' ? 'toolbar-btn--active' : ''}`}
            onClick={() => activateTool('draw_line_string')}
            aria-label="Draw line"
            aria-pressed={activeTool === 'draw_line_string'}
          >
            <span className="toolbar-btn-icon"><LineIcon /></span>
            <span className="toolbar-btn-label">Line</span>
          </button>
          <button
            className={`toolbar-btn ${activeTool === 'draw_point' ? 'toolbar-btn--active' : ''}`}
            onClick={() => activateTool('draw_point')}
            aria-label="Draw point"
            aria-pressed={activeTool === 'draw_point'}
          >
            <span className="toolbar-btn-icon"><PointIcon /></span>
            <span className="toolbar-btn-label">Point</span>
          </button>
          <button
            className="toolbar-btn toolbar-btn--danger"
            onClick={clearDrawing}
            aria-label="Clear all drawings"
          >
            <span className="toolbar-btn-icon"><ClearIcon /></span>
            <span className="toolbar-btn-label">Clear</span>
          </button>
        </div>
      </div>

      <div className="toolbar-divider" aria-hidden="true" />

      <div className="toolbar-section toolbar-section--search">
        <span className="toolbar-section-label">SEARCH</span>
        <div className="toolbar-search">
          <input
            className="toolbar-search-input"
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Search for a location..."
            aria-label="Search for a location"
          />
          <button
            className="toolbar-btn toolbar-search-btn"
            onClick={handleSearch}
            aria-label="Search"
          >
            <span className="toolbar-btn-icon"><SearchIcon /></span>
            <span className="toolbar-btn-label">Search</span>
          </button>
        </div>
      </div>

      <div className="toolbar-divider toolbar-divider--push" aria-hidden="true" />

      <div className="toolbar-section">
        <span className="toolbar-section-label">&nbsp;</span>
        <div className="toolbar-buttons">
          <button
            className="toolbar-btn"
            onClick={() => setShowSettingsPopup(true)}
            aria-label="Open settings"
          >
            <span className="toolbar-btn-icon"><SettingsIcon /></span>
            <span className="toolbar-btn-label">Settings</span>
          </button>
        </div>
      </div>

    </div>

    {showAboutPopup && (
      <div className="attribute-popup" role="dialog" aria-modal="true">
        <div className="popup-content">
          <h3>About Arctic Map</h3>
          <button className="close-btn" onClick={() => setShowAboutPopup(false)}>✕</button>
          <p>
            Arctic Map is a tool for exploring & analyzing a robust collection of 80+ cleaned, geospatial datasets related to the Arctic region.
            Explore the app's following features:
          </p>
          <ul style={{ paddingLeft: '20px', fontSize: '0.9em' }}>
            <li><strong>Layers:</strong> Toggle layers on and off to visualize different datasets.</li>
            <li><strong>Spatial Query:</strong> Use the drawing tools to select an area and find intersecting features.</li>
            <li><strong>Download Data:</strong> Download entire datasets as zipped shapefiles and custom areas/queries as GeoJSON files.</li>
            <li><strong>Thematic Map:</strong> Switch to Thematic Mode to color map layers based on attribute data.</li>
            <li><strong>Search:</strong> Use the search bar to find locations and features of interest.</li>
          </ul>
          <p>
            This web application is a project of the <a href="https://nna-cpad.org/">CPAD consortium</a> and is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.
          </p>
          <p>
            Credits: Developed by Brown University students Soujanya Aryal and Noreen Chen.
          </p>
        </div>
      </div>
    )}

    {showSettingsPopup && (
      <div className="attribute-popup" role="dialog" aria-modal="true">
        <div className="popup-content">
          <h3>Settings</h3>
          <button className="close-btn" onClick={() => setShowSettingsPopup(false)}>✕</button>
          <p>
            Adjust the map projection:
          </p>
          <div className="projection-options">
            {PROJECTIONS.map((proj) => (
              <button
                key={proj.id}
                className={`projection-btn ${projection === proj.id ? 'projection-btn--active' : ''}`}
                onClick={() => handleProjectionChange(proj.id)}
              >
                {proj.label}
              </button>
            ))}
          </div>

          <div style={{ marginTop: '16px', marginBottom: '12px' }}>
            <strong>Globe Atmosphere</strong>
          </div>
          <label style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer' }}>
            <input
              type="checkbox"
              checked={atmosphereOn}
              onChange={handleAtmosphereToggle}
            />
            Show atmosphere glow
          </label>
        </div>
      </div>
    )}

    </>
  );
};

export default Toolbar;