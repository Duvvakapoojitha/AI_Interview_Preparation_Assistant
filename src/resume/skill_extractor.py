import re


# --------------------------------------------------
# SKILL DATABASE
# --------------------------------------------------

TECHNICAL_SKILLS = [

    # Programming
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "kotlin",
    "go",
    "rust",

    # Java
    "spring",
    "spring boot",
    "hibernate",
    "jdbc",
    "servlets",
    "jsp",

    # Web
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "express",

    # Database
    "mysql",
    "postgresql",
    "oracle",
    "mongodb",
    "sql",
    "nosql",
    "dbms",

    # Core CS
    "data structures",
    "algorithms",
    "dsa",
    "oop",
    "operating systems",
    "computer networks",

    # Cloud
    "aws",
    "azure",
    "google cloud",
    "oracle cloud",
    "ibm cloud",

    # DevOps
    "docker",
    "kubernetes",
    "jenkins",
    "git",
    "github",
    "linux",

    # AI / ML
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "computer vision",
    "tensorflow",
    "pytorch",
    "scikit-learn",

    # Data
    "pandas",
    "numpy",
    "matplotlib",
    "power bi",
    "tableau",

    # APIs / Architecture
    "rest api",
    "rest",
    "microservices",
    "api",

    # Cybersecurity
    "cybersecurity",
    "network security",
    "ethical hacking",

    # Testing
    "selenium",
    "junit",
    "testing",
    "unit testing"
]


# --------------------------------------------------
# SKILL EXTRACTION
# --------------------------------------------------

def extract_skills(resume_text):
    """
    Extract technical skills from resume text.
    """

    if not resume_text:

        return []

    text = resume_text.lower()

    found_skills = []

    for skill in TECHNICAL_SKILLS:

        # Escape special characters
        pattern = re.escape(skill)

        # Search skill
        if re.search(
            r"\b" + pattern + r"\b",
            text
        ):

            found_skills.append(skill)

    return sorted(
        list(set(found_skills))
    )


# --------------------------------------------------
# SKILL MATCHING WITH DATASET
# --------------------------------------------------

def match_skills_with_dataset(
    resume_skills,
    df
):
    """
    Find interview questions related
    to skills found in the resume.
    """

    if not resume_skills:

        return df.iloc[0:0]

    if "Keywords" not in df.columns:

        return df.iloc[0:0]

    matched_rows = []

    for index, row in df.iterrows():

        keywords = str(
            row["Keywords"]
        ).lower()

        question = str(
            row["Question"]
        ).lower()

        for skill in resume_skills:

            if (
                skill.lower() in keywords
                or skill.lower() in question
            ):

                matched_rows.append(index)

                break

    matched_rows = list(
        set(matched_rows)
    )

    return df.loc[matched_rows]


# --------------------------------------------------
# SKILL SUMMARY
# --------------------------------------------------

def get_skill_summary(resume_text):

    skills = extract_skills(
        resume_text
    )

    return {
        "total_skills": len(skills),
        "skills": skills
    }