import os
import pickle
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    import faiss
    FAISS_AVAILABLE = True
except:
    FAISS_AVAILABLE = False

DATA_DIR = "data"
VECTORIZER_PATH = os.path.join(DATA_DIR, "vectorizer.pkl")
INDEX_PATH = os.path.join(DATA_DIR, "faiss_index.bin")
META_PATH = os.path.join(DATA_DIR, "jobs_meta.pkl")
JOBS_PATH = os.path.join(DATA_DIR, "jobs.csv")


def build_index():
    print("Building vector index...")

    df = pd.read_csv(JOBS_PATH)
    texts = (df["job_description"].fillna("") + " " + df["required_skills"].fillna(""))

    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    job_vectors = vectorizer.fit_transform(texts).toarray()

    pickle.dump(vectorizer, open(VECTORIZER_PATH, "wb"))
    df.to_pickle(META_PATH)

    if FAISS_AVAILABLE:
        dim = job_vectors.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(job_vectors.astype("float32"))
        faiss.write_index(index, INDEX_PATH)

    print("Index built.")


def match_resume_to_jobs(resume_text):

    # If artifacts missing → build them
    if not os.path.exists(VECTORIZER_PATH) or not os.path.exists(META_PATH):
        build_index()

    vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))
    JOBS_PATH = os.path.join(DATA_DIR, "jobs.csv")
    SAMPLE_PATH = os.path.join(DATA_DIR, "jobs_sample.csv")

    if not os.path.exists(JOBS_PATH):
        JOBS_PATH = SAMPLE_PATH


    resume_vec = vectorizer.transform([resume_text]).toarray()

    if FAISS_AVAILABLE and os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        distances, indices = index.search(resume_vec.astype("float32"), 10)
        results = jobs_df.iloc[indices[0]].copy()
        results["match_score"] = 1 / (1 + distances[0])
    else:
        job_vectors = vectorizer.transform(
            (jobs_df["job_description"] + " " + jobs_df["required_skills"]).fillna("")
        ).toarray()

        similarities = cosine_similarity(resume_vec, job_vectors)[0]
        results = jobs_df.copy()
        results["match_score"] = similarities
        results = results.sort_values(by="match_score", ascending=False).head(10)

    return results.reset_index(drop=True)
