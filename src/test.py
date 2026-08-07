from file_loader import ResumeLoader
from chunker import DocumentChunker
from vector_store import VectorStoreManager
from hybrid_search import HybridSearch

loader = ResumeLoader()

documents = loader.load_documents()

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

vector_db = VectorStoreManager()

vector_store = vector_db.create_vector_store(chunks)

hybrid = HybridSearch(vector_store)

hybrid.build_bm25_index(chunks)

results = hybrid.hybrid_search(
    "Python Machine Learning Engineer"
)

print(results)