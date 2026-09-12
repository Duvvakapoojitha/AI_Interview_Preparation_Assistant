import re
from collections import Counter


# --------------------------------------------------
# TEXT FEATURES
# --------------------------------------------------

def extract_text_features(text):
    """
    Extract basic features from a text answer.
    """

    if not text:
        return {
            "word_count": 0,
            "sentence_count": 0,
            "character_count": 0,
            "average_word_length": 0
        }

    text = str(text).strip()

    # Words
    words = re.findall(r"\b\w+\b", text)

    # Sentences
    sentences = re.split(r"[.!?]+", text)
    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    word_count = len(words)
    sentence_count = len(sentences)
    character_count = len(text)

    if word_count > 0:
        average_word_length = (
            sum(len(word) for word in words)
            / word_count
        )
    else:
        average_word_length = 0

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "character_count": character_count,
        "average_word_length": round(
            average_word_length, 2
        )
    }


# --------------------------------------------------
# KEYWORD FEATURES
# --------------------------------------------------

def extract_keyword_features(answer, keywords):
    """
    Check how many expected keywords
    appear in the candidate's answer.
    """

    if not answer:
        answer = ""

    answer = answer.lower()

    if not keywords:
        return {
            "total_keywords": 0,
            "matched_keywords": 0,
            "keyword_match_percentage": 0,
            "matched": [],
            "missing": []
        }

    keyword_list = [
        keyword.strip().lower()
        for keyword in str(keywords).split(",")
        if keyword.strip()
    ]

    matched = []
    missing = []

    for keyword in keyword_list:

        if keyword in answer:
            matched.append(keyword)
        else:
            missing.append(keyword)

    total = len(keyword_list)
    matched_count = len(matched)

    if total > 0:
        percentage = (
            matched_count / total
        ) * 100
    else:
        percentage = 0

    return {
        "total_keywords": total,
        "matched_keywords": matched_count,
        "keyword_match_percentage": round(
            percentage, 2
        ),
        "matched": matched,
        "missing": missing
    }


# --------------------------------------------------
# ANSWER FEATURES
# --------------------------------------------------

def extract_answer_features(
    answer,
    expected_answer,
    keywords
):
    """
    Combine all useful answer features.
    """

    text_features = extract_text_features(
        answer
    )

    keyword_features = extract_keyword_features(
        answer,
        keywords
    )

    return {
        **text_features,
        **keyword_features,
        "has_expected_answer": bool(
            expected_answer
        )
    }


# --------------------------------------------------
# DATASET STATISTICS
# --------------------------------------------------

def get_dataset_statistics(df):
    """
    Generate useful statistics from
    the interview dataset.
    """

    statistics = {}

    statistics["total_questions"] = len(df)

    if "Company" in df.columns:
        statistics["companies"] = (
            df["Company"]
            .nunique()
        )

    if "Industry" in df.columns:
        statistics["industries"] = (
            df["Industry"]
            .nunique()
        )

    if "Role" in df.columns:
        statistics["roles"] = (
            df["Role"]
            .nunique()
        )

    if "Difficulty" in df.columns:
        statistics["difficulties"] = (
            df["Difficulty"]
            .nunique()
        )

    if "Round" in df.columns:
        statistics["rounds"] = (
            df["Round"]
            .nunique()
        )

    return statistics