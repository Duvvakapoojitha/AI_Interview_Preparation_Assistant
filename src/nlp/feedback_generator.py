def generate_feedback(result):

    score = result["final_score"]

    matched = result["matched_keywords"]

    missing = result["missing_keywords"]

    feedback = []

    if score >= 85:

        feedback.append(
            "Excellent answer. Your response is highly relevant and well aligned with the expected answer."
        )

    elif score >= 70:

        feedback.append(
            "Good answer. You demonstrated a reasonable understanding of the topic."
        )

    elif score >= 50:

        feedback.append(
            "Average answer. You should provide more relevant technical details."
        )

    else:

        feedback.append(
            "Your answer needs improvement. Focus on the main concepts asked in the question."
        )

    if matched:

        feedback.append(
            "Concepts identified: "
            + ", ".join(matched)
        )

    if missing:

        feedback.append(
            "Important concepts missing: "
            + ", ".join(missing)
        )

    if result["word_count"] < 20:

        feedback.append(
            "Your answer is quite short. Try explaining the concept with an example."
        )

    return feedback