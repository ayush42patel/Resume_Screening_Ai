import re

SKILL_KEYWORDS = [
    "python","sql","machine learning","data science","pandas",
    "numpy","scikit-learn","power bi","excel","statistics",
    "nlp","deep learning","tensorflow","tableau","docker","git","linux"
]

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    found = []

    for skill in SKILL_KEYWORDS:
        if re.search(r"\b" + re.escape(skill) + r"\b", resume_text):
            found.append(skill)

    return list(set(found))
