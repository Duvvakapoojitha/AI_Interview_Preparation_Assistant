import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.data_processing.clean_data import (
    load_dataset
)

from src.data_processing.feature_extraction import (
    extract_text_features,
    extract_keyword_features,
    get_dataset_statistics
)

from src.resume.skill_extractor import (
    extract_skills,
    match_skills_with_dataset
)


# --------------------------------------------------
# TEST DATASET
# --------------------------------------------------

def test_dataset_loading():

    df = load_dataset()

    assert df is not None

    assert len(df) > 0


# --------------------------------------------------
# TEST DATASET COLUMNS
# --------------------------------------------------

def test_dataset_columns():

    df = load_dataset()

    required_columns = [

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

    for column in required_columns:

        assert column in df.columns


# --------------------------------------------------
# TEST TEXT FEATURES
# --------------------------------------------------

def test_text_features():

    text = """
    Java is an object-oriented programming
    language.
    """

    result = extract_text_features(text)

    assert result["word_count"] > 0

    assert result["sentence_count"] > 0

    assert result["character_count"] > 0


# --------------------------------------------------
# TEST KEYWORD FEATURES
# --------------------------------------------------

def test_keyword_features():

    answer = """
    Java supports inheritance and polymorphism.
    """

    keywords = (
        "java, inheritance, polymorphism, abstraction"
    )

    result = extract_keyword_features(
        answer,
        keywords
    )

    assert result["total_keywords"] == 4

    assert result["matched_keywords"] == 3

    assert "abstraction" in result["missing"]


# --------------------------------------------------
# TEST RESUME SKILL EXTRACTION
# --------------------------------------------------

def test_skill_extraction():

    resume = """
    Skills:
    Java, Python, Spring Boot, MySQL,
    Machine Learning and Docker.
    """

    skills = extract_skills(resume)

    assert "java" in skills

    assert "python" in skills

    assert "spring boot" in skills

    assert "mysql" in skills

    assert "machine learning" in skills

    assert "docker" in skills


# --------------------------------------------------
# TEST DATASET STATISTICS
# --------------------------------------------------

def test_dataset_statistics():

    df = load_dataset()

    statistics = get_dataset_statistics(df)

    assert "total_questions" in statistics

    assert statistics[
        "total_questions"
    ] > 0


# --------------------------------------------------
# TEST RESUME + DATASET MATCHING
# --------------------------------------------------

def test_resume_dataset_matching():

    df = load_dataset()

    resume_skills = [
        "java",
        "python"
    ]

    result = match_skills_with_dataset(
        resume_skills,
        df
    )

    # It is acceptable if no matching
    # questions exist in a tiny test dataset.
    assert result is not None