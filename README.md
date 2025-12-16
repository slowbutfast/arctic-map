# Arctic Map

For full documentation and setup instructions, please visit the [Wiki](https://github.com/soujanya957/arctic-map/wiki).

## 🚀 Deployment

This application is deployed on **Google Cloud Run** with automated CI/CD via GitHub Actions.

**Production URL:** [https://arctic-map-519427003190.us-east1.run.app](https://arctic-map-519427003190.us-east1.run.app)

### Quick Deploy

```bash
# 1. Set up GCP resources
./.deployment/scripts/gcp/setup-service-account.sh

# 2. Upload database to Cloud Storage
gsutil cp backend/cpad.sqlite gs://${GCP_PROJECT_ID}-arctic-map-data/cpad.sqlite

# 3. Configure GitHub secrets (interactive)
./.deployment/scripts/github/setup-github-secrets.sh

# 4. Deploy
gh workflow run deploy.yml --ref main
```

For complete deployment instructions, see the **[Deployment Guide](.deployment/DEPLOYMENT.md)**.

---

#### Developers:
Soujanya, Noreen
