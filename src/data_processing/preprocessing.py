# import pandas as pd
# import os


# DATASET_PATH = os.path.join(
#     os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
#     "dataset",
#     "interview_dataset.csv"
# )


# def load_dataset():
#     """
#     Load the interview dataset.
#     """

#     if not os.path.exists(DATASET_PATH):
#         raise FileNotFoundError(
#             f"Dataset not found at: {DATASET_PATH}"
#         )

#     df = pd.read_csv(DATASET_PATH)

#     # Remove completely empty rows
#     df = df.dropna(how="all")

#     # Fill missing values
#     df = df.fillna("")

#     # Remove unwanted spaces
#     for column in df.columns:
#         if df[column].dtype == "object":
#             df[column] = df[column].astype(str).str.strip()

#     return df


# if __name__ == "__main__":
#     data = load_dataset()

#     print("Dataset loaded successfully")
#     print("Number of rows:", len(data))
#     print("Columns:", list(data.columns))\

import pandas as pd


def preprocess_dataset(df):
    """
    Convert the raw interview dataset into the format
    required by the AI Interview Preparation Assistant.
    """

    # --------------------------------------------------
    # RENAME EXISTING COLUMNS
    # --------------------------------------------------

    df = df.rename(columns={
        "company": "Company",
        "role": "Role",
        "round": "Round",
        "question": "Question",
        "difficulty": "Difficulty",
        "category": "Industry"
    })


    # --------------------------------------------------
    # CREATE MISSING COLUMNS
    # --------------------------------------------------

    if "Expected_Answer" not in df.columns:
        df["Expected_Answer"] = ""

    if "Keywords" not in df.columns:
        df["Keywords"] = ""

    if "Evaluation_Criteria" not in df.columns:
        df["Evaluation_Criteria"] = ""

    if "Follow_Up_Question" not in df.columns:
        df["Follow_Up_Question"] = ""


    # --------------------------------------------------
    # CLEAN TEXT COLUMNS
    # --------------------------------------------------

    text_columns = [
        "Company",
        "Industry",
        "Role",
        "Round",
        "Question",
        "Expected_Answer",
        "Keywords",
        "Difficulty",
        "Evaluation_Criteria",
        "Follow_Up_Question"
    ]

    for column in text_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .fillna("")
                .astype(str)
                .str.strip()
            )


    # --------------------------------------------------
    # REMOVE EMPTY QUESTIONS
    # --------------------------------------------------

    df = df[
        df["Question"].str.strip() != ""
    ]


    # --------------------------------------------------
    # RESET INDEX
    # --------------------------------------------------

    df = df.reset_index(drop=True)


    return df