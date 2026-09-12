import random


def get_questions(df):

    return df[
        [
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
    ].to_dict("records")


def get_random_question(df):

    if len(df) == 0:
        return None

    index = random.randint(0, len(df) - 1)

    return df.iloc[index].to_dict()


def get_random_questions(df, number_of_questions=5):

    if len(df) == 0:
        return []

    number_of_questions = min(
        number_of_questions,
        len(df)
    )

    selected = df.sample(
        number_of_questions
    )

    return selected.to_dict("records")