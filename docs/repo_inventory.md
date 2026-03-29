# Repo Inventory

## Current Top-Level Structure
- `app/` - Python application package for config, DB access, models, repositories, services, schemas, and utilities
- `sql/` - PostgreSQL schema, indexes, reference data, views, reporting queries, and validation checks
- `streamlit_app/` - Analyst-facing Streamlit interface
- `scripts/` - Operational scripts for DB initialization, seeding, ingestion, synthetic data generation, and smoke testing
- `data/` - Example inputs plus generated raw and processed artifacts
- `tests/` - Schema, ingestion, query, provenance, and Streamlit smoke tests
- `docs/` - Architecture, logs, deployment plan, workflow examples, and screenshots

## Infrastructure Status

- Python virtual environment: configured and verified (`.venv`)
- PostgreSQL: running via Docker Compose (`postgres:16`)
- Environment configuration: `.env` and `.env.example` in place
- Dependency management: `requirements.txt` and `requirements-dev.txt`
- Build tooling: `Makefile` with standard commands
- Containerization baseline: `Dockerfile` and `docker-compose.yml`


