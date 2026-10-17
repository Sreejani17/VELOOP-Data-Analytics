
from pathlib import Path
import pandas as pd

# Project root is the parent of the src folder.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Update this filename to match your downloaded workbook.
FILE_PATH = DATA_DIR / "VELOOP_Data.xlsx"

if not FILE_PATH.exists():
    raise FileNotFoundError(
        f"Workbook not found: {FILE_PATH}\n"
        "Place the supplied Excel workbook in the data folder "
        "and update FILE_PATH if needed."
    )

sheets = pd.read_excel(FILE_PATH, sheet_name=None)

inventory = []
quality_rows = []

for sheet_name, df in sheets.items():
    print(f"\n--- {sheet_name} ---")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("Column names:", list(df.columns))
    print("Duplicate rows:", int(df.duplicated().sum()))

    # Summary of missing values by column.
    missing = df.isna().sum()
    print("Missing values:")
    print(missing[missing > 0].to_dict())

    # Create an initial inventory.
    date_columns = [
        col for col in df.columns
        if any(word in str(col).lower()
               for word in ["date", "time", "timestamp"])
    ]

    date_range = "Not identified"
    for col in date_columns:
        parsed = pd.to_datetime(df[col], errors="coerce")
        valid = parsed.dropna()
        if not valid.empty:
            date_range = (
                f"{valid.min()} to {valid.max()}"
            )
            break

    inventory.append({
        "dataset": sheet_name,
        "records": len(df),
        "columns": len(df.columns),
        "date_range": date_range,
        "duplicate_rows": int(df.duplicated().sum()),
        "total_missing_cells": int(df.isna().sum().sum()),
    })

    for col in df.columns:
        count = int(df[col].isna().sum())
        if count:
            quality_rows.append({
                "dataset": sheet_name,
                "field": col,
                "issue_type": "Missing values",
                "records_affected": count,
                "status": "Needs investigation",
            })

pd.DataFrame(inventory).to_csv(
    OUTPUT_DIR / "initial_data_inventory.csv",
    index=False
)

pd.DataFrame(quality_rows).to_csv(
    OUTPUT_DIR / "initial_missing_values_report.csv",
    index=False
)

print("\nInitial profiling complete.")
print("Reports saved in:", OUTPUT_DIR)
