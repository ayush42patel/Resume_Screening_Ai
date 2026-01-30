# 🚀 AI Resume Screening & Career Assistant

An **AI-powered resume screening and career intelligence system** that analyzes resumes, matches jobs using NLP, detects skill gaps, and provides intelligent improvement suggestions.

This project simulates how modern **recruitment platforms** and **ATS (Applicant Tracking Systems)** evaluate candidates.

---

## 🌐 Live Demo
🔗 https://resume-screening-ai-ap.streamlit.app/

---

## 🎯 Project Objective

To build an intelligent system that can:

- Extract skills from resumes (PDF)
- Match resumes with job roles using NLP similarity
- Identify missing skills (Skill Gap Analysis)
- Evaluate ATS keyword compatibility
- Generate AI-based resume improvement suggestions
- Suggest projects, learning roadmap, and stronger resume bullet points

---

## 🧠 AI Capabilities

| Feature | Description |
|--------|-------------|
| 📄 Resume Parsing | Extracts structured text from PDF resumes |
| 🧠 Skill Extraction | NLP-based keyword detection of technical skills |
| 🔍 Job Matching | TF-IDF Vectorization + Cosine Similarity |
| 📉 Skill Gap Analysis | Identifies missing skills compared to job requirements |
| 📊 ATS Score | Keyword density evaluation |
| 💡 AI Suggestions | Resume improvement recommendations |
| ✍ Bullet Rewriter | Generates impact-driven resume bullet points |
| 🚀 Career Booster | Suggests projects + personalized skill roadmap |

---

## ⚙️ System Workflow

1. Resume PDF uploaded  
2. Text extraction using NLP pipeline  
3. Skills identified  
4. Resume matched against jobs dataset  
5. AI generates:
   - Match Score
   - Missing Skills
   - ATS Score
   - Resume Suggestions
   - Project Ideas
   - Learning Roadmap

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn** (TF-IDF, Cosine Similarity)
- **Pandas**
- **PDFPlumber**
- **Plotly** (Interactive Score Gauge)

---

## 📁 Project Structure

```bash
resume_screening_ai/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── jobs.csv
│
└── src/
    ├── resume_parser.py
    ├── skill_extractor.py
    ├── matcher.py
    ├── suggestion_engine.py
    └── ai_career_tools.py
