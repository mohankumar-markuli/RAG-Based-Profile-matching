"""
Handles Chroma Vector Database operations.
"""

from typing import List, Tuple

from langchain_core.documents import Document
from langchain_chroma import Chroma

from config import (
    embedding_model,
    VECTOR_STORE_DIR,
    TOP_K
)


class VectorStoreManager:
    """
    Handles vector database operations.
    """

    def __init__(self):

        self.vector_store = None

    def create_vector_store(
        self,
        documents: List[Document]
    ) -> Chroma:
        """
        Creates a new Chroma vector database.
        """

        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embedding_model,
            persist_directory=str(VECTOR_STORE_DIR)
        )

        return self.vector_store

    def load_vector_store(self) -> Chroma:
        """
        Loads an existing Chroma database.
        """

        self.vector_store = Chroma(
            persist_directory=str(VECTOR_STORE_DIR),
            embedding_function=embedding_model
        )

        return self.vector_store

    def get_retriever(
        self,
        top_k: int = TOP_K
    ):

        return self.vector_store.as_retriever(
            search_kwargs={"k": top_k}
        )

    def similarity_search(
        self,
        query: str,
        top_k: int = TOP_K
    ) -> List[Tuple[Document, float]]:
        """
        Returns semantic search results with similarity scores.
        """

        return self.vector_store.similarity_search_with_score(
            query=query,
            k=top_k
        )

    def document_count(self):

        return self.vector_store._collection.count()