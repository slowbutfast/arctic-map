#!/bin/bash
# Validation script for GCP setup
# This script checks if all required GCP resources are properly configured

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}==================================================================${NC}"
echo -e "${GREEN}🔍 Validating GCP Configuration${NC}"
echo -e "${GREEN}==================================================================${NC}"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}❌ Error: gcloud CLI is not installed${NC}"
    exit 1
fi

# Get project ID
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [ -z "$PROJECT_ID" ]; then
    echo -e "${RED}❌ Error: No GCP project configured${NC}"
    echo "Run: gcloud config set project YOUR_PROJECT_ID"
    exit 1
fi

echo -e "${GREEN}📊 Validating Project: $PROJECT_ID${NC}"
echo ""

# Variables
SERVICE_NAME="arctic-map"
SERVICE_ACCOUNT_NAME="${SERVICE_NAME}-sa"
SERVICE_ACCOUNT_EMAIL="${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
REGION="us-east1"
ARTIFACT_REGISTRY_REPO="arctic-map-repo"
BUCKET_NAME="${PROJECT_ID}-${SERVICE_NAME}-data"

ERRORS=0

# Check APIs
echo -e "${YELLOW}🔌 Checking required APIs...${NC}"
REQUIRED_APIS=(
    "run.googleapis.com"
    "artifactregistry.googleapis.com"
    "cloudbuild.googleapis.com"
    "secretmanager.googleapis.com"
    "storage.googleapis.com"
)

for api in "${REQUIRED_APIS[@]}"; do
    if gcloud services list --enabled --filter="name:$api" --project="$PROJECT_ID" 2>/dev/null | grep -q "$api"; then
        echo -e "  ${GREEN}✅ $api${NC}"
    else
        echo -e "  ${RED}❌ $api (not enabled)${NC}"
        ((ERRORS++))
    fi
done
echo ""

# Check service account
echo -e "${YELLOW}👤 Checking service account...${NC}"
if gcloud iam service-accounts describe "$SERVICE_ACCOUNT_EMAIL" --project="$PROJECT_ID" &> /dev/null; then
    echo -e "  ${GREEN}✅ Service account exists: $SERVICE_ACCOUNT_EMAIL${NC}"
else
    echo -e "  ${RED}❌ Service account not found: $SERVICE_ACCOUNT_EMAIL${NC}"
    ((ERRORS++))
fi
echo ""

# Check Artifact Registry repository
echo -e "${YELLOW}📦 Checking Artifact Registry repository...${NC}"
if gcloud artifacts repositories describe "$ARTIFACT_REGISTRY_REPO" \
    --location="$REGION" \
    --project="$PROJECT_ID" &> /dev/null; then
    echo -e "  ${GREEN}✅ Artifact Registry repository exists${NC}"
else
    echo -e "  ${RED}❌ Artifact Registry repository not found${NC}"
    ((ERRORS++))
fi
echo ""

# Check Cloud Storage bucket
echo -e "${YELLOW}🗄️  Checking Cloud Storage bucket...${NC}"
if gsutil ls -b "gs://$BUCKET_NAME" &> /dev/null; then
    echo -e "  ${GREEN}✅ Storage bucket exists: gs://$BUCKET_NAME${NC}"
    
    # Check if cpad.sqlite exists
    if gsutil ls "gs://$BUCKET_NAME/cpad.sqlite" &> /dev/null; then
        echo -e "  ${GREEN}✅ Database file uploaded: cpad.sqlite${NC}"
    else
        echo -e "  ${YELLOW}⚠️  Database file not found: cpad.sqlite${NC}"
        echo "     Upload with: gsutil cp backend/cpad.sqlite gs://$BUCKET_NAME/cpad.sqlite"
    fi
else
    echo -e "  ${RED}❌ Storage bucket not found: gs://$BUCKET_NAME${NC}"
    ((ERRORS++))
fi
echo ""

# Check secrets
echo -e "${YELLOW}🔐 Checking Secret Manager secrets...${NC}"
REQUIRED_SECRETS=("GOOGLE_SHEET_ID" "GOOGLE_SHEET_GID")
for secret in "${REQUIRED_SECRETS[@]}"; do
    if gcloud secrets describe "$secret" --project="$PROJECT_ID" &> /dev/null; then
        echo -e "  ${GREEN}✅ Secret exists: $secret${NC}"
    else
        echo -e "  ${YELLOW}⚠️  Secret not found: $secret (optional)${NC}"
    fi
done
echo ""

# Check Cloud Run service
echo -e "${YELLOW}🚀 Checking Cloud Run service...${NC}"
if gcloud run services describe "$SERVICE_NAME" --region="$REGION" --project="$PROJECT_ID" &> /dev/null; then
    echo -e "  ${GREEN}✅ Cloud Run service exists${NC}"
    
    SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" \
        --region="$REGION" \
        --project="$PROJECT_ID" \
        --format='value(status.url)')
    echo -e "  ${GREEN}🌐 Service URL: $SERVICE_URL${NC}"
else
    echo -e "  ${YELLOW}⚠️  Cloud Run service not deployed yet${NC}"
fi
echo ""

# Summary
echo -e "${GREEN}==================================================================${NC}"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ All validations passed!${NC}"
    echo -e "${GREEN}==================================================================${NC}"
    echo ""
    echo -e "${YELLOW}📋 Configuration is ready for deployment${NC}"
else
    echo -e "${RED}❌ $ERRORS validation error(s) found${NC}"
    echo -e "${GREEN}==================================================================${NC}"
    echo ""
    echo -e "${YELLOW}📋 Please fix the errors and run validation again${NC}"
    exit 1
fi
echo ""
