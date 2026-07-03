import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class ResumeRewriter:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.2
        )

    def rewrite(self, resume):

        prompt = f"""
You are a professional Resume Writer.

Rewrite the following resume professionally.

Rules:

- Improve grammar.
- Improve formatting.
- Improve professional wording.
- Keep all information truthful.
- Make it ATS friendly.
- Add professional bullet points.
- Improve project descriptions.
- Improve skills section.
- Improve summary.

Return the improved resume in proper markdown.

Resume:

{resume}
"""

        response = self.llm.invoke(prompt)

        return response.content