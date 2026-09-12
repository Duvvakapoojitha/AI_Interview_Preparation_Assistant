def extract_keywords(keyword_text):

    if not keyword_text:
        return []

    keywords = keyword_text.split(",")

    keywords = [
        keyword.strip().lower()
        for keyword in keywords
        if keyword.strip()
    ]

    return keywords


def find_matching_keywords(answer, expected_keywords):

    answer = answer.lower()

    matched = []
    missing = []

    for keyword in expected_keywords:

        if keyword.lower() in answer:
            matched.append(keyword)
        else:
            missing.append(keyword)

    return matched, missing