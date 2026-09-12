# 

import pandas as pd


def get_difficulties(df):
    """
    Return the unique difficulty levels available
    in the dataset.
    """

    if df.empty:
        return []

    difficulties = (
        df["Difficulty"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    return sorted(difficulties)


def filter_by_difficulty(df, difficulty):
    """
    Filter the dataset based on difficulty level.
    """

    # Return all questions
    if difficulty == "All Levels":
        return df

    # Filter selected difficulty
    filtered_df = df[
        df["Difficulty"].str.lower()
        == difficulty.lower()
    ]

    return filtered_df.reset_index(drop=True)