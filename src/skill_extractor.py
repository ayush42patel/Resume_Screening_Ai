import re

SKILL_KEYWORDS = [
    "python", "java", "sql", "machine learning", "data science",
    "pandas", "numpy", "scikit-learn", "power bi", "excel",
    "statistics", "nlp", "deep learning", "tensorflow", "tableau",
    "docker", "git", "linux"
]

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text):
            found_skills.append(skill)

    return list(set(found_skills))
