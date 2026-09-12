import os
import re
from datetime import datetime


# --------------------------------------------------
# TEXT CLEANING
# --------------------------------------------------

def clean_text(text):

    if not text:

        return ""

    text = str(text)

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# --------------------------------------------------
# WORD COUNT
# --------------------------------------------------

def count_words(text):

    if not text:

        return 0

    return len(
        text.split()
    )


# --------------------------------------------------
# FILE EXTENSION
# --------------------------------------------------

def get_file_extension(
    file_name
):

    return os.path.splitext(
        file_name
    )[1].lower()


# --------------------------------------------------
# CURRENT DATE AND TIME
# --------------------------------------------------

def get_current_datetime():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# --------------------------------------------------
# SCORE LABEL
# --------------------------------------------------

def get_score_label(score):

    if score >= 85:

        return "Excellent"

    elif score >= 70:

        return "Good"

    elif score >= 50:

        return "Average"

    else:

        return "Needs Improvement"


# --------------------------------------------------
# SCORE COLOR MESSAGE
# --------------------------------------------------

def get_score_message(score):

    if score >= 85:

        return (
            "Excellent performance! "
            "Keep practicing at this level."
        )

    elif score >= 70:

        return (
            "Good performance. "
            "A little more practice will help."
        )

    elif score >= 50:

        return (
            "Average performance. "
            "Focus on your weak areas."
        )

    else:

        return (
            "More preparation is required. "
            "Review the concepts and try again."
        )