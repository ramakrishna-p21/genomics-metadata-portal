# Build Log

## 2026-02-20 - Project initialization
- Created repository root structure for Genomics Metadata, Provenance & Analysis Portal.
- Initialized Git repository on main branch.
- Created Python virtual environment for local Mac development.
- Installed initial Python dependencies for PostgreSQL, SQLAlchemy, Streamlit, testing, linting, and synthetic data generation.
- Added project skeleton directories and starter files.
- Added Docker Compose configuration for local PostgreSQL.
- Added root config files: `.gitignore`, `.dockerignore`, `.env.example`, `pyproject.toml`, `requirements.txt`, `requirements-dev.txt`, `Makefile`, and `Dockerfile`.

## 2026-02-21 - Environment stabilization and infrastructure verification
- Identified incomplete virtual environment caused by macOS system Python (CommandLineTools).
- Removed broken `.venv` and recreated environment using Homebrew-managed Python interpreter.
- Successfully activated virtual environment and verified interpreter isolation.
- Installed full project dependency set (runtime + dev tools).
- Created all root configuration files (`pyproject.toml`, `.gitignore`, `.dockerignore`, `.env`, `Makefile`, `Dockerfile`).
- Verified repository structure integrity using directory inspection.
- Started PostgreSQL container using Docker Compose and confirmed healthy status.
- Validated database connectivity using `psql` inside container.
- Confirmed clean Git working tree after initial commit.

## 2026-02-22 - Core relational schema implemented
- Implemented normalized PostgreSQL schema covering patients, samples, sequencing runs, pipelines, provenance, QC, variant summaries, file assets, and audit events.
- Added foreign key relationships, integrity constraints, controlled vocabulary checks, and analytical indexes.
- Seeded core reference/master data for pipelines, pipeline versions, references, tools, and QC metric definitions.
- Verified table creation and seed counts directly in PostgreSQL container.
- Resolved Docker Compose stdin execution issue on macOS by using non-TTY SQL execution with `docker compose exec -T`.