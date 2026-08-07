# Project Workflow

This document explains the complete end-to-end workflow of the **RAG-Based Resume Profile Matching System**. It describes how resumes are processed, indexed, searched, ranked, and matched against a Job Description using Retrieval-Augmented Generation (RAG).

# Workflow Overview

The project is divided into two major phases:

- **Phase 1 – Resume Indexing (RAG Pipeline)**
- **Phase 2 – Job Matching Pipeline**

```text
                     Phase 1                           Phase 2

Resume PDFs ───────────────► ChromaDB ───────────────► Job Matching ─────────────► JSON Output
```


# Phase 1 – Resume Indexing Pipeline

The objective of this phase is to process all resumes and create a searchable vector database.

This phase is executed using:

```bash
python resume_rag.py
```


## Step 1 – Load Resume PDFs

The application scans the resume directory.

```text
data/
└── resumes/
```

Every PDF is loaded using **PyPDFLoader**.

Output:

```text
Resume PDF
        │
        ▼
LangChain Documents
```


## Step 2 – Extract Resume Text

Each PDF is converted into text while preserving page information.

Output:

```text
Resume Pages
        │
        ▼
Document Objects
```

Each document contains:

- Resume Name
- Resume Path
- Page Number
- Page Content


## Step 3 – Document Chunking

Large resume documents are divided into smaller overlapping chunks.

Configuration:

```text
Chunk Size = 1000

Chunk Overlap = 200
```

Chunking improves retrieval accuracy and embedding quality.

Output:

```text
Resume
      │
      ▼
Chunk 1

Chunk 2

Chunk 3

...
```


## Step 4 – Generate Embeddings

Every chunk is converted into a numerical vector using the embedding model.

Embedding Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Output:

```text
Text Chunk
      │
      ▼
Vector Embedding
```


## Step 5 – Store in ChromaDB

The generated embeddings are stored inside ChromaDB.

Each record contains:

- Chunk Text
- Vector Embedding
- Resume Metadata

Output:

```text
Resume Chunks
      │
      ▼
Embeddings
      │
      ▼
ChromaDB
```

At the end of this phase, the resume database is ready for semantic search.


# Phase 2 – Job Matching Pipeline

The objective of this phase is to retrieve and rank the most relevant resumes for a given Job Description.

This phase is executed using:

```bash
python job_matcher.py
```

## Step 1 – Load Job Description

The user has two options.

### Option 1

Select an existing Job Description.

```text
data/job_descriptions/
```

Example:

```text
jd_data_scientist.txt

jd_ml_engineer.txt

jd_ai_product_manager.txt
```

### Option 2

Paste a custom Job Description during execution.

## Step 2 – Semantic Search

The Job Description is converted into an embedding and compared against all resume embeddings stored in ChromaDB.

```text
Job Description
        │
        ▼
Embedding
        │
        ▼
Similarity Search
        │
        ▼
Top Matching Resume Chunks
```

## Step 3 – BM25 Keyword Search

A keyword-based search is also performed using BM25.

This helps identify resumes containing important keywords.

Example:

- Python
- Machine Learning
- SQL
- Docker
- AWS

Output:

```text
Keyword Matching Results
```

## Step 4 – Hybrid Search

Semantic Search and BM25 Search are combined to improve retrieval accuracy.

```text
Semantic Search
        │
        ├─────────────┐
        │             │
        ▼             ▼
BM25 Search      Candidate Chunks
        │             │
        └─────────────┘
              │
              ▼
        Hybrid Results
```


## Step 5 – Candidate Aggregation

Multiple chunks belonging to the same resume are grouped together.

The system combines:

- Resume Name
- Resume Path
- Semantic Score
- BM25 Score
- Retrieved Chunks

Output:

```text
Candidate Dictionary
```

## Step 6 – Candidate Ranking

The retrieved candidates are ranked using a weighted scoring approach.

Scoring Formula

```text
Match Score

=

60% Semantic Score

+

40% BM25 Score
```

The final score is normalized to a scale of **0–100**.

Output:

```text
Ranked Candidates
```

## Step 7 – Metadata Extraction

The LLM extracts structured candidate information.

Extracted fields include:

- Candidate Name
- Skills
- Years of Experience
- Education

Example:

```json
{
    "candidate_name": "John Doe",
    "skills": [
        "Python",
        "Machine Learning",
        "Docker"
    ],
    "experience_years": 6,
    "education": "M.Tech"
}
```

## Step 8 – AI Match Reasoning

The selected resume and Job Description are provided to the OpenRouter GPT-4o Mini model.

The model generates:

- Matching Skills
- Missing Skills
- Candidate Summary
- Recruiter-friendly Explanation

Example:

```json
{
    "matched_skills": [
        "Python",
        "Machine Learning"
    ],
    "missing_skills": [
        "Kubernetes"
    ],
    "reasoning": "The candidate demonstrates strong experience in Python and Machine Learning with relevant industry projects."
}
```

## Step 9 – JSON Output

The final ranked results are exported as JSON.

Example:

```json
{
    "job_description": "...",
    "top_matches": [
        {
            "candidate_name": "John Doe",
            "match_score": 94.6,
            "matched_skills": [
                "Python",
                "Machine Learning"
            ],
            "relevant_excerpts": [
                "...",
                "..."
            ],
            "reasoning": "Strong candidate with relevant Machine Learning experience."
        }
    ]
}
```

Saved to:

```text
outputs/
└── job_matching_results.json
```

# Complete End-to-End Workflow

```text
Resume PDFs
      │
      ▼
Load PDF Documents
      │
      ▼
Extract Resume Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
────────────────────────────────────────────────────────
      │
      ▼
Load Job Description
      │
      ▼
Semantic Search
      │
      ▼
BM25 Keyword Search
      │
      ▼
Hybrid Search
      │
      ▼
Aggregate Candidates
      │
      ▼
Rank Candidates
      │
      ▼
Extract Metadata
      │
      ▼
Generate AI Reasoning
      │
      ▼
Export JSON Results
```

# Execution Summary

| Phase | Script | Purpose |
|--------|--------|---------|
| Phase 1 | `resume_rag.py` | Load resumes, generate embeddings, and build the ChromaDB vector database. |
| Phase 2 | `job_matcher.py` | Retrieve, rank, explain, and export the best matching candidates. |

# Next Documentation

To understand the system design, module interactions, and architecture in detail, refer to:

➡️ **[Architecture](ARCHITECTURE.md)**