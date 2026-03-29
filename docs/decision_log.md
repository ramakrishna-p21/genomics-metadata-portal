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


