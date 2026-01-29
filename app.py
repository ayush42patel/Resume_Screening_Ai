import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go
from src.resume_parser import extract_text_from_resume
from src.skill_extractor import extract_skills
from src.matcher import match_resume_to_jobs
from src.suggestion_engine import generate_resume_suggestions
from src.ai_career_tools import rewrite_resume_bullet, suggest_projects, skill_roadmap

st.set_page_config(page_title="AI Resume Screening", layout="wide")

# --------------------------------------------------
# PATHS (GLOBAL)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JOBS_PATH = os.path.join(BASE_DIR, "data", "jobs.csv")

# --------------------------------------------------
# STYLING
# --------------------------------------------------
st.markdown("""
<style>
.stApp {background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%); font-family:"Segoe UI";}
.section-card {background:#fff;padding:25px;border-radius:16px;margin-top:20px;box-shadow:0 4px 14px rgba(0,0,0,0.08);border:1px solid #e5e7eb;}
.skill-badge {background:#e3f2fd;color:#0d47a1;padding:6px 14px;border-radius:20px;margin:5px;display:inline-block;font-size:14px;font-weight:500;}
.ai-box {background:#e8f5e9;padding:15px;border-radius:10px;border-left:4px solid #43a047;margin-top:15px;color:#1b5e20;}
.job-card {transition:transform .25s ease, box-shadow .25s ease;}
.job-card:hover {transform:translateY(-5px);box-shadow:0 10px 22px rgba(0,0,0,.12);}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div style="background:linear-gradient(90deg,#1e3a8a,#2563eb);padding:25px;border-radius:16px;color:white;margin-bottom:25px;">
<h1>🚀 AI Resume Optimizer & Career Assistant</h1>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = extract_text_from_resume("temp_resume.pdf")
    skills = extract_skills(resume_text)

    # --------------------------------------------------
    # 🔥 GLOBAL CALCULATIONS (USED IN ALL TABS)
    # --------------------------------------------------
    results = match_resume_to_jobs(resume_text, JOBS_PATH)
    results["match_percentage"] = (results["match_score"] * 100).round(2)

    resume_skills = set(skills)
    results["missing_skills"] = results["required_skills"].apply(
        lambda x: list(set(x.lower().split(",")) - resume_skills)
    )
    missing_all = list(set(results["missing_skills"].explode().dropna()))

    job_keywords = " ".join(pd.read_csv(JOBS_PATH)["required_skills"])
    ats_score = min((sum(word in job_keywords for word in resume_text.split()) / len(resume_text.split())) * 100, 100)

    # --------------------------------------------------
    # TABS
    # --------------------------------------------------
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📄 Resume Analysis",
        "🔍 Job Matching",
        "📉 Skill Gap",
        "📊 ATS Check",
        "🧠 AI Suggestions",
        "🚀 Career Booster"
    ])

    # TAB 1
    with tab1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("### 🧠 Extracted Skills")
        st.markdown("".join([f'<span class="skill-badge">{s.title()}</span>' for s in skills]), unsafe_allow_html=True)

        resume_score = min(len(skills) * 5, 100)
        fig = go.Figure(go.Indicator(mode="gauge+number", value=resume_score, number={'suffix': "/100"},
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#2563eb"}}))
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(f'<div class="ai-box">AI Insight: Strong skills in <b>{", ".join(skills)}</b>.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # TAB 2
    with tab2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        for _, row in results.head(5).iterrows():
            color = "#16a34a" if row["match_percentage"] > 70 else "#f59e0b"
            st.markdown(f"""<div class="job-card" style="background:white;padding:18px;border-radius:12px;margin-bottom:15px;">
            <h4>{row['job_title']} <span style="color:#6b7280;">@ {row['company']}</span></h4>
            <p><b>Match Score:</b> <span style="color:{color};">{row['match_percentage']}%</span></p>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # TAB 3
    with tab3:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.dataframe(results[["job_title", "missing_skills"]])
        st.markdown('</div>', unsafe_allow_html=True)

    # TAB 4
    with tab4:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.metric("ATS Match Score", f"{ats_score:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

    # TAB 5
    with tab5:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        for s in generate_resume_suggestions(skills, missing_all, ats_score):
            st.markdown(f"<div class='ai-box'>💡 {s}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # TAB 6
    with tab6:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        skill_input = st.selectbox("Select skill", skills)
        st.success(rewrite_resume_bullet(skill_input))
        for p in suggest_projects(missing_all):
            st.markdown(f"<div class='ai-box'>📌 {p}</div>", unsafe_allow_html=True)
        for step in skill_roadmap(missing_all):
            st.markdown(f"<div class='ai-box'>🔹 {step}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div style="margin-top:50px;padding:25px;border-radius:16px;background:#ffffff;box-shadow:0 4px 14px rgba(0,0,0,0.08);text-align:center;font-size:14px;color:#374151;">
<b style="font-size:16px;">AI Resume Optimizer & Career Assistant</b><br>
Built using AI, NLP & Machine Learning<br><br>
<b>Ayush Patel</b> | B.Tech CSE (Data Science)<br><br>
🔗 <a href="https://github.com/ayush42patel" target="_blank">GitHub</a> | 
🔗 <a href="https://www.linkedin.com/in/ayush-42-patel/" target="_blank">LinkedIn</a><br><br>
✉️ Open to internships, AI/ML roles, and collaborations
</div>
""", unsafe_allow_html=True)
