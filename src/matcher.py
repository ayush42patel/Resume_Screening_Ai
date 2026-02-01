import pickle
import faiss
import numpy as np
import pandas as pd

def match_resume_to_jobs(resume_text):
    vectorizer = pickle.load(open("data/vectorizer.pkl", "rb"))
    index = faiss.read_index("data/faiss_index.bin")
    jobs_df = pd.read_pickle("data/jobs_meta.pkl")

    resume_vec = vectorizer.transform([resume_text]).toarray().astype("float32")

    k = 10
    distances, indices = index.search(resume_vec, k)

    results = jobs_df.iloc[indices[0]].copy()
    results["match_score"] = 1 / (1 + distances[0])

    return results
