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
