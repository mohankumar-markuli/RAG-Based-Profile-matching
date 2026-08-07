"""
Integration Test for Resume RAG Pipeline
"""

from file_loader import ResumeLoader
from chunker import DocumentChunker
from vector_store import VectorStoreManager
from hybrid_search import HybridSearch
from scoring import CandidateScorer
from metadata_extractor import MetadataExtractor
from reasoning import CandidateReasoner


# ============================================================
# Step 1: Load Resume Documents
# ============================================================

print("=" * 80)
print("Loading Resume Documents")
print("=" * 80)

loader = ResumeLoader()
documents = loader.load_documents()

print(f"Loaded {len(documents)} pages.\n")


# ============================================================
# Step 2: Chunk Documents
# ============================================================

print("=" * 80)
print("Chunking Documents")
print("=" * 80)

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

print(f"Created {len(chunks)} chunks.\n")


# ============================================================
# Step 3: Create Chroma Vector Store
# ============================================================

print("=" * 80)
print("Creating Vector Store")
print("=" * 80)

vector_manager = VectorStoreManager()

vector_store = vector_manager.create_vector_store(chunks)

print(f"Indexed {vector_manager.document_count()} chunks.\n")


# ============================================================
# Step 4: Hybrid Search
# ============================================================

print("=" * 80)
print("Hybrid Search")
print("=" * 80)

hybrid = HybridSearch(vector_store)

hybrid.build_bm25_index(chunks)

job_description = """
Looking for a Python Machine Learning Engineer
with experience in NLP, Deep Learning,
Docker, AWS and SQL.
"""

results = hybrid.hybrid_search(job_description)

print(f"Candidates Retrieved : {len(results)}\n")


# ============================================================
# Step 5: Candidate Ranking
# ============================================================

print("=" * 80)
print("Ranking Candidates")
print("=" * 80)

scorer = CandidateScorer()

ranking_df = scorer.rank_candidates(results)

print(
    ranking_df[
        [
            "resume_name",
            "semantic_score",
            "bm25_score",
            "match_score"
        ]
    ]
)

print()


# ============================================================
# Step 6: Metadata Extraction
# ============================================================

print("=" * 80)
print("Metadata Extraction")
print("=" * 80)

extractor = MetadataExtractor()

metadata = extractor.extract_metadata(
    chunks[0].page_content
)

print(metadata)

print()


# ============================================================
# Step 7: Candidate Reasoning
# ============================================================

print("=" * 80)
print("LLM Reasoning")
print("=" * 80)

reasoner = CandidateReasoner()

top_candidate = ranking_df.iloc[0]

resume_text = "\n\n".join(top_candidate["chunks"])

reason = reasoner.generate_reasoning(
    job_description=job_description,
    resume_text=resume_text
)

print(reason)

print()

print("=" * 80)
print("Pipeline Executed Successfully")
print("=" * 80)