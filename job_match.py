import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class JobMatcher:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.2
        )

    def analyze(self, resume, job_description):

        prompt = f"""
You are an expert HR Recruiter.

Compare the following resume with the job description.

Resume:

{resume}

-----------------------------------------

Job Description:

{job_description}

-----------------------------------------

Generate the report in this exact format.

# Job Match Score

Give a percentage between 0 and 100.

# Matching Skills

- Skill 1
- Skill 2
- Skill 3

# Missing Skills

- Skill 1
- Skill 2
- Skill 3

# Hiring Recommendation

Write a short paragraph.

# Resume Improvement Tips

- Tip 1
- Tip 2
- Tip 3
"""

        response = self.llm.invoke(prompt)

        return response.content