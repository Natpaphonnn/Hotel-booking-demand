"""Data cleaning functions for Hotel Booking Demand dataset."""

import pandas as pd
import numpy as np
from src.config import MONTH_TO_NUM


def load_raw_data(path: str = "../hotel_bookings.csv") -> pd.DataFrame:
    """Load the raw hotel bookings CSV."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all cleaning steps and return a clean DataFrame."""
    df = df.copy()

    # 1. Handle NULL string values (dataset uses "NULL" as string)
    df["children"] = df["children"].fillna(0).astype(int)
    df["agent"] = df["agent"].replace("NULL", np.nan).astype(float)
    df["company"] = df["company"].replace("NULL", np.nan).astype(float)
    df["country"] = df["country"].replace("NULL", "Unknown")

    # 2. Convert meal "Undefined" to "SC" (Self Catering / no meal)
    df["meal"] = df["meal"].replace("Undefined", "SC")

    # 3. Convert arrival_date_month to numeric
    df["arrival_date_month_num"] = df["arrival_date_month"].map(MONTH_TO_NUM)

    # 4. Create arrival_date (datetime)
    df["arrival_date"] = pd.to_datetime(
        df["arrival_date_year"].astype(str) + "-"
        + df["arrival_date_month_num"].astype(str).str.zfill(2) + "-"
        + df["arrival_date_day_of_month"].astype(str).str.zfill(2),
        errors="coerce"
    )

    # 5. Filter abnormal ADR
    df = df[(df["adr"] >= 0) & (df["adr"] <= 5000)].copy()

    # 6. Fix data types
    df["is_canceled"] = df["is_canceled"].astype(int)
    df["is_repeated_guest"] = df["is_repeated_guest"].astype(int)
    df["adults"] = df["adults"].astype(int)
    df["babies"] = df["babies"].fillna(0).astype(int)

    # 7. Convert reservation_status_date to datetime
    df["reservation_status_date"] = pd.to_datetime(
        df["reservation_status_date"], errors="coerce"
    )

    df = df.reset_index(drop=True)
    return df


def get_data_summary(df: pd.DataFrame) -> dict:
    """Return a summary dict of the cleaned dataset."""
    return {
        "shape": df.shape,
        "missing_pct": (df.isnull().sum() / len(df) * 100).round(2),
        "dtypes": df.dtypes,
        "canceled_pct": df["is_canceled"].mean() * 100,
    }
