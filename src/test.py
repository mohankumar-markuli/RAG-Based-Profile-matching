from file_loader import ResumeLoader
from chunker import DocumentChunker
from vector_store import VectorStoreManager
from hybrid_search import HybridSearch
from scoring import CandidateScorer

# ============================================================
# Load Resume Documents
# ============================================================

loader = ResumeLoader()
documents = loader.load_documents()

print(f"Loaded {len(documents)} pages.")

# ============================================================
# Chunk Documents
# ============================================================

chunker = DocumentChunker()
chunks = chunker.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

# ============================================================
# Create Vector Store
# ============================================================

vector_manager = VectorStoreManager()
vector_store = vector_manager.create_vector_store(chunks)

print("Vector Store Created.")

# ============================================================
# Hybrid Search
# ============================================================

hybrid = HybridSearch(vector_store)

hybrid.build_bm25_index(chunks)

job_description = """
Looking for a Python Machine Learning Engineer
with experience in NLP, Deep Learning,
Docker and AWS.
"""

results = hybrid.hybrid_search(job_description)

print(f"Candidates Retrieved: {len(results)}")

# ============================================================
# Candidate Ranking
# ============================================================

scorer = CandidateScorer()

ranking_df = scorer.rank_candidates(results)

print(ranking_df[
    [
        "resume_name",
        "semantic_score",
        "bm25_score",
        "match_score"
    ]
])