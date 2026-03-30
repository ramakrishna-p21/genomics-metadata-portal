import subprocess
from pathlib import Path

from app.logging_config import configure_logging, get_logger

configure_logging()
logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
SQL_DIR = BASE_DIR / "sql"


def run_sql_file(sql_file: Path) -> None:
    logger.info("Applying SQL file: %s", sql_file.name)

    command = [
        "docker",
        "compose",
        "exec",
        "-T",
        "postgres",
        "psql",
        "-U",
        "genomics_user",
        "-d",
        "genomics_portal",
        "-f",
        "/dev/stdin",
    ]

    with sql_file.open("rb") as handle:
        result = subprocess.run(command, stdin=handle, cwd=BASE_DIR, check=False)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to apply {sql_file.name}")

    logger.info("Applied SQL file successfully: %s", sql_file.name)


def main() -> None:
    logger.info("Initializing database from SQL files")

    for sql_name in [
        "001_schema.sql",
        "002_constraints_indexes.sql",
        "003_seed_reference_data.sql",
    ]:
        run_sql_file(SQL_DIR / sql_name)

    logger.info("Database initialization complete")


if __name__ == "__main__":
    main()
