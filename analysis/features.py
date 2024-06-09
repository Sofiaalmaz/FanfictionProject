import re
from typing import Optional

import pandas as pd


def extract_pairings(characters: str) -> Optional[str]:
    pairings = re.findall(r"\[(.*?)\]", characters)
    return ", ".join(pairings) if pairings else None


def add_pairings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["pairing"] = df["characters"].apply(extract_pairings)
    return df


def group_data_per_year(df: pd.DataFrame) -> pd.DataFrame:
    # Group by year and calculate the mean, median, and sum for 'favs', 'follows', and 'reviews'
    df = df.copy()
    df["Published"] = pd.to_datetime(df["Published"], errors="coerce")
    df["year"] = df["Published"].dt.year
    grouped = (
        df.groupby("year")
        .agg(
            {
                "Favs": ["mean", "median", "sum"],
                "Follows": ["mean", "median", "sum"],
                "Reviews": ["mean", "median", "sum"],
            }
        )
        .reset_index()
    )

    # Flatten the multi-level columns
    grouped.columns = [
        "year",
        "favs_mean",
        "favs_median",
        "favs_sum",
        "follows_mean",
        "follows_median",
        "follows_sum",
        "reviews_mean",
        "reviews_median",
        "reviews_sum",
    ]
    return grouped
