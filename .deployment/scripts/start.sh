#!/bin/bash
# Startup script for Arctic Map on Cloud Run
# This script:
# 1. Verifies the database file is accessible from GCS mount
# 2. Starts the zip_downloads service on port 8001
# 3. Starts the main API service on port 8000 (Cloud Run default)

set -e

echo "=============================================="
echo "Arctic Map - Startup"
echo "=============================================="

# Check if database is accessible from GCS mount
if [ -f /app/database/cpad.sqlite ]; then
    FILE_SIZE=$(du -h /app/database/cpad.sqlite | cut -f1)
    echo "[INFO] ✅ Database found (size: $FILE_SIZE)"
else
    echo "[ERROR] ❌ Database not found at /app/database/cpad.sqlite"
    echo "[ERROR] Please ensure cpad.sqlite is uploaded to the GCS bucket"
    exit 1
fi

# Change to backend directory
cd /app/backend

# Start zip_downloads service on port 8001 in background
echo "[INFO] Starting zip_downloads service on port 8001..."
uvicorn zip_downloads:app --host 0.0.0.0 --port 8001 &

# Start main service with production config on PORT (provided by Cloud Run) or default 8000
PORT=${PORT:-8000}
echo "[INFO] Starting main service on port $PORT..."
exec uvicorn production:app --host 0.0.0.0 --port $PORT
