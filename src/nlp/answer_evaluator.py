from src.nlp.similarity_checker import SimilarityChecker
from src.nlp.keyword_extractor import (
    extract_keywords,
    find_matching_keywords
)


class AnswerEvaluator:

    def __init__(self):

        self.similarity_checker = SimilarityChecker()

    def evaluate(
        self,
        candidate_answer,
        expected_answer,
        keywords
    ):

        # Similarity
        similarity = (
            self.similarity_checker
            .similarity_percentage(
                candidate_answer,
                expected_answer
            )
        )

        # Keywords
        keyword_list = extract_keywords(keywords)

        matched, missing = find_matching_keywords(
            candidate_answer,
            keyword_list
        )

        if len(keyword_list) > 0:

            keyword_score = (
                len(matched)
                / len(keyword_list)
            ) * 100

        else:

            keyword_score = 0

        # Answer length score
        word_count = len(
            candidate_answer.split()
        )

        if word_count >= 80:
            length_score = 100

        elif word_count >= 40:
            length_score = 80

        elif word_count >= 20:
            length_score = 60

        elif word_count >= 10:
            length_score = 40

        else:
            length_score = 20

        # Final score
        final_score = (
            similarity * 0.60
            + keyword_score * 0.30
            + length_score * 0.10
        )

        return {
            "similarity_score": round(
                similarity, 2
            ),

            "keyword_score": round(
                keyword_score, 2
            ),

            "length_score": round(
                length_score, 2
            ),

            "final_score": round(
                final_score, 2
            ),

            "matched_keywords": matched,

            "missing_keywords": missing,

            "word_count": word_count
        }