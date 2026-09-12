from src.speech.filler_detector import (
    detect_filler_words
)


# --------------------------------------------------
# SPEAKING SPEED
# --------------------------------------------------

def calculate_speaking_speed(
    text,
    duration_seconds
):
    """
    Calculate words per minute.
    """

    if not text or duration_seconds <= 0:

        return 0

    words = len(
        text.split()
    )

    minutes = (
        duration_seconds / 60
    )

    wpm = words / minutes

    return round(wpm, 2)


# --------------------------------------------------
# SPEAKING ANALYSIS
# --------------------------------------------------

def analyze_voice(
    text,
    duration_seconds
):
    """
    Analyze speaking performance.
    """

    filler_result = (
        detect_filler_words(text)
    )

    speaking_speed = (
        calculate_speaking_speed(
            text,
            duration_seconds
        )
    )

    # Speaking speed evaluation

    if speaking_speed == 0:

        speed_feedback = (
            "No speech detected."
        )

    elif speaking_speed < 100:

        speed_feedback = (
            "Your speaking speed is slow. "
            "Try to speak more naturally."
        )

    elif speaking_speed <= 160:

        speed_feedback = (
            "Your speaking speed is good "
            "for an interview."
        )

    elif speaking_speed <= 190:

        speed_feedback = (
            "You are speaking slightly fast. "
            "Try to slow down."
        )

    else:

        speed_feedback = (
            "You are speaking too fast. "
            "Pause and speak clearly."
        )

    # Filler evaluation

    filler_percentage = (
        filler_result[
            "filler_percentage"
        ]
    )

    if filler_percentage < 3:

        filler_feedback = (
            "Excellent fluency with very few "
            "filler words."
        )

    elif filler_percentage < 7:

        filler_feedback = (
            "Good fluency. Reduce filler "
            "words slightly."
        )

    else:

        filler_feedback = (
            "You use many filler words. "
            "Practice speaking with short pauses."
        )

    return {

        "speaking_speed_wpm":
            speaking_speed,

        "filler_count":
            filler_result["count"],

        "filler_percentage":
            filler_percentage,

        "filler_words":
            filler_result["fillers"],

        "speed_feedback":
            speed_feedback,

        "filler_feedback":
            filler_feedback
    }