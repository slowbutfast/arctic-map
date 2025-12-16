# API Configuration System

This document explains the centralized API URL configuration for the Community Arctic Map application.

## Overview

The application uses a centralized API configuration system that automatically adapts to different environments:
- **Development**: Points to `http://localhost:8000` (separate backend server)
- **Production**: Uses relative URLs (same origin as frontend)

## Files

### Configuration Files

- **`frontend/src/config/api.js`**: Centralized API configuration module (auto-detects environment)

### How It Works

The system automatically detects the environment based on the frontend dev server port:
- **Development** (when `window.location.port` is `'5173'`): Uses `http://localhost:8000`
- **Production** (any other port or no port): Uses relative URLs (empty string)

This means the frontend knows it's in development mode only when running on Vite's dev server (port 5173).

## Usage

### In React Components

Import and use the `getApiUrl` function:

```jsx
import { getApiUrl } from '../config/api';

// In your component
const response = await fetch(getApiUrl('/api/layer_hierarchy'));
```

### Available Functions

#### `getApiUrl(endpoint)`
Returns the full API URL for a given endpoint.

```javascript
// Development: returns "http://localhost:8000/api/layer_hierarchy"
// Production: returns "/api/layer_hierarchy"
const url = getApiUrl('/api/layer_hierarchy');
```

#### `apiFetch(endpoint, options)`
Convenience wrapper around fetch with automatic URL resolution.

```javascript
const response = await apiFetch('/api/layer_hierarchy');
const data = await response.json();
```

#### `API_BASE_URL`
Direct access to the base URL constant.

```javascript
import { API_BASE_URL } from '../config/api';
console.log('API base:', API_BASE_URL);
```

## Setup

### Development Setup

1. **Start backend** (in terminal 1):
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

2. **Start frontend** (in terminal 2):
   ```bash
   cd frontend
   npm run dev
   ```

### Production Setup

Production configuration is handled automatically:

1. The `api.js` module detects non-localhost hostname and uses relative URLs
2. **`VITE_MAPBOX_ACCESS_TOKEN`** is set via Docker build args
3. Backend serves the frontend from the same origin

### Development Mode

```
Frontend (localhost:5173)  →  Backend (localhost:8000)
     ↓
Detects port = '5173'
     ↓
Uses absolute URL: http://localhost:8000/api/...
```

### Production Mode

```
Browser → Cloud Run (port 8000)
                ↓
        ┌───────┴────────┐
        ↓                ↓
   Frontend          Backend
   (/, /assets)      (/api/*)
        ↓
Detects port ≠ '5173'
        ↓
Uses relative URL: /api/...
(Same origin, no CORS issues)
```

## Migration Guide

If you're updating old code that uses hardcoded URLs:

### Before
```jsx
fetch('http://localhost:8000/api/layer_hierarchy')
```

### After
```jsx
import { getApiUrl } from '../config/api';

fetch(getApiUrl('/api/layer_hierarchy'))
```

## Troubleshooting

### Issue: API calls fail in development
**Solution**: Ensure backend is running on port 8000
```bash
cd backend
uvicorn main:app --reload --port 8000
```

### Issue: API calls fail in production
**Solution**: The system auto-detects based on port 5173. If you're testing locally with Docker or another setup, ensure you're not running on port 5173 (which would trigger dev mode).

### Issue: API calls go to wrong URL
**Solution**: Check the browser console to see what `API_BASE_URL` is being used:
```javascript
import { API_BASE_URL } from './config/api';
console.log('API Base URL:', API_BASE_URL);
console.log('Current port:', window.location.port);
```

### Issue: CORS errors in development
**Solution**: This is normal! The backend (main.py) already has CORS configured to allow all origins:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Benefits

✅ **Single source of truth** for API configuration  
✅ **Automatic environment detection**  
✅ **No hardcoded URLs** in components  
✅ **Easy to test** both locally and in production  
✅ **Runtime detection** - works without build-time configuration  
✅ **No CORS issues** in production (same origin)  
✅ **Zero configuration** - just works out of the box

## Related Files

- `backend/main.py` - FastAPI backend with API endpoints
- `backend/production.py` - Production wrapper that serves frontend and backend together
- `Dockerfile` - Multi-stage build that creates the production image
- `.github/workflows/deploy.yml` - CI/CD pipeline that builds and deploys
