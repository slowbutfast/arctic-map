import React, { useEffect, useCallback } from 'react';
import MapboxDraw from '@mapbox/mapbox-gl-draw';
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css';

const DrawControls = ({ map, onDrawGeometry, drawRef }) => {

  const handleDrawChange = useCallback(() => {
    if (!drawRef || !drawRef.current) return;
    const features = drawRef.current.getAll().features;
    if (features.length > 0 && onDrawGeometry) {
      onDrawGeometry(features[features.length - 1]);
    } else if (onDrawGeometry) {
      onDrawGeometry(null);
    }
  }, [onDrawGeometry, drawRef]);

  useEffect(() => {
    if (!map) return;

    if (!drawRef.current) {
      drawRef.current = new MapboxDraw({
        displayControlsDefault: false,
        controls: { polygon: false, point: false, line_string: false, trash: false },
      });
      map.addControl(drawRef.current, 'top-left');
      map.on('draw.create', handleDrawChange);
      map.on('draw.update', handleDrawChange);
      map.on('draw.delete', () => {
        if (onDrawGeometry) onDrawGeometry(null);
      });
    }

    return () => {
      if (map && drawRef.current) {
        map.removeControl(drawRef.current);
        map.off('draw.create', handleDrawChange);
        map.off('draw.update', handleDrawChange);
        map.off('draw.delete');
        drawRef.current = null;
        if (onDrawGeometry) onDrawGeometry(null);
      }
    };
  }, [map, handleDrawChange, onDrawGeometry, drawRef]);

  return null;
};

export default DrawControls;