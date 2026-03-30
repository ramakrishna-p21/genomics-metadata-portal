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

## 2026-02-23 - Python database layer implemented
- Added environment-driven application settings using Pydantic settings.
- Implemented SQLAlchemy engine, session factory, and declarative base.
- Added structured application logging configuration.
- Implemented SQLAlchemy ORM models aligned to the PostgreSQL schema.
- Added Python-based database smoke test to validate connectivity and seeded master data access.
- Resolved Python module import issue by standardizing on module-style script execution from repository root.
- Added `scripts/__init__.py` and VS Code workspace settings to improve local interpreter and import resolution.

## 2026-02-24 - Synthetic data generation implemented
- Added shared enum definitions, ID generators, and date utilities for controlled synthetic record creation.
- Implemented synthetic data generator for patients, batches, samples, sequencing runs, pipeline runs, QC results, variant summaries, file assets, analysis summaries, and audit events.
- Generated realistic raw manifests and example files aligned to the production schema and ingestion plan.
- Introduced operational realism including reruns, failed runs, WARN/FAIL QC cases, outdated pipeline version usage, high-TMB cases, and KRAS-mutated samples.
- Standardized the local runtime on Homebrew Python 3.11 to support the intended project feature set and reproducible script execution.
- Verified generated artifact structure and manifest summary from the local filesystem.

## 2026-02-25 - Initial ingestion layer implemented
- Added reusable validation service for manifest structure, required fields, uniqueness, and controlled-value checks.
- Implemented sample ingest service for patients, batches, and samples.
- Added Python ingestion script for loading sample metadata manifests into PostgreSQL through the ORM/session layer.
- Verified loaded record counts and patient-sample joins in PostgreSQL after ingestion.
- Confirmed idempotent rerun behavior by re-executing sample ingestion without creating duplicate records.

## 2026-02-26 - Sequencing run registration implemented
- Added sequencing run registration service for loading sequencing runs and sample-run assignment manifests.
- Validated run metadata, allowed statuses/platforms, and foreign-key compatibility with previously loaded samples.
- Loaded sequencing run records and sample-to-run assignments into PostgreSQL.
- Verified sequencing lineage joins and confirmed idempotent rerun behavior for sequencing registration.