"""Feature engineering functions for Hotel Booking Demand dataset."""

import pandas as pd
import numpy as np
from src.config import HIGH_SEASON_MONTHS, MID_SEASON_MONTHS, LEAD_TIME_BINS, LEAD_TIME_LABELS


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add all engineered features to the DataFrame."""
    df = df.copy()

    # Total nights stayed
    df["total_nights"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]

    # Revenue metrics
    df["total_revenue"] = df["adr"] * df["total_nights"]
    df["revenue_lost"] = np.where(df["is_canceled"] == 1, df["total_revenue"], 0)

    # Room upgrade flag
    df["is_room_upgraded"] = (df["reserved_room_type"] != df["assigned_room_type"]).astype(int)

    # Total guests
    df["total_guests"] = df["adults"] + df["children"] + df["babies"]

    # Lead time buckets
    df["booking_window"] = pd.cut(
        df["lead_time"],
        bins=LEAD_TIME_BINS,
        labels=LEAD_TIME_LABELS,
        include_lowest=True,
    )

    # Season
    month_num = df["arrival_date_month_num"]
    df["season"] = np.select(
        [month_num.isin(HIGH_SEASON_MONTHS), month_num.isin(MID_SEASON_MONTHS)],
        ["High", "Mid"],
        default="Low",
    )
    df["is_high_season"] = month_num.isin(HIGH_SEASON_MONTHS).astype(int)

    # Price per person (avoid division by zero)
    df["price_per_person"] = np.where(
        df["total_guests"] > 0,
        df["adr"] / df["total_guests"],
        df["adr"],
    )

    # Engagement signals
    df["has_special_requests"] = (df["total_of_special_requests"] > 0).astype(int)
    df["is_family"] = ((df["children"] > 0) | (df["babies"] > 0)).astype(int)

    # Interaction features
    df["lead_time_squared"] = df["lead_time"] ** 2  # non-linear lead time effect
    df["adr_per_person"] = np.where(df["total_guests"] > 0, df["adr"] / df["total_guests"], df["adr"])
    df["stays_ratio"] = np.where(df["total_nights"] > 0, df["stays_in_weekend_nights"] / df["total_nights"], 0)  # weekend proportion
    df["is_long_stay"] = (df["total_nights"] >= 7).astype(int)

    # Agent/company presence flags (NaN already replaced with NaN floats in cleaning;
    # after fillna(0) in modeling these become 0.0, so check for non-zero and non-NaN)
    df["has_company"] = (df["company"].notna() & (df["company"] != 0)).astype(int)
    df["has_agent"] = (df["agent"].notna() & (df["agent"] != 0)).astype(int)

    # Booking behavior signals
    df["booking_changes_flag"] = (df["booking_changes"] > 0).astype(int)
    df["waiting_list_flag"] = (df["days_in_waiting_list"] > 0).astype(int)

    # Historical booking patterns
    df["net_previous_bookings"] = df["previous_bookings_not_canceled"] - df["previous_cancellations"]
    df["cancel_history_ratio"] = np.where(
        (df["previous_cancellations"] + df["previous_bookings_not_canceled"]) > 0,
        df["previous_cancellations"] / (df["previous_cancellations"] + df["previous_bookings_not_canceled"]),
        0
    )

    return df
