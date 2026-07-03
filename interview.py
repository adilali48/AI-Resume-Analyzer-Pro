import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class InterviewGenerator:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.3
        )

    def generate(self, resume, job_description=""):

        prompt = f"""
You are a Senior Technical Interviewer.

Resume:

{resume}

Job Description:

{job_description}

Generate:

# Technical Interview Questions
(5 questions with sample answers)

# HR Interview Questions
(5 questions with sample answers)

# Behavioral Questions
(5 questions with sample answers)

# Interview Preparation Tips
"""

        response = self.llm.invoke(prompt)

        return response.content