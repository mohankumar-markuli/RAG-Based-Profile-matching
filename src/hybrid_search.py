"""
Hybrid Search Module

Combines:
1. Semantic Search (ChromaDB)
2. BM25 Keyword Search
"""

from collections import defaultdict

import numpy as np
from rank_bm25 import BM25Okapi

from config import TOP_K


class HybridSearch:

    def __init__(self, vector_store):

        self.vector_store = vector_store

        self.bm25 = None

        self.documents = None

    def build_bm25_index(self, chunked_documents):

        """
        Build BM25 index from all chunks.
        """

        self.documents = chunked_documents

        corpus = [
            doc.page_content.lower().split()
            for doc in chunked_documents
        ]

        self.bm25 = BM25Okapi(corpus)

    def semantic_search(
        self,
        query,
        top_k=TOP_K
    ):

        return self.vector_store.similarity_search_with_score(
            query=query,
            k=top_k
        )

    def keyword_search(
        self,
        query,
        top_k=TOP_K
    ):

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for idx in indices:

            results.append(
                (
                    self.documents[idx],
                    scores[idx]
                )
            )

        return results

    def hybrid_search(
        self,
        query,
        top_k=TOP_K
    ):

        semantic_results = self.semantic_search(
            query,
            top_k
        )

        bm25_results = self.keyword_search(
            query,
            top_k
        )

        candidates = defaultdict(
            lambda: {
                "resume_name": "",
                "resume_path": "",
                "semantic_score": 0,
                "bm25_score": 0,
                "chunks": []
            }
        )

        # Semantic Results

        for document, score in semantic_results:

            name = document.metadata["resume_name"]

            candidates[name]["resume_name"] = name

            candidates[name]["resume_path"] = document.metadata[
                "resume_path"
            ]

            candidates[name]["semantic_score"] = max(
                candidates[name]["semantic_score"],
                score
            )

            candidates[name]["chunks"].append(
                document.page_content
            )

        # BM25 Results

        for document, score in bm25_results:

            name = document.metadata["resume_name"]

            if name in candidates:

                candidates[name]["bm25_score"] = max(
                    candidates[name]["bm25_score"],
                    score
                )

        return candidates