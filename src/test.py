from file_loader import ResumeLoader
from chunker import DocumentChunker
from vector_store import VectorStoreManager

loader = ResumeLoader()

documents = loader.load_documents()

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

vector_db = VectorStoreManager()

vector_db.create_vector_store(chunks)

print(f"Indexed Chunks : {vector_db.document_count()}")