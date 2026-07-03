import fitz  # PyMuPDF
import docx
import os


class ResumeParser:

    def __init__(self):
        pass

    def extract_text(self, uploaded_file):

        filename = uploaded_file.name.lower()

        if filename.endswith(".pdf"):
            return self.extract_pdf(uploaded_file)

        elif filename.endswith(".docx"):
            return self.extract_docx(uploaded_file)

        else:
            return "Unsupported file format."

    def extract_pdf(self, uploaded_file):

        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text

    def extract_docx(self, uploaded_file):

        document = docx.Document(uploaded_file)

        text = ""

        for para in document.paragraphs:
            text += para.text + "\n"

        return text