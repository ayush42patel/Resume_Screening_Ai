import pandas as pd

def build_jobs_dataset(postings_path, skills_path, summary_path, output_path):
    print("Loading reduced datasets...")

    # Load only necessary columns + limited rows
    postings = pd.read_csv(
        postings_path,
        usecols=["job_link", "job_title", "company"],
        nrows=200000
    )

    summary = pd.read_csv(
        summary_path,
        usecols=["job_link", "job_summary"],
        nrows=200000
    )

    skills = pd.read_csv(
        skills_path,
        usecols=["job_link", "job_skills"],
        nrows=400000
    )

    print("Combining skills per job...")
    skills_grouped = (
        skills.groupby("job_link")["job_skills"]
        .apply(lambda x: ", ".join(x.astype(str).str.lower()))
        .reset_index()
    )

    print("Merging datasets...")
    df = postings.merge(summary, on="job_link", how="left")
    df = df.merge(skills_grouped, on="job_link", how="left")

    df = df.rename(columns={
        "job_summary": "job_description",
        "job_skills": "required_skills"
    })

    df = df[["job_title", "company", "job_description", "required_skills"]]

    df["job_description"] = df["job_description"].fillna("").astype(str).str.lower()
    df["required_skills"] = df["required_skills"].fillna("").astype(str).str.lower()

    df.dropna(subset=["job_title", "job_description"], inplace=True)

    print("Saving jobs.csv...")
    df.to_csv(output_path, index=False)

    print("jobs.csv created FAST.")
