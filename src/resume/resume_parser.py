import os
from PyPDF2 import PdfReader
from docx import Document


# --------------------------------------------------
# PDF PARSER
# --------------------------------------------------

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF resume.
    """

    text = ""

    try:

        reader = PdfReader(file_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as error:

        print(
            "PDF extraction error:",
            error
        )

    return text.strip()


# --------------------------------------------------
# DOCX PARSER
# --------------------------------------------------

def extract_text_from_docx(file_path):
    """
    Extract text from a DOCX resume.
    """

    text = ""

    try:

        document = Document(file_path)

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                text += (
                    paragraph.text
                    + "\n"
                )

    except Exception as error:

        print(
            "DOCX extraction error:",
            error
        )

    return text.strip()


# --------------------------------------------------
# GENERAL RESUME PARSER
# --------------------------------------------------

def parse_resume(file_path):
    """
    Automatically detect resume format
    and extract text.
    """

    if not os.path.exists(file_path):

        raise FileNotFoundError(
            "Resume file not found."
        )

    extension = (
        os.path.splitext(file_path)[1]
        .lower()
    )

    if extension == ".pdf":

        return extract_text_from_pdf(
            file_path
        )

    elif extension == ".docx":

        return extract_text_from_docx(
            file_path
        )

    else:

        raise ValueError(
            "Unsupported resume format. "
            "Please upload PDF or DOCX."
        )