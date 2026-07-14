from io import BytesIO

from docx import Document
from pypdf import PdfReader


def read_uploaded_cv(uploaded_file) -> str:
    file_name = uploaded_file.name.lower()
    file_bytes = uploaded_file.getvalue()

    try:
        if file_name.endswith(".pdf"):
            reader = PdfReader(BytesIO(file_bytes))
            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        elif file_name.endswith(".docx"):
            document = Document(BytesIO(file_bytes))
            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

        elif file_name.endswith(".txt"):
            text = file_bytes.decode("utf-8")

        else:
            raise ValueError("Unsupported CV file type.")

    except ValueError:
        raise

    except Exception as error:
        raise ValueError(
            "The uploaded CV could not be read."
        ) from error

    cleaned_text = text.strip()

    if not cleaned_text:
        raise ValueError(
            "No readable text was found in the uploaded CV."
        )

    return cleaned_text
