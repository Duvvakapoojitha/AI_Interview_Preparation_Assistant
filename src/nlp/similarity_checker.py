import re

from sklearn.metrics.pairwise import cosine_similarity


class SimilarityChecker:

    def __init__(self):
        """Use a lightweight local similarity scorer with no ML dependency."""

    @staticmethod
    def _lexical_similarity(candidate_answer, expected_answer):
        """Return cosine similarity over word frequencies without an ML model."""

        candidate_words = re.findall(
            r"\b\w+\b", candidate_answer.lower()
        )
        expected_words = re.findall(
            r"\b\w+\b", expected_answer.lower()
        )

        if not candidate_words or not expected_words:
            return 0.0

        vocabulary = sorted(
            set(candidate_words) | set(expected_words)
        )
        candidate_vector = [
            candidate_words.count(word) for word in vocabulary
        ]
        expected_vector = [
            expected_words.count(word) for word in vocabulary
        ]

        return float(
            cosine_similarity(
                [candidate_vector], [expected_vector]
            )[0][0]
        )

    def calculate_similarity(
        self,
        candidate_answer,
        expected_answer
    ):

        if not candidate_answer.strip():
            return 0.0

        if not expected_answer.strip():
            return 0.0

        return self._lexical_similarity(
            candidate_answer,
            expected_answer
        )

    def similarity_percentage(
        self,
        candidate_answer,
        expected_answer
    ):

        score = self.calculate_similarity(
            candidate_answer,
            expected_answer
        )

        return round(score * 100, 2)
