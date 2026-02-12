# Agentic Graph RAG Backend
# Agentic Graph-Based RAG System

## Overview
This project implements a Retrieval-Augmented Generation system
with modular architecture separating retrieval, generation, and orchestration.

## Architecture
Retriever → Context Builder → Generator → Final Response

## How to Run
pip install -r requirements.txt
python main.py

## Evaluation
Basic regression test added in tests/ folder.


This README includes instructions for running, testing, and configuring CI publishing to container registries.

Running

```powershell
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Testing

```powershell
C:/Users/nithi/AppData/Local/Microsoft/WindowsApps/python3.11.exe -m pytest -q backend/tests
```

Docker Hub / GHCR secret setup

To enable CI publishing, add the following repository secrets in GitHub:

- For Docker Hub:
  - `DOCKERHUB_USERNAME` — your Docker Hub username
  - `DOCKERHUB_TOKEN` — a Docker Hub access token (recommended) or password

- For GitHub Container Registry (GHCR):
  - `GITHUB_TOKEN` — already available in Actions as a secret; no extra setup required for the default token

Notes:
- The workflow will detect the presence of these secrets and only run the corresponding publish steps. If both are present, it pushes to both registries.

CI: image tagging and auto-publish by Git tag

The CI workflow now supports auto-tagging images using Git tags. When you push a Git tag (for example `v1.2.3`) the CI job will:

1. Build the image.
2. Tag it as `:v1.2.3` and `:latest`.
3. Push to Docker Hub and/or GHCR depending on configured secrets.

To create a tag locally and push:

```powershell
git tag v1.2.3
git push origin v1.2.3
```

Mocking external services in tests

I added a small example fixture for mocking external services (LLM client, Neo4j already mocked in a test). Create additional fixtures in `backend/tests/conftest.py` to centralize mocks for reuse across tests.

Docker Hub token example

To create a Docker Hub access token:

1. Log in to Docker Hub and go to Account Settings > Security.
2. Create a new Access Token and copy it.
3. Add secrets to your GitHub repo (Settings > Secrets > Actions):
  - `DOCKERHUB_USERNAME` — your Docker Hub username
  - `DOCKERHUB_TOKEN` — the access token you created

You can add these from the command line using the GitHub CLI:

```bash
gh secret set DOCKERHUB_USERNAME --body "your-username"
gh secret set DOCKERHUB_TOKEN --body "<paste-your-token-here>"
```

