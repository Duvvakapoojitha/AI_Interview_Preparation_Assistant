import speech_recognition as sr


# --------------------------------------------------
# SPEECH TO TEXT
# --------------------------------------------------

def speech_to_text():

    """
    Capture audio from microphone
    and convert it to text.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print(
            "Listening... Please speak."
        )

        # Adjust microphone for background noise
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source
        )

    try:

        text = recognizer.recognize_google(
            audio
        )

        print(
            "You said:",
            text
        )

        return text

    except sr.UnknownValueError:

        print(
            "Could not understand the audio."
        )

        return ""

    except sr.RequestError:

        print(
            "Speech recognition service unavailable."
        )

        return ""


# --------------------------------------------------
# SPEECH TO TEXT WITH ERROR HANDLING
# --------------------------------------------------

def convert_audio_to_text(audio):

    """
    Convert an audio object to text.
    """

    recognizer = sr.Recognizer()

    try:

        text = recognizer.recognize_google(
            audio
        )

        return text

    except (
        sr.UnknownValueError,
        sr.RequestError
    ):

        return ""