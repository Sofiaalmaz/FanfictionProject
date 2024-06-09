import os

import pandas as pd


def prepare_data_part1(df_part1: pd.DataFrame) -> pd.DataFrame:
    df_part1 = df_part1.copy()
    df_part1.drop(columns=["Updated", "published_mmyy"], inplace=True)
    df_part1["Words"] = df_part1["Words"].astype(str).str.replace(",", "")
    df_part1["Favs"] = pd.to_numeric(df_part1["Favs"], errors="coerce")
    df_part1["Follows"] = pd.to_numeric(df_part1["Follows"], errors="coerce")
    df_part1["Reviews"] = pd.to_numeric(df_part1["Reviews"], errors="coerce")
    df_part1["Words"] = pd.to_numeric(df_part1["Words"], errors="coerce")
    df_part1["Favs"] = df_part1["Favs"].fillna(0)
    df_part1["Follows"] = df_part1["Follows"].fillna(0)
    df_part1["Reviews"] = df_part1["Reviews"].fillna(0)
    df_part1["Words"] = df_part1["Words"].fillna(0)
    df_part1["Published"] = pd.to_datetime(df_part1["Published"])
    return df_part1


def prepare_data_part2(df_part2: pd.DataFrame) -> pd.DataFrame:
    df_part2 = df_part2.copy()
    df_part2.drop(columns=["author_link", "updated"], inplace=True)
    df_part2["favs"] = df_part2["favs"].fillna(0)
    df_part2["follows"] = df_part2["follows"].fillna(0)
    df_part2["reviews"] = df_part2["reviews"].fillna(0)
    df_part2["words"] = df_part2["words"].fillna(0)
    df_part2["characters"] = df_part2["characters"].apply(str).fillna("")
    df_part2["published"] = pd.to_datetime(df_part2["published"])
    df_part2.rename(
        columns={
            "link": "story_link",
            "summary": "synopsis",
            "rated": "rating",
            "reviews": "Reviews",
            "chapters": "Chapters",
            "favs": "Favs",
            "follows": "Follows",
            "published": "Published",
            "words": "Words",
        },
        inplace=True,
    )
    df_part2.sort_values(by="Published", inplace=True)
    return df_part2


def read_data_part1(data_dir: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join(data_dir, "hpcleanvlarge1.csv"))


def read_data_part2(data_dir: str) -> pd.DataFrame:
    return pd.read_csv(os.path.join(data_dir, "fanfiction_data.csv"))


def create_union_data(df_part1: pd.DataFrame, df_part2: pd.DataFrame) -> pd.DataFrame:
    df_part2_prepared = df_part2[df_part1.columns]
    df = pd.concat([df_part1, df_part2_prepared])
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=["author", "title", "language", "Published"], keep="last", inplace=False)
