#!/bin/bash
# Startup script for Community Arctic Map on Cloud Run
# This script:
# 1. Verifies the database file is accessible from GCS mount
# 2. Starts the zip_downloads service on port 8001
# 3. Starts the main API service on port 8000 (Cloud Run default)

set -e

echo "=============================================="
echo "Community Arctic Map - Startup"
echo "=============================================="

# Check if database is accessible from GCS mount
echo "[INFO] Checking for database file at /app/database/cpad.sqlite..."
if [ -f /app/database/cpad.sqlite ]; then
    FILE_SIZE=$(du -h /app/database/cpad.sqlite | cut -f1)
    echo "[INFO] ✅ Database found (size: $FILE_SIZE)"
else
    echo "[ERROR] ❌ Database not found at /app/database/cpad.sqlite"
    echo "[ERROR] Please ensure cpad.sqlite is uploaded to the GCS bucket"
    echo "[ERROR] Upload with: gsutil cp backend/cpad.sqlite gs://\${GCP_PROJECT_ID}-community-arctic-map-data/cpad.sqlite"
fi

# Change to backend directory
cd /app/backend

# Debug: List files in backend directory
echo "[DEBUG] Contents of /app/backend:"
ls -la /app/backend/

# Debug: Check if Python files exist
if [ -f "production.py" ]; then
    echo "[DEBUG] ✅ production.py found"
else
    echo "[DEBUG] ❌ production.py NOT found"
fi

if [ -f "zip_downloads.py" ]; then
    echo "[DEBUG] ✅ zip_downloads.py found"
else
    echo "[DEBUG] ❌ zip_downloads.py NOT found"
fi

# Start zip_downloads service on port 8001 in background
echo "[INFO] Starting zip_downloads service on port 8001..."
uvicorn zip_downloads:app --host 0.0.0.0 --port 8001 &
ZIP_PID=$!
echo "[INFO] zip_downloads service started (PID: $ZIP_PID)"

# Start main service with production config on PORT (provided by Cloud Run) or default 8000
PORT=${PORT:-8000}
echo "[INFO] Starting main service on port $PORT..."
exec uvicorn production:app --host 0.0.0.0 --port $PORT

# Note: exec replaces the shell with uvicorn, so this line is never reached
# If the main service exits, the container will stop
