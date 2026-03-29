import json
from pathlib import Path

import pandas as pd


def read_tsv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path, sep="\t")


def read_json_records(path: str | Path) -> pd.DataFrame:
    with open(path, encoding="utf-8") as handle:
        payload = json.load(handle)

    if isinstance(payload, list):
        return pd.DataFrame(payload)

    if isinstance(payload, dict):
        return pd.DataFrame([payload])

    raise ValueError(f"Unsupported JSON structure in {path}")