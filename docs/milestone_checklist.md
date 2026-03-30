# Milestone Checklist

## Milestone 1 - Project foundation
- [x] Create project folder in working directory
- [x] Initialize Git repository
- [x] Open repo in VS Code
- [x] Create Python virtual environment
- [x] Resolve macOS Python environment issue and standardize interpreter
- [x] Install initial runtime and dev dependencies
- [x] Create repository skeleton
- [x] Add root configuration files
- [x] Add Docker Compose PostgreSQL setup
- [x] Start and verify PostgreSQL container health
- [x] Add initial documentation and tracking logs

## Milestone 2 - Database foundation
- [x] Implement SQL schema
- [x] Add constraints and indexes
- [x] Seed controlled vocabularies and reference data
- [ ] Add SQL views and reporting queries

## Milestone 3 - Python data layer
- [x] Implement config and environment-driven settings
- [x] Implement SQLAlchemy engine and session management
- [x] Implement ORM models aligned to schema
- [x] Add database smoke test and verify connectivity
- [x] Implement validation service layer
- [ ] Implement repository/query layer

## Milestone 4 - Synthetic data and ingestion
- [x] Build synthetic data generator
- [x] Generate realistic manifests and raw data artifacts
- [x] Implement ingestion scripts for samples, runs, QC, variants, and files
- [x] Register provenance relationships (tools, references, parameters)

## Milestone 5 - Query and UI layer
- [~] Implement repository/query layer - sample-centric repository and smoke test added; additional run/QC/dashboard-oriented repositories may still follow
- [x] Implement Streamlit pages (Sample Explorer, Run Explorer, QC Dashboard, Variant Search, Provenance Trace)
- [ ] Add data dictionary and provenance trace workflows

## Milestone 6 - Quality and deployment
- [~] Add tests and smoke checks - initial smoke tests for DB connectivity and repository workflows implemented
- [ ] Add full stack containerization
- [ ] Finalize documentation and screenshots
- [ ] Prepare portfolio summary and resume bullets