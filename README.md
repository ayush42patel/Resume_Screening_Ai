# 🚀 AI Resume Screening & Career Assistant

An **AI-powered resume screening and career intelligence system** that analyzes resumes, performs semantic job matching, detects skill gaps, evaluates ATS compatibility, and provides intelligent career improvement suggestions.

This project simulates how modern **AI recruitment engines** and **Applicant Tracking Systems (ATS)** evaluate candidates.

---

## 🌐 Live Demo  
🔗 https://resume-screening-ai-ap.streamlit.app/

---

## 🎯 Project Objective

To design an intelligent pipeline that can:

- Extract skills from resumes (PDF)
- Match resumes with real job roles using **NLP similarity search**
- Identify missing skills (**Skill Gap Analysis**)
- Evaluate **ATS keyword compatibility**
- Generate AI-driven resume improvement suggestions
- Recommend projects and learning roadmaps

---

## 🧠 AI Capabilities

| Feature | Description |
|--------|-------------|
| 📄 Resume Parsing | Extracts structured text from PDF resumes |
| 🧠 Skill Extraction | NLP-based technical skill identification |
| 🔍 Smart Job Matching | **TF-IDF Vectorization + FAISS Similarity Search** |
| 🧩 Tech Role Filtering | Filters only **software/AI/data** jobs using skill-based filtering |
| 📉 Skill Gap Analysis | Detects missing skills per matched role |
| 📊 ATS Score | Measures resume keyword alignment with job skills |
| 💡 AI Suggestions | Resume improvement & optimization tips |
| ✍ Bullet Rewriter | Generates impact-driven resume bullet points |
| 🚀 Career Booster | Project suggestions + personalized skill roadmap |

---

## ⚙️ System Workflow

1. Resume PDF uploaded  
2. Text extraction using NLP pipeline  
3. Technical skills detected  
4. Resume vector compared against job dataset  
5. System generates:
   - Job Match Score
   - Missing Skills
   - ATS Compatibility Score
   - Resume Suggestions
   - Project Ideas
   - Learning Roadmap

---

## 🧠 Matching Architecture
```bash
Resume → Text Cleaning → Skill Extraction
↓
TF-IDF Vectorization
↓
FAISS Similarity Search
↓
Tech-Filtered Job Roles
↓
Skill Gap + ATS + AI Suggestions
```

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn** (TF-IDF)
- **FAISS** (Fast similarity search)
- **Pandas**
- **PDFPlumber**
- **Plotly** (Interactive metrics)

---

## 📁 Project Structure

```bash
resume_screening_ai/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── jobs_sample.csv      # Cloud dataset
│   └── (jobs.csv local only)
│
└── src/
    ├── resume_parser.py
    ├── skill_extractor.py
    ├── matcher.py
    ├── suggestion_engine.py
    ├── ai_career_tools.py
    └── text_utils.py
```

## ☁️ Deployment Design

| Environment | Dataset Used |
|--------|-------------|
| Local | Full Kaggle job dataset |
| Streamlit Cloud | Lightweight sample dataset |
| Vector Index | Auto-built at runtime |

## 🚀 Future Improvements

- **Sentence-BERT semantic matching**
- **Salary trend prediction**
- **Role-based recommendation system**
- **Job market analytics dashboard**

## 👨‍💻 Author

Ayush Patel<br>
B.Tech CSE (Data Science)<br>
Open to AI/ML internships, research roles, and collaborations.
