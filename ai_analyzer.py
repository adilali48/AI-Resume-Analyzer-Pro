import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class AIAnalyzer:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.2
        )

    def analyze(self, resume_text):

        prompt = f"""
You are an expert HR recruiter and ATS Resume Expert.

Analyze the following resume.

Resume:

{resume_text}

Generate a professional report in this exact format.

# Resume Summary

Write a short professional summary.

# ATS Score

Give an ATS score out of 100.

# Strengths

- Point 1
- Point 2
- Point 3

# Weaknesses

- Point 1
- Point 2

# Missing Skills

- Point 1
- Point 2
- Point 3

# Improvement Suggestions

- Point 1
- Point 2
- Point 3

# Recommended Job Roles

- Role 1
- Role 2
- Role 3
"""

        response = self.llm.invoke(prompt)

        return response.content