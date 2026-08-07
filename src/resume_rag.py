"""
Resume RAG Pipeline

Loads resumes, chunks them,
creates embeddings and stores
them in ChromaDB.
"""

from file_loader import ResumeLoader
from chunker import DocumentChunker
from vector_store import VectorStoreManager


def main():

    print("=" * 80)
    print("Resume RAG Pipeline")
    print("=" * 80)

    # -------------------------------------------------------
    # Load Resumes
    # -------------------------------------------------------

    loader = ResumeLoader()

    documents = loader.load_documents()

    print(f"Loaded {len(documents)} pages.")

    # -------------------------------------------------------
    # Chunk Documents
    # -------------------------------------------------------

    chunker = DocumentChunker()

    chunks = chunker.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # -------------------------------------------------------
    # Build ChromaDB
    # -------------------------------------------------------

    vector_manager = VectorStoreManager()

    vector_manager.create_vector_store(chunks)

    print(f"Indexed {vector_manager.document_count()} chunks.")

    print()

    print("Vector Database Successfully Created.")

    print("=" * 80)


if __name__ == "__main__":
    main()