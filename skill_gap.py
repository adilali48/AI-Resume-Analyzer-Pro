import re


class SkillGapAnalyzer:

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
            "kubernetes",
            "aws",
            "azure",
            "git",
            "github",
            "linux",
            "react",
            "javascript",
            "nodejs"
        ]

    def analyze(self, resume, job):

        resume = resume.lower()
        job = job.lower()

        found = []
        missing = []

        for skill in self.skills:

            if skill in job:

                if skill in resume:
                    found.append(skill.title())
                else:
                    missing.append(skill.title())

        total = len(found) + len(missing)

        if total == 0:
            percentage = 100
        else:
            percentage = int((len(found) / total) * 100)

        return found, missing, percentage