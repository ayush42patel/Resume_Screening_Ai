import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_jobs(resume_text, jobs_csv_path):
    jobs_df = pd.read_csv(jobs_csv_path)

    documents = [resume_text] + jobs_df["job_description"].fillna("").tolist()

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    jobs_df["match_score"] = similarity_scores

    return jobs_df.sort_values(by="match_score", ascending=False)
