#!/bin/bash
# Setup script for creating GitHub Environments (staging and production)
# This script uses the GitHub API to create deployment environments with protection rules

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}==================================================================${NC}"
echo -e "${GREEN}🌍 GitHub Environments Setup for Arctic Map${NC}"
echo -e "${GREEN}==================================================================${NC}"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}❌ Error: GitHub CLI (gh) is not installed${NC}"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo -e "${RED}❌ Error: Not authenticated with GitHub CLI${NC}"
    exit 1
fi

# Get repository information
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null)
if [ -z "$REPO" ]; then
    echo -e "${RED}❌ Error: Could not determine repository${NC}"
    exit 1
fi

echo -e "${GREEN}📊 Repository: $REPO${NC}"
echo ""

# Function to create an environment
create_environment() {
    local env_name=$1
    local wait_timer=$2
    local reviewers=$3
    
    echo -e "${YELLOW}🌍 Creating environment: $env_name${NC}"
    
    # Create environment (this requires admin permissions)
    gh api \
        --method PUT \
        -H "Accept: application/vnd.github+json" \
        "/repos/$REPO/environments/$env_name" \
        -f "wait_timer=$wait_timer" \
        2>/dev/null && \
    echo -e "${GREEN}✅ Environment $env_name created${NC}" || \
    echo -e "${YELLOW}⚠️  Environment $env_name may already exist or you lack permissions${NC}"
    
    echo ""
}

echo -e "${YELLOW}📝 This script will create deployment environments${NC}"
echo "   - staging: No protection rules, for testing"
echo "   - production: With optional protection rules"
echo ""

# Create staging environment (no protection)
create_environment "staging" "0" ""

# Create production environment (with optional protection)
echo -e "${YELLOW}🔒 For production environment:${NC}"
echo -e "${YELLOW}   Do you want to add a wait timer? (seconds, 0 for no wait):${NC}"
read -r wait_timer
wait_timer=${wait_timer:-0}

create_environment "production" "$wait_timer" ""

# Summary
echo -e "${GREEN}==================================================================${NC}"
echo -e "${GREEN}✅ GitHub Environments Setup Complete!${NC}"
echo -e "${GREEN}==================================================================${NC}"
echo ""
echo -e "${YELLOW}📋 Next Steps:${NC}"
echo "1. Visit: https://github.com/$REPO/settings/environments"
echo "2. Configure additional protection rules if needed:"
echo "   - Required reviewers"
echo "   - Deployment branches"
echo "   - Environment secrets"
echo ""
echo -e "${YELLOW}💡 Tip:${NC}"
echo "   You can add environment-specific secrets in the GitHub UI"
echo "   Settings → Environments → [environment] → Add secret"
echo ""
