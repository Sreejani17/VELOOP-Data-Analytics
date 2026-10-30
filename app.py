
from pathlib import Path

import pandas as pd
import streamlit as st

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "sample"

st.set_page_config(
    page_title="VELOOP Rewards Analytics",
    page_icon="📊",
    layout="wide"
)


@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)


st.title("VELOOP Rewards – Analytics Dashboard")
st.caption("Product Analytics | Data Quality | Rewards Insights")

st.info(
    "DEMO NOTICE: This dashboard uses synthetic sample data "
    "created for analytical testing. It does not represent "
    "actual VELOOP production performance."
)

# Find available CSV files
csv_files = sorted(DATA_DIR.glob("*.csv"))

if not csv_files:
    st.error("No CSV datasets found in data/sample.")
    st.stop()

# Sidebar
st.sidebar.header("Dashboard Controls")

selected_file = st.sidebar.selectbox(
    "Select a dataset",
    csv_files,
    format_func=lambda path: path.stem.replace("_", " ")
)

df = load_data(selected_file)

# Calculate data quality information
total_rows = len(df)
total_columns = len(df.columns)
missing_cells = int(df.isna().sum().sum())
duplicate_rows = int(df.duplicated().sum())
total_cells = total_rows * total_columns

missing_percentage = (
    (missing_cells / total_cells) * 100
    if total_cells else 0
)

# Main metrics
st.subheader(f"{selected_file.stem.replace('_', ' ')} Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", f"{total_rows:,}")
col2.metric("Total Columns", f"{total_columns:,}")
col3.metric("Missing Cells", f"{missing_cells:,}")
col4.metric("Duplicate Rows", f"{duplicate_rows:,}")

st.divider()

overview_tab, explorer_tab, quality_tab = st.tabs(
    ["📊 Overview", "🔎 Data Explorer", "✅ Data Quality"]
)

with overview_tab:
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Missing Values by Column")

    missing_by_column = df.isna().sum()
    missing_by_column = missing_by_column[
        missing_by_column > 0
    ].sort_values(ascending=False)

    if not missing_by_column.empty:
        st.bar_chart(missing_by_column)
    else:
        st.success("No missing values found in this dataset.")

    # Show a categorical distribution
    categorical_columns = [
        col for col in df.columns
        if 1 < df[col].nunique(dropna=True) <= 30
    ]

    if categorical_columns:
        st.subheader("Category Distribution")

        selected_column = st.selectbox(
            "Choose a column",
            categorical_columns
        )

        category_counts = (
            df[selected_column]
            .fillna("Missing")
            .astype(str)
            .value_counts()
            .head(10)
        )

        st.bar_chart(category_counts)

with explorer_tab:
    st.subheader("Explore Dataset")

    selected_columns = st.multiselect(
        "Choose columns to display",
        options=list(df.columns),
        default=list(df.columns)
    )

    if selected_columns:
        st.dataframe(
            df[selected_columns],
            use_container_width=True
        )
    else:
        st.warning("Select at least one column.")

    st.download_button(
        label="Download Selected Dataset as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"{selected_file.stem}_export.csv",
        mime="text/csv"
    )

with quality_tab:
    st.subheader("Data Quality Summary")

    quality_metrics = pd.DataFrame({
        "Metric": [
            "Total records",
            "Total columns",
            "Missing cells",
            "Missing percentage",
            "Duplicate rows"
        ],
        "Value": [
            total_rows,
            total_columns,
            missing_cells,
            f"{missing_percentage:.2f}%",
            duplicate_rows
        ]
    })

    st.dataframe(quality_metrics, use_container_width=True)

    st.subheader("Missing Values by Field")

    missing_report = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": df.isna().sum().values,
        "Missing Percentage": (
            df.isna().mean().values * 100
        ).round(2)
    })

    st.dataframe(
        missing_report.sort_values(
            "Missing Count",
            ascending=False
        ),
        use_container_width=True
    )

    st.subheader("Duplicate Records")

    if duplicate_rows:
        st.warning(
            f"{duplicate_rows} duplicate rows detected."
        )
        st.dataframe(
            df[df.duplicated(keep=False)],
            use_container_width=True
        )
    else:
        st.success("No duplicate rows detected.")

st.divider()

st.caption(
    "VELOOP Rewards Analytics | Internship Project Demo"
)
