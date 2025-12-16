# 🚀 Deployment Guide for Community Arctic Map

Complete guide for deploying the Community Arctic Map application to Google Cloud Run.

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Detailed Setup](#detailed-setup)
- [GitHub Actions Deployment](#github-actions-deployment)
- [Manual Deployment](#manual-deployment)
- [Database Management](#database-management)
- [Troubleshooting](#troubleshooting)

---

## Overview

**Technology Stack:**
- Frontend: React + Vite
- Backend: Python FastAPI (2 services)
- Database: SQLite (4.3 GB) stored in Google Cloud Storage
- Hosting: Google Cloud Run (serverless)
- CI/CD: GitHub Actions

**Deployment Flow:**
1. Code pushed to GitHub
2. GitHub Actions builds Docker image
3. Image pushed to Artifact Registry
4. Deployed to Cloud Run with database mounted from GCS

---

## Prerequisites

### Required Tools

1. **Google Cloud SDK** (`gcloud`)
   ```bash
   # Install from: https://cloud.google.com/sdk/docs/install
   # Verify installation:
   gcloud --version
   ```

2. **GitHub CLI** (`gh`)
   ```bash
   # Install from: https://cli.github.com/
   # Verify installation:
   gh --version
   ```

3. **Docker** (for local testing)
   ```bash
   # Install from: https://docs.docker.com/get-docker/
   # Verify installation:
   docker --version
   ```

### Required Accounts

- **Google Cloud Platform**: Billing enabled, project created
- **GitHub**: Repository admin access
- **Mapbox**: Free account for access token

### Environment Variables Needed

```bash
# GCP Configuration
export GCP_PROJECT_ID="your-project-id"
export GCP_REGION="us-east1"

# Application Secrets
export VITE_MAPBOX_ACCESS_TOKEN="pk.your_mapbox_token"
export GOOGLE_SHEET_ID="your_google_sheet_id"
export GOOGLE_SHEET_GID="your_google_sheet_gid"
```

---

## Quick Start

### Automated Setup (Recommended)

```bash
# 1. Clone repository
git clone https://github.com/brown-ccv/community-arctic-map.git
cd community-arctic-map

# 2. Set your GCP project
export GCP_PROJECT_ID="your-project-id"

# 3. Run setup script
./.deployment/scripts/gcp/setup-service-account.sh

# 4. Upload database to Cloud Storage
gsutil cp backend/cpad.sqlite gs://${GCP_PROJECT_ID}-community-arctic-map-data/cpad.sqlite

# 5. Configure GitHub secrets
gh secret set GCP_SERVICE_ACCOUNT_KEY < service-account-key.json
gh secret set VITE_MAPBOX_ACCESS_TOKEN --body "your_mapbox_token"
gh secret set GOOGLE_SHEET_ID --body "your_sheet_id"
gh secret set GOOGLE_SHEET_GID --body "your_gid"

# 6. Deploy via GitHub Actions
gh workflow run deploy.yml --ref main
```

---

## Detailed Setup

### Phase 1: Google Cloud Setup

#### 1. Create GCP Project

```bash
# Set project ID
export GCP_PROJECT_ID="your-project-id"

# Create project
gcloud projects create $GCP_PROJECT_ID --name="Community Arctic Map"

# Set as default
gcloud config set project $GCP_PROJECT_ID

# Enable billing (must be done via console)
echo "Enable billing at: https://console.cloud.google.com/billing/linkedaccount?project=${GCP_PROJECT_ID}"
```

#### 2. Enable Required APIs

```bash
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  storage.googleapis.com \
  iamcredentials.googleapis.com
```

#### 3. Create Service Account

```bash
# Create service account
gcloud iam service-accounts create community-arctic-map-sa \
  --display-name="Community Arctic Map Service Account"

# Grant required roles
for role in \
  roles/run.admin \
  roles/storage.admin \
  roles/artifactregistry.writer \
  roles/iam.serviceAccountUser; do
  gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
    --member="serviceAccount:community-arctic-map-sa@${GCP_PROJECT_ID}.iam.gserviceaccount.com" \
    --role="$role"
done

# Create and download key
gcloud iam service-accounts keys create service-account-key.json \
  --iam-account=community-arctic-map-sa@${GCP_PROJECT_ID}.iam.gserviceaccount.com
```

#### 4. Create Artifact Registry Repository

```bash
gcloud artifacts repositories create arctic-map-repo \
  --repository-format=docker \
  --location=us-east1 \
  --description="Docker repository for Community Arctic Map"
```

#### 5. Create Cloud Storage Bucket

```bash
# Create bucket
gsutil mb -l us-east1 gs://${GCP_PROJECT_ID}-community-arctic-map-data

# Set permissions
gsutil iam ch \
  serviceAccount:community-arctic-map-sa@${GCP_PROJECT_ID}.iam.gserviceaccount.com:objectViewer \
  gs://${GCP_PROJECT_ID}-community-arctic-map-data
```

### Phase 2: Database Upload

```bash
# Upload database file (4.3 GB - may take several minutes)
gsutil cp backend/cpad.sqlite gs://${GCP_PROJECT_ID}-community-arctic-map-data/cpad.sqlite

# Verify upload
gsutil ls -lh gs://${GCP_PROJECT_ID}-community-arctic-map-data/
```

### Phase 3: GitHub Secrets Configuration

```bash
# Set service account key
gh secret set GCP_SERVICE_ACCOUNT_KEY < service-account-key.json

# Set application secrets
gh secret set VITE_MAPBOX_ACCESS_TOKEN --body "pk.your_mapbox_token_here"
gh secret set GOOGLE_SHEET_ID --body "your_google_sheet_id"
gh secret set GOOGLE_SHEET_GID --body "your_gid"
```

Verify secrets:
```bash
gh secret list
```

---

## GitHub Actions Deployment

### Trigger Deployment

```bash
# Deploy from main branch
gh workflow run deploy.yml --ref main

# Monitor progress
gh run watch

# View logs
gh run view --log
```

### Workflow Overview

The deployment workflow (`.github/workflows/deploy.yml`) performs:

1. **Prepare Phase:**
   - Validates configuration
   - Authenticates to GCP
   - Checks required secrets

2. **Deploy Phase:**
   - Builds Docker image with multi-stage build
   - Pushes to Artifact Registry
   - Deploys to Cloud Run with:
     - 2 CPU, 2GB RAM
     - Database mounted from GCS bucket
     - Environment variables configured
     - Public access enabled

3. **Verify Phase:**
   - Checks service health
   - Reports deployment URL

### Get Service URL

```bash
gcloud run services describe community-arctic-map \
  --region=us-east1 \
  --format='value(status.url)'
```

---

## Manual Deployment

### Build Docker Image Locally

```bash
docker build \
  --build-arg VITE_MAPBOX_ACCESS_TOKEN=$VITE_MAPBOX_ACCESS_TOKEN \
  --build-arg GOOGLE_SHEET_ID=$GOOGLE_SHEET_ID \
  --build-arg GOOGLE_SHEET_GID=$GOOGLE_SHEET_GID \
  -t community-arctic-map:local \
  .
```

### Test Locally

```bash
# Run with database mounted
docker run -d \
  --name community-arctic-map \
  -p 8000:8000 \
  -v "$(pwd)/backend/cpad.sqlite:/app/database/cpad.sqlite:ro" \
  -e GOOGLE_SHEET_ID=$GOOGLE_SHEET_ID \
  -e GOOGLE_SHEET_GID=$GOOGLE_SHEET_GID \
  community-arctic-map:local

# Test
curl http://localhost:8000/api/layer_hierarchy

# View logs
docker logs -f community-arctic-map

# Stop
docker stop community-arctic-map && docker rm community-arctic-map
```

### Push to Artifact Registry

```bash
# Authenticate
gcloud auth configure-docker us-east1-docker.pkg.dev

# Tag image
docker tag community-arctic-map:local \
  us-east1-docker.pkg.dev/${GCP_PROJECT_ID}/arctic-map-repo/community-arctic-map:latest

# Push
docker push us-east1-docker.pkg.dev/${GCP_PROJECT_ID}/arctic-map-repo/community-arctic-map:latest
```

### Deploy to Cloud Run

```bash
gcloud run deploy community-arctic-map \
  --image=us-east1-docker.pkg.dev/${GCP_PROJECT_ID}/arctic-map-repo/community-arctic-map:latest \
  --region=us-east1 \
  --platform=managed \
  --allow-unauthenticated \
  --service-account=community-arctic-map-sa@${GCP_PROJECT_ID}.iam.gserviceaccount.com \
  --cpu=2 \
  --memory=2Gi \
  --timeout=300 \
  --add-volume=name=database,type=cloud-storage,bucket=${GCP_PROJECT_ID}-community-arctic-map-data \
  --add-volume-mount=volume=database,mount-path=/app/database \
  --set-env-vars=GOOGLE_SHEET_ID=$GOOGLE_SHEET_ID,GOOGLE_SHEET_GID=$GOOGLE_SHEET_GID
```

---

## Database Management

### Database Path Detection

The application automatically detects the database location:

1. Checks `/app/database/cpad.sqlite` (Docker/Cloud Run with volume mount)
2. Falls back to `backend/cpad.sqlite` (local development)

No configuration needed - it just works!

### Update Database

```bash
# Upload new version
gsutil cp backend/cpad.sqlite gs://${GCP_PROJECT_ID}-community-arctic-map-data/cpad.sqlite

# Force Cloud Run to use new version (restart service)
gcloud run services update community-arctic-map \
  --region=us-east1 \
  --update-env-vars=DB_UPDATED=$(date +%s)
```

### Download Production Database

```bash
gsutil cp gs://${GCP_PROJECT_ID}-community-arctic-map-data/cpad.sqlite ./backend/cpad.sqlite
```

---

## Troubleshooting

### Check Service Status

```bash
# Service info
gcloud run services describe community-arctic-map --region=us-east1

# View logs
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=community-arctic-map" --limit=50 --format=json

# Stream logs
gcloud alpha run services logs tail community-arctic-map --region=us-east1
```

### Common Issues

#### Database not found

```bash
# Check if database exists in bucket
gsutil ls -lh gs://${GCP_PROJECT_ID}-community-arctic-map-data/

# Check volume mount
gcloud run services describe community-arctic-map --region=us-east1 --format="value(spec.template.spec.volumes)"
```

**Solution:** Ensure database is uploaded and volume is properly mounted.

#### No themes/subthemes appearing

```bash
# Check environment variables
gcloud run services describe community-arctic-map --region=us-east1 --format="value(spec.template.spec.containers[0].env)"
```

**Solution:** Update GitHub secrets and redeploy:
```bash
gh secret set GOOGLE_SHEET_ID --body "1TaDGGnUw00DaFtldVNYib8EGi6WbXOX01rNJAFWjmgI"
gh secret set GOOGLE_SHEET_GID --body "583540745"
gh workflow run deploy.yml --ref main
```

#### Container fails to start

```bash
# View recent logs
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=community-arctic-map AND severity>=ERROR" --limit=20
```

**Solution:** Check build logs in GitHub Actions for errors.

#### Port conflicts locally

The application uses:
- Port 8000: Main API + Frontend (Docker mode) OR Backend only (dev mode)
- Port 8001: Download service
- Port 5173: Frontend dev server (dev mode only)

**Solution:** Ensure ports are available or modify in `run.sh` / `start.sh`.

### Verify Deployment

```bash
# Get service URL
URL=$(gcloud run services describe community-arctic-map --region=us-east1 --format='value(status.url)')

# Test endpoints
curl $URL/api/layer_hierarchy
curl $URL/api/geojson/a_alaska_schools
```

### Environment Variables Check

```bash
# List all env vars
gcloud run services describe community-arctic-map \
  --region=us-east1 \
  --format="table(spec.template.spec.containers[0].env[])"
```

---

## Cleanup / Teardown

To remove all resources:

```bash
# Delete Cloud Run service
gcloud run services delete community-arctic-map --region=us-east1 --quiet

# Delete Artifact Registry repository
gcloud artifacts repositories delete arctic-map-repo --location=us-east1 --quiet

# Delete Cloud Storage bucket
gsutil rm -r gs://${GCP_PROJECT_ID}-community-arctic-map-data

# Delete service account
gcloud iam service-accounts delete community-arctic-map-sa@${GCP_PROJECT_ID}.iam.gserviceaccount.com --quiet

# (Optional) Delete project
gcloud projects delete $GCP_PROJECT_ID --quiet
```

---

## Additional Resources

- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Artifact Registry Documentation](https://cloud.google.com/artifact-registry/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Main Project README](../README.md)
- [Backend README](../backend/README.md)
- [Frontend README](../frontend/README.md)

---

## Support

For issues or questions:
- Check [Troubleshooting](#troubleshooting) section
- Review GitHub Actions logs
- Check Cloud Run logs in GCP Console
- Contact: Brown University Center for Computation and Visualization
