def rewrite_resume_bullet(skill):
    templates = {
        "python": "Developed Python-based automation scripts improving workflow efficiency.",
        "machine learning": "Built machine learning models and improved performance using feature engineering.",
        "data science": "Analyzed complex datasets to extract insights and drive decision-making.",
        "sql": "Designed SQL queries for data extraction and reporting.",
        "power bi": "Created interactive dashboards in Power BI to visualize key metrics."
    }
    return templates.get(skill.lower(), f"Worked on projects involving {skill}.")


def suggest_projects(missing_skills):
    project_templates = {
        "tensorflow": "Deep Learning Image Classification using TensorFlow",
        "docker": "Deploy ML model using Docker container",
        "nlp": "Sentiment Analysis System using NLP",
        "statistics": "A/B Testing and Statistical Analysis Project"
    }

    suggestions = []
    for skill in missing_skills:
        if skill in project_templates:
            suggestions.append(project_templates[skill])

    return suggestions[:3]


def skill_roadmap(missing_skills):
    roadmap = []

    for skill in missing_skills[:5]:
        roadmap.append(f"Start learning {skill} through projects and hands-on practice.")

    return roadmap
