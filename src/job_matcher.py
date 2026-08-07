"""
Job Matching Pipeline

1. Load ChromaDB
2. Read Job Description
3. Hybrid Search
4. Rank Candidates
5. Generate Match Reasoning
6. Generate JSON Output
"""

import json
from pathlib import Path

from config import JOB_DESCRIPTION_DIR, OUTPUT_DIR
from vector_store import VectorStoreManager
from file_loader import ResumeLoader
from chunker import DocumentChunker
from hybrid_search import HybridSearch
from scoring import CandidateScorer
from reasoning import CandidateReasoner


# ============================================================
# Choose Job Description
# ============================================================

def choose_job_description():

    jd_files = sorted(JOB_DESCRIPTION_DIR.glob("*.txt"))

    print("\nAvailable Job Descriptions\n")

    for idx, jd in enumerate(jd_files, start=1):
        print(f"{idx}. {jd.stem}")

    print(f"{len(jd_files)+1}. Enter Custom Job Description")

    choice = int(input("\nSelect Option: "))

    if choice == len(jd_files) + 1:

        print("\nPaste Job Description")
        print("Press ENTER twice to finish\n")

        lines = []

        while True:

            line = input()

            if line == "":
                break

            lines.append(line)

        return "\n".join(lines)

    selected = jd_files[choice - 1]

    with open(selected, "r", encoding="utf-8") as f:
        return f.read()


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 80)
    print("Resume Job Matcher")
    print("=" * 80)

    # --------------------------------------------------------
    # Load Job Description
    # --------------------------------------------------------

    job_description = choose_job_description()

    # --------------------------------------------------------
    # Load Resume Documents
    # --------------------------------------------------------

    loader = ResumeLoader()

    documents = loader.load_documents()

    # --------------------------------------------------------
    # Chunk Documents
    # --------------------------------------------------------

    chunker = DocumentChunker()

    chunks = chunker.split_documents(documents)

    # --------------------------------------------------------
    # Load ChromaDB
    # --------------------------------------------------------

    vector_manager = VectorStoreManager()

    try:

        vector_store = vector_manager.load_vector_store()

    except Exception:

        vector_store = vector_manager.create_vector_store(chunks)

    # --------------------------------------------------------
    # Hybrid Search
    # --------------------------------------------------------

    hybrid = HybridSearch(vector_store)

    hybrid.build_bm25_index(chunks)

    candidates = hybrid.hybrid_search(job_description)

    # --------------------------------------------------------
    # Candidate Ranking
    # --------------------------------------------------------

    scorer = CandidateScorer()

    ranking_df = scorer.rank_candidates(candidates)

    # --------------------------------------------------------
    # Candidate Reasoning
    # --------------------------------------------------------

    reasoner = CandidateReasoner()

    final_output = {

        "job_description": job_description,

        "top_matches": []

    }

    TOP_K = min(10, len(ranking_df))

    for _, candidate in ranking_df.head(TOP_K).iterrows():

        resume_text = "\n\n".join(candidate["chunks"])

        reasoning = reasoner.generate_reasoning(
            job_description=job_description,
            resume_text=resume_text
        )

        final_output["top_matches"].append({

            "candidate_name": candidate["resume_name"],

            "resume_path": candidate["resume_path"],

            "match_score": float(candidate["match_score"]),

            "matched_skills": reasoning["matched_skills"],

            "relevant_excerpts": candidate["chunks"][:2],

            "reasoning": reasoning["reasoning"]

        })

    # --------------------------------------------------------
    # Save JSON
    # --------------------------------------------------------

    output_file = OUTPUT_DIR / "job_matching_results.json"

    with open(output_file, "w", encoding="utf-8") as f:

        json.dump(
            final_output,
            f,
            indent=4
        )

    print("\nResults Saved")

    print(output_file)

    print()

    print(json.dumps(final_output, indent=4))


if __name__ == "__main__":
    main()