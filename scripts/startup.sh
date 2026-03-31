#!/bin/bash
set -e

echo "Waiting for database..."
sleep 5

echo "Checking whether database is initialized..."
if PGPASSWORD="${POSTGRES_PASSWORD:-${DB_PASSWORD}}" psql \
    -h "${POSTGRES_HOST:-${DB_HOST:-postgres}}" \
    -p "${POSTGRES_PORT:-${DB_PORT:-5432}}" \
    -U "${POSTGRES_USER:-${DB_USER:-genomics_user}}" \
    -d "${POSTGRES_DB:-${DB_NAME:-genomics_portal}}" \
    -tAc "SELECT to_regclass('public.patients');" | grep -q patients; then
    echo "Database already initialized. Skipping schema init."
else
    echo "Initializing database..."
    python -m scripts.init_db
fi

echo "Ingesting samples..."
python -m scripts.ingest_samples

echo "Registering sequencing runs..."
python -m scripts.register_sequencing_run

echo "Registering pipeline runs..."
python -m scripts.register_pipeline_run

echo "Registering file assets..."
python -m scripts.register_file_assets

echo "Ingesting QC results..."
python -m scripts.ingest_qc_results

echo "Ingesting variant summaries..."
python -m scripts.ingest_variant_summaries

echo "Starting Streamlit..."
exec streamlit run streamlit_app/Home.py --server.port=8501 --server.address=0.0.0.0