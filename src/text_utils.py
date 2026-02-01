import re

def normalize_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9, ]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_skills(skill_str):
    skill_str = normalize_text(skill_str)
    skills = [s.strip() for s in skill_str.split(",") if s.strip()]
    return list(set(skills))
