import os


# --------------------------------------------------
# PROJECT CONFIGURATION
# --------------------------------------------------

PROJECT_NAME = (
    "AI Interview Preparation Assistant"
)


# --------------------------------------------------
# DATASET
# --------------------------------------------------

DATASET_PATH = os.path.join(
    "dataset",
    "interview_dataset.csv"
)


# --------------------------------------------------
# NLP MODEL
# --------------------------------------------------

SENTENCE_TRANSFORMER_MODEL = (
    "all-MiniLM-L6-v2"
)


# --------------------------------------------------
# RESUME
# --------------------------------------------------

SUPPORTED_RESUME_FORMATS = [
    ".pdf",
    ".docx"
]


# --------------------------------------------------
# SPEECH
# --------------------------------------------------

DEFAULT_SPEAKING_SPEED_MIN = 100

DEFAULT_SPEAKING_SPEED_MAX = 160


# --------------------------------------------------
# SCORE WEIGHTS
# --------------------------------------------------

SIMILARITY_WEIGHT = 0.60

KEYWORD_WEIGHT = 0.30

LENGTH_WEIGHT = 0.10


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

DATABASE_PATH = os.path.join(
    "database",
    "interview_history.db"
)