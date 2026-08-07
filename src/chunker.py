"""
Chunks LangChain Document objects into smaller overlapping chunks.
"""

from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


class DocumentChunker:
    """
    Splits resume documents into smaller chunks while preserving metadata.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:
        """
        Split documents into chunks.

        Parameters
        ----------
        documents : List[Document]

        Returns
        -------
        List[Document]
        """

        chunked_documents = self.text_splitter.split_documents(
            documents
        )

        return chunked_documents