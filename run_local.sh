#!/bin/bash
# run_local.sh - Run the backend services and frontend concurrently without tmux

# Port definitions
BACKEND_PORT=8000
DOWNLOAD_PORT=8001

echo "=============================================="
echo "Arctic Map - Local Development Starter"
echo "=============================================="

# Store process IDs to kill them on exit
PIDS=()

# Function to clean up processes on Ctrl+C
cleanup() {
    echo ""
    echo "[INFO] Shutting down all services..."
    for pid in "${PIDS[@]}"; do
        if kill -0 "$pid" 2>/dev/null; then
            kill "$pid" 2>/dev/null
        fi
    done
    echo "[INFO] Done! All services stopped."
    exit 0
}

# Trap Ctrl+C (SIGINT) and SIGTERM
trap cleanup SIGINT SIGTERM

# 1. Start Main Backend Service (Port 8000)
echo "[INFO] Starting main backend service on port $BACKEND_PORT..."
cd backend
./venv/bin/python -m uvicorn main:app --reload --port $BACKEND_PORT --host 0.0.0.0 &
PIDS+=($!)
cd ..

# 2. Start Zip Downloads Service (Port 8001)
echo "[INFO] Starting zip downloads service on port $DOWNLOAD_PORT..."
cd backend
./venv/bin/python -m uvicorn zip_downloads:app --reload --port $DOWNLOAD_PORT --host 0.0.0.0 &
PIDS+=($!)
cd ..

# 3. Start Frontend Service (Vite Dev Server)
echo "[INFO] Starting frontend Vite dev server..."
cd frontend
# Ensure node_modules exists, otherwise install
if [ ! -d "node_modules" ]; then
    echo "[INFO] Installing frontend dependencies first..."
    npm install
fi
npm run dev -- --host &
PIDS+=($!)
cd ..

echo "=============================================="
echo "✅ All services started successfully!"
echo "👉 Backend API: http://localhost:$BACKEND_PORT"
echo "👉 Zip Download Service: http://localhost:$DOWNLOAD_PORT"
echo "=============================================="
echo "Press Ctrl+C to stop all services."
echo ""

# Keep script running to keep trapping Ctrl+C
wait
