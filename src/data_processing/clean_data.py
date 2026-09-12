import pandas as pd
import os


DATASET_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "dataset",
    "interview_dataset.csv"
)


# The public question dataset uses a compact, lowercase schema.  The rest of
# the application consumes this canonical schema, so keep the translation at
# the data-loading boundary rather than making every caller handle both forms.
CANONICAL_COLUMN_MAP = {
    "company": "Company",
    "category": "Industry",
    "role": "Role",
    "round": "Round",
    "question": "Question",
    "topic": "Keywords",
    "difficulty": "Difficulty",
}


def _add_derived_columns(df):
    """Supply evaluation fields absent from the compact source dataset."""

    topics = df["Keywords"].replace("", "the topic")

    if "Expected_Answer" not in df.columns:
        df["Expected_Answer"] = topics.map(
            lambda topic: (
                f"Explain {topic} clearly, describe a practical approach, "
                "and support it with relevant examples or trade-offs."
            )
        )

    if "Evaluation_Criteria" not in df.columns:
        df["Evaluation_Criteria"] = topics.map(
            lambda topic: (
                f"Clear understanding of {topic}; logical reasoning; "
                "practical examples; and awareness of trade-offs."
            )
        )

    if "Follow_Up_Question" not in df.columns:
        df["Follow_Up_Question"] = topics.map(
            lambda topic: f"Can you share a concrete example involving {topic}?"
        )

    return df


def load_dataset():
    """
    Load the interview dataset.
    """

    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(
            f"Dataset not found at: {DATASET_PATH}"
        )

    df = pd.read_csv(DATASET_PATH)

    # Normalize source column names to the schema used by the UI, NLP modules,
    # and tests.  Existing canonical columns are left untouched.
    rename_map = {
        source: target
        for source, target in CANONICAL_COLUMN_MAP.items()
        if source in df.columns and target not in df.columns
    }
    df = df.rename(columns=rename_map)

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Fill missing values
    df = df.fillna("")

    # Remove unwanted spaces
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].astype(str).str.strip()

    return _add_derived_columns(df)


if __name__ == "__main__":
    data = load_dataset()

    print("Dataset loaded successfully")
    print("Number of rows:", len(data))
    print("Columns:", list(data.columns))
