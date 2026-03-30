# Decision Log

## 2026-02-20 - Local development model
- Decision: Use Python virtual environment for local app development on Mac and Docker Compose for PostgreSQL first.
- Rationale: Faster iteration for Python/Streamlit while keeping database environment consistent and cloud-aligned.
- Consequence: The app remains easy to run locally during development, while the database behaves like a managed external dependency.

## 2026-02-20 - PostgreSQL-first containerization
- Decision: Start with PostgreSQL-only Docker Compose and add full app containerization later.
- Rationale: Matches implementation priorities and reduces early debugging complexity.
- Consequence: Database can be validated independently before introducing full-stack container orchestration.

## 2026-02-20 - Python runtime standardization
- Decision: Use Homebrew Python instead of macOS system Python.
- Rationale: Ensures stable virtual environments and compatibility with modern Python tooling.
- Consequence: Prevents environment inconsistencies and improves reproducibility.

## 2026-02-21 - Python interpreter standardization enforcement
- Decision: Explicitly require Homebrew Python for local development instead of system Python.
- Rationale: macOS system Python can produce incomplete virtual environments and inconsistent dependency behavior.
- Consequence: Slight setup overhead, but significantly improved stability and reproducibility.

## 2026-02-21 - Early infrastructure validation
- Decision: Validate PostgreSQL container health and connectivity before implementing schema.
- Rationale: Prevents misattributing future schema or ingestion issues to infrastructure problems.
- Consequence: Cleaner debugging boundaries during database and service layer implementation.

## 2026-02-22 - Controlled vocabularies enforced with database checks
- Decision: Enforce key controlled vocabularies using PostgreSQL CHECK constraints rather than separate lookup tables in the first implementation.
- Rationale: Keeps the schema readable, strongly validated, and easier to demonstrate in a portfolio project while preserving operational realism.
- Consequence: Vocabulary expansion requires schema edits, but the design remains clear and robust for the intended scope.

## 2026-02-22 - Provenance modeled as explicit relational links
- Decision: Represent run-level tools and references with dedicated association tables (`pipeline_run_tools`, `pipeline_run_references`).
- Rationale: Supports precise provenance tracing and avoids burying critical lineage data inside JSON blobs.
- Consequence: More joins are required, but traceability and analytical value are much stronger.

## 2026-02-22 - Non-interactive SQL execution in Docker Compose
- Decision: Use `docker compose exec -T` when executing SQL files through stdin redirection on macOS.
- Rationale: Prevents TTY allocation errors during scripted PostgreSQL execution.
- Consequence: Local database initialization commands are more robust and reproducible.

## 2026-02-23 - Centralized configuration and session management
- Decision: Use a shared settings module and centralized SQLAlchemy session factory for all application components.
- Rationale: Prevents duplicated connection logic and supports clean reuse across scripts, repositories, tests, and UI pages.
- Consequence: Configuration becomes easier to manage and the codebase remains more maintainable as features expand.

## 2026-02-23 - ORM models aligned to existing SQL-first schema
- Decision: Build SQLAlchemy models against the already-implemented PostgreSQL schema rather than generating schema from ORM first.
- Rationale: The project is intentionally database-first to emphasize SQL design, integrity rules, and provenance-aware relational modeling.
- Consequence: SQL remains the primary schema contract, while Python models serve as an application access layer.

## 2026-02-23 - Module-style script execution
- Decision: Run project scripts using `python -m ...` from the repository root instead of direct file execution.
- Rationale: Ensures the repo root is on the Python import path and avoids fragile import behavior.
- Consequence: Script execution is more consistent across local development, testing, and future CI environments.

## 2026-02-24 - File-first synthetic data workflow
- Decision: Generate synthetic manifests and output-like files under `data/raw/` before implementing DB ingestion.
- Rationale: Mirrors real bioinformatics operations where systems ingest pipeline outputs and metadata artifacts rather than creating records directly in the database.
- Consequence: Ingestion scripts can be designed and tested against realistic source artifacts.

## 2026-02-24 - Deterministic synthetic data generation
- Decision: Use a fixed random seed for synthetic data generation.
- Rationale: Keeps development, testing, screenshots, and demonstrations reproducible across runs.
- Consequence: Generated datasets are stable unless the generator logic is intentionally changed.

## 2026-02-24 - Pin local development runtime to Python 3.11
- Decision: Standardize local development on Homebrew Python 3.11 instead of the newest available Python release.
- Rationale: Python 3.11 is modern, actively supported, broadly compatible with current libraries, and stable for portfolio development.
- Consequence: Reduces risk of version-edge compatibility issues while keeping the project on a current supported runtime.

## 2026-02-25 - Validation before ORM insertion
- Decision: Validate required columns, uniqueness, non-null rules, and controlled values before inserting manifests into the database.
- Rationale: Failing fast at the manifest layer produces cleaner debugging and prevents avoidable database integrity errors.
- Consequence: Ingestion scripts become more reliable and easier to reason about.

## 2026-02-25 - Idempotent primary-key-based ingest behavior
- Decision: Skip records whose primary keys already exist during initial ingestion scripts.
- Rationale: Allows safe local reruns during development without creating duplicates.
- Consequence: Current behavior favors insert-if-missing rather than full synchronization logic, which is sufficient for this project stage.