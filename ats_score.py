import re


class ATSScore:

    def __init__(self):

        self.skills = [
            "python",
            "java",
            "c++",
            "sql",
            "mysql",
            "mongodb",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "langchain",
            "streamlit",
            "fastapi",
            "docker",
            "git",
            "github",
            "linux",
            "aws",
            "azure",
            "javascript",
            "react"
        ]

    def calculate(self, resume):

        score = 0

        # Email
        if re.search(r"\S+@\S+\.\S+", resume):
            score += 10

        # Phone
        if re.search(r"\+?\d[\d\s-]{8,}", resume):
            score += 10

        # Education
        if "education" in resume.lower():
            score += 10

        # Experience
        if "experience" in resume.lower():
            score += 15

        # Projects
        if "project" in resume.lower():
            score += 15

        # Skills
        found = 0

        for skill in self.skills:

            if skill.lower() in resume.lower():
                found += 1

        score += min(found * 2, 30)

        # Certifications
        if "certification" in resume.lower():
            score += 10

        return min(score, 100)