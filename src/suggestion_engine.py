def generate_resume_suggestions(skills, missing_skills, ats_score):
    suggestions = []

    if ats_score < 50:
        suggestions.append("Increase ATS keyword coverage by adding more job-relevant technical terms.")

    if missing_skills:
        suggestions.append(
            f"Consider learning or mentioning skills like {', '.join(missing_skills[:3])} to improve job match rates."
        )

    if "machine learning" in skills and "project" not in skills:
        suggestions.append("Add a Machine Learning project with results and metrics.")

    if "data science" in skills and "statistics" not in skills:
        suggestions.append("Include statistical analysis or data modeling projects.")

    suggestions.append("Add measurable achievements (e.g., improved accuracy by 15%).")
    suggestions.append("Use action verbs like 'Developed', 'Built', 'Implemented' in bullet points.")
    suggestions.append("Ensure your resume is 1 page and ATS-friendly format.")

    return suggestions
