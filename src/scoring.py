"""
Candidate Scoring Module

Calculates the final match score by combining:
1. Semantic Search Score
2. BM25 Keyword Score
"""

import pandas as pd


class CandidateScorer:

    def __init__(
        self,
        semantic_weight=0.6,
        bm25_weight=0.4
    ):

        self.semantic_weight = semantic_weight
        self.bm25_weight = bm25_weight

    def rank_candidates(self, candidates):

        df = pd.DataFrame(candidates.values())

        if df.empty:
            return df

        # --------------------------------------------------
        # Normalize Semantic Score
        # --------------------------------------------------

        semantic_min = df["semantic_score"].min()
        semantic_max = df["semantic_score"].max()

        df["semantic_norm"] = (
            (df["semantic_score"] - semantic_min)
            /
            (semantic_max - semantic_min + 1e-9)
        )

        # --------------------------------------------------
        # Normalize BM25 Score
        # --------------------------------------------------

        bm25_min = df["bm25_score"].min()
        bm25_max = df["bm25_score"].max()

        df["bm25_norm"] = (
            (df["bm25_score"] - bm25_min)
            /
            (bm25_max - bm25_min + 1e-9)
        )

        # --------------------------------------------------
        # Final Match Score
        # --------------------------------------------------

        df["match_score"] = (

            self.semantic_weight * df["semantic_norm"]

            +

            self.bm25_weight * df["bm25_norm"]

        ) * 100

        df["match_score"] = df["match_score"].round(2)

        df = df.sort_values(
            "match_score",
            ascending=False
        ).reset_index(drop=True)

        return df