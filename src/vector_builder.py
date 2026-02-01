import pandas as pd
import pickle
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer
from src.text_utils import normalize_text

def build_vector_index(jobs_path):
    print("Loading jobs...")
    df = pd.read_csv(jobs_path)

    texts = (df["job_description"].fillna("") + " " + df["required_skills"].fillna("")).apply(normalize_text)

    print("Training TF-IDF...")
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    job_vectors = vectorizer.fit_transform(texts).toarray()

    print("Building FAISS index...")
    dim = job_vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(job_vectors)

    # Save artifacts
    pickle.dump(vectorizer, open("data/vectorizer.pkl", "wb"))
    faiss.write_index(index, "data/faiss_index.bin")
    df.to_pickle("data/jobs_meta.pkl")

    print("Vector index built and saved.")
