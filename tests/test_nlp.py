import sys
import os

# Add project root to Python path
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.nlp.keyword_extractor import (
    extract_keywords,
    find_matching_keywords
)

from src.nlp.feedback_generator import (
    generate_feedback
)


# --------------------------------------------------
# TEST KEYWORD EXTRACTION
# --------------------------------------------------

def test_extract_keywords():

    keywords = "java, inheritance, polymorphism"

    result = extract_keywords(keywords)

    assert "java" in result
    assert "inheritance" in result
    assert "polymorphism" in result


# --------------------------------------------------
# TEST KEYWORD MATCHING
# --------------------------------------------------

def test_keyword_matching():

    answer = """
    In Java, inheritance allows a subclass
    to acquire properties and methods from
    a superclass.
    """

    keywords = [
        "inheritance",
        "subclass",
        "superclass",
        "polymorphism"
    ]

    matched, missing = find_matching_keywords(
        answer,
        keywords
    )

    assert "inheritance" in matched
    assert "subclass" in matched
    assert "superclass" in matched
    assert "polymorphism" in missing


# --------------------------------------------------
# TEST FEEDBACK
# --------------------------------------------------

def test_feedback_generator():

    result = {

        "final_score": 85,

        "similarity_score": 90,

        "keyword_score": 80,

        "length_score": 100,

        "word_count": 50,

        "matched_keywords": [
            "java",
            "inheritance"
        ],

        "missing_keywords": []
    }

    feedback = generate_feedback(result)

    assert len(feedback) > 0

    assert any(
        "Excellent" in message
        for message in feedback
    )