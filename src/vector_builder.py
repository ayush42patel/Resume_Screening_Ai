import pandas as pd
import pickle
import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from src.text_utils import normalize_text

# 🎯 Only keep tech roles
TECH_KEYWORDS = [
    "engineer","developer","data","machine learning",
    "software","analyst","ai","python","cloud","ml"
]

def build_vector_index(jobs_path):
    print("Loading jobs...")
    df = pd.read_csv(jobs_path)

    # 🔹 Filter to tech jobs only
    df = df[df["job_title"].str.lower().str.contains("|".join(TECH_KEYWORDS), na=False)]
    print(f"Jobs after tech filter: {len(df)}")

    # 🔹 Normalize text
    texts = (df["job_description"].fillna("") + " " + df["required_skills"].fillna("")).apply(normalize_text)

    print("Training TF-IDF...")
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    job_vectors = vectorizer.fit_transform(texts).toarray().astype("float32")

    print("Building FAISS index...")
    dim = job_vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(job_vectors)

    # Save artifacts
    pickle.dump(vectorizer, open("data/vectorizer.pkl", "wb"))
    faiss.write_index(index, "data/faiss_index.bin")
    df.to_pickle("data/jobs_meta.pkl")

    print("Vector index built and saved.")
