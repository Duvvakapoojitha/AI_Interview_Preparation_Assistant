import streamlit as st
import pandas as pd

from src.data_processing.clean_data import load_dataset
from src.data_processing.preprocessing import preprocess_dataset

from src.interview.company_filter import (
    get_companies,
    filter_by_company,
    filter_by_industry,
    filter_by_role
)

from src.interview.difficulty_selector import (
    get_difficulties,
    filter_by_difficulty
)

from src.interview.question_generator import (
    get_random_question
)

from src.nlp.answer_evaluator import AnswerEvaluator
from src.nlp.feedback_generator import generate_feedback


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(
    "🤖 AI Interview Preparation Assistant"
)

st.write(
    "AI-powered personalized interview practice using NLP."
)


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

@st.cache_data
def load_data():

    df = load_dataset()

    df = preprocess_dataset(df)

    return df


df = load_data()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Interview Configuration")


# Company

companies = get_companies(df)

company = st.sidebar.selectbox(
    "Select Company",
    ["All Companies"] + companies
)


# Company filtering

filtered_df = filter_by_company(
    df,
    company
)


# Industry

industries = sorted(
    filtered_df["Industry"]
    .unique()
    .tolist()
)

industry = st.sidebar.selectbox(
    "Select Industry",
    ["All Industries"] + industries
)


filtered_df = filter_by_industry(
    filtered_df,
    industry
)


# Role

roles = sorted(
    filtered_df["Role"]
    .unique()
    .tolist()
)

role = st.sidebar.selectbox(
    "Select Role",
    ["All Roles"] + roles
)


filtered_df = filter_by_role(
    filtered_df,
    role
)


# Difficulty

difficulties = get_difficulties(
    filtered_df
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["All Levels"] + difficulties
)


filtered_df = filter_by_difficulty(
    filtered_df,
    difficulty
)


# --------------------------------------------------
# DATASET INFORMATION
# --------------------------------------------------

st.sidebar.markdown("---")

st.sidebar.write(
    f"📚 Questions available: {len(filtered_df)}"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "question" not in st.session_state:

    st.session_state.question = None


if "answer" not in st.session_state:

    st.session_state.answer = ""


# --------------------------------------------------
# GENERATE QUESTION
# --------------------------------------------------

if st.button("🎯 Generate Interview Question"):

    if len(filtered_df) == 0:

        st.error(
            "No questions found for the selected filters."
        )

    else:

        st.session_state.question = (
            get_random_question(
                filtered_df
            )
        )

        st.session_state.answer = ""


# --------------------------------------------------
# DISPLAY QUESTION
# --------------------------------------------------

question = st.session_state.question


if question:

    st.markdown("---")

    st.subheader("Interview Question")

    st.info(
        question["Question"]
    )

    # Question metadata

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Company",
            question["Company"]
        )

    with col2:

        st.metric(
            "Role",
            question["Role"]
        )

    with col3:

        st.metric(
            "Round",
            question["Round"]
        )

    with col4:

        st.metric(
            "Difficulty",
            question["Difficulty"]
        )


    # --------------------------------------------------
    # ANSWER
    # --------------------------------------------------

    st.subheader("Your Answer")

    answer = st.text_area(
        "Type your interview answer below:",
        height=200,
        key="answer"
    )


    # --------------------------------------------------
    # ANALYZE
    # --------------------------------------------------

    if st.button("🧠 Analyze My Answer"):

        if not answer.strip():

            st.warning(
                "Please enter an answer first."
            )

        else:

            with st.spinner(
                "AI is evaluating your answer..."
            ):

                evaluator = AnswerEvaluator()

                result = evaluator.evaluate(

                    candidate_answer=answer,

                    expected_answer=
                    question["Expected_Answer"],

                    keywords=
                    question["Keywords"]
                )


            # --------------------------------------------------
            # SCORE
            # --------------------------------------------------

            st.markdown("---")

            st.subheader(
                "📊 Interview Performance"
            )


            col1, col2, col3, col4 = st.columns(4)


            with col1:

                st.metric(
                    "Final Score",
                    f"{result['final_score']}%"
                )


            with col2:

                st.metric(
                    "Similarity",
                    f"{result['similarity_score']}%"
                )


            with col3:

                st.metric(
                    "Keyword Score",
                    f"{result['keyword_score']}%"
                )


            with col4:

                st.metric(
                    "Word Count",
                    result["word_count"]
                )


            # --------------------------------------------------
            # FEEDBACK
            # --------------------------------------------------

            st.subheader(
                "💡 AI Feedback"
            )

            feedback = generate_feedback(
                result
            )

            for item in feedback:

                st.write(
                    "• " + item
                )


            # --------------------------------------------------
            # FOLLOW-UP QUESTION
            # --------------------------------------------------

            st.subheader(
                "🔄 Possible Follow-up Question"
            )

            st.warning(
                question["Follow_Up_Question"]
            )


            # --------------------------------------------------
            # EVALUATION CRITERIA
            # --------------------------------------------------

            with st.expander(
                "View Evaluation Criteria"
            ):

                st.write(
                    question[
                        "Evaluation_Criteria"
                    ]
                )


else:

    st.info(
        "Select your interview preferences "
        "and click 'Generate Interview Question'."
    )