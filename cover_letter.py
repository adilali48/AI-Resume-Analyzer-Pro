import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class CoverLetterGenerator:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.3
        )

    def generate(self, resume, job_description):

        prompt = f"""
You are an expert HR recruiter.

Using the resume and job description below,
write a professional cover letter.

Requirements:

- Professional tone
- One page
- Mention relevant skills
- Mention experience
- Explain why the candidate is a good fit
- End politely

Resume:

{resume}

--------------------------------

Job Description:

{job_description}
"""

        response = self.llm.invoke(prompt)

        return response.content