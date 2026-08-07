# System Architecture

This document describes the architecture of the **RAG-Based Resume Profile Matching System**, including its major components, data flow, module interactions, and the Retrieval-Augmented Generation (RAG) pipeline.


# Architecture Overview

The system follows a modular architecture where each component has a single responsibility.

The architecture consists of four major layers:

1. Document Processing Layer
2. Vector Database Layer
3. Retrieval Layer
4. AI Reasoning Layer

```text
                   +--------------------------------+
                   |        Resume PDFs             |
                   +---------------+----------------+
                                   |
                                   v
                    +------------------------------+
                    |       file_loader.py         |
                    +------------------------------+
                                   |
                                   v
                    +------------------------------+
                    |         chunker.py           |
                    +------------------------------+
                                   |
                                   v
                    +------------------------------+
                    |     Embedding Generation     |
                    +------------------------------+
                                   |
                                   v
                    +------------------------------+
                    |      vector_store.py         |
                    +------------------------------+
                                   |
                                   v
                         +------------------+
                         |    ChromaDB      |
                         +------------------+
                                   |
                     ──────────────┼────────────────
                                   |
                                   v
                        Job Description
                                   |
                                   v
                    +------------------------------+
                    |      hybrid_search.py        |
                    +------------------------------+
                                   |
                                   v
                    +------------------------------+
                    |        scoring.py            |
                    +------------------------------+
                                   |
                                   v
                    +------------------------------+
                    |       reasoning.py           |
                    +------------------------------+
                                   |
                                   v
                    +------------------------------+
                    |      job_matcher.py          |
                    +------------------------------+
                                   |
                                   v
                     job_matching_results.json
```

# High-Level Architecture

```text
                        User
                          │
                          ▼
                 Select Job Description
                          │
                          ▼
                Resume Matching Engine
                          │
        ┌─────────────────┼──────────────────┐
        │                 │                  │
        ▼                 ▼                  ▼
 Resume Loader      ChromaDB Search      BM25 Search
        │                 │                  │
        └─────────────────┼──────────────────┘
                          │
                          ▼
                   Hybrid Search Engine
                          │
                          ▼
                  Candidate Ranking
                          │
                          ▼
                    OpenRouter LLM
                          │
                          ▼
                  JSON Result Output
```

# Layer 1 – Document Processing

The Document Processing Layer converts raw PDF resumes into searchable text chunks.

Components:

- file_loader.py
- chunker.py

Workflow:

```text
Resume PDF
      │
      ▼
PyPDFLoader
      │
      ▼
Extract Resume Text
      │
      ▼
LangChain Documents
      │
      ▼
RecursiveCharacterTextSplitter
      │
      ▼
Resume Chunks
```

Responsibilities:

- Read PDF resumes
- Extract text
- Preserve metadata
- Split large documents into chunks

# Layer 2 – Embedding & Vector Storage

The embedding layer converts every text chunk into numerical vectors.

Component:

- vector_store.py

Embedding Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Workflow:

```text
Resume Chunk
      │
      ▼
Embedding Model
      │
      ▼
Vector Embedding
      │
      ▼
ChromaDB
```

Responsibilities:

- Generate embeddings
- Create vector database
- Persist embeddings
- Load existing database

# Layer 3 – Retrieval Layer

The retrieval layer finds the most relevant resumes for a Job Description.

Component:

- hybrid_search.py

The project combines two retrieval techniques.

## Semantic Search

Uses ChromaDB to compare vector similarity.

```text
Job Description
      │
      ▼
Embedding
      │
      ▼
Vector Similarity Search
      │
      ▼
Relevant Resume Chunks
```

## Keyword Search

Uses BM25 to identify exact keyword matches.

Example keywords:

- Python
- Machine Learning
- SQL
- Docker
- AWS

Workflow:

```text
Job Description
      │
      ▼
Tokenization
      │
      ▼
BM25 Ranking
```

## Hybrid Search

Semantic Search and BM25 results are merged.

```text
Semantic Search
      │
      ├──────────────┐
      │              │
      ▼              ▼
BM25 Search      Candidate Chunks
      │              │
      └──────────────┘
             │
             ▼
      Hybrid Search Results
```

Advantages:

- Better recall
- Better precision
- Improved candidate ranking

# Layer 4 – Candidate Ranking

Component:

- scoring.py

The retrieved candidates are ranked using a weighted score.

Formula:

```text
Match Score = 60% Semantic Score + 40% BM25 Score
```

Output:

```text
Candidate Ranking

↓

Top Candidates
```


# Layer 5 – AI Reasoning

Component:

- reasoning.py

The OpenRouter GPT-4o Mini model analyzes:

- Job Description
- Resume

and generates:

- Matching Skills
- Missing Skills
- Recruiter Summary
- Match Reasoning

Workflow:

```text
Resume + Job Description

↓

GPT-4o Mini

↓

Reasoning
```

# Metadata Extraction

Component:

- metadata_extractor.py

The LLM extracts structured information.

Output:

```json
{
    "candidate_name": "John Doe",
    "skills": [
        "Python",
        "Machine Learning"
    ],
    "experience_years": 5,
    "education": "M.Tech"
}
```


# Source Code Interaction

```text
config.py
      │
      ▼
file_loader.py
      │
      ▼
chunker.py
      │
      ▼
vector_store.py
      │
      ▼
ChromaDB
      │
      ▼
hybrid_search.py
      │
      ▼
scoring.py
      │
      ▼
reasoning.py
      │
      ▼
job_matcher.py
```

# Execution Architecture

## Phase 1 – Build the Vector Database

```text
resume_rag.py

↓

Load Resumes

↓

Chunk Documents

↓

Generate Embeddings

↓

Create ChromaDB

↓

Persist Database
```

## Phase 2 – Candidate Matching

```text
job_matcher.py

↓

Read Job Description

↓

Load ChromaDB

↓

Hybrid Search

↓

Candidate Ranking

↓

Generate AI Reasoning

↓

Export JSON
```


# Data Flow Diagram

```text
Resume PDFs
      │
      ▼
Load Documents
      │
      ▼
Chunk Documents
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
──────────────────────────────────────────────
      │
      ▼
Read Job Description
      │
      ▼
Semantic Search
      │
      ▼
BM25 Search
      │
      ▼
Hybrid Search
      │
      ▼
Rank Candidates
      │
      ▼
Generate AI Reasoning
      │
      ▼
Generate JSON Output
```

---

# Design Principles

The project follows the following software design principles:

- **Modular Design** – Each module has a single responsibility.
- **Separation of Concerns** – Loading, chunking, retrieval, ranking, and reasoning are implemented independently.
- **Reusable Components** – Modules can be reused independently in future projects.
- **Configurable Architecture** – API keys, models, chunk sizes, and vector database locations are managed using environment variables.
- **Extensible Design** – Additional embedding models, vector databases, or retrieval strategies can be integrated with minimal changes.


# Technology Architecture

| Layer | Technology |
|--------|------------|
| Language | Python |
| Framework | LangChain |
| LLM | OpenRouter GPT-4o Mini |
| Embedding Model | Sentence Transformers |
| Vector Database | ChromaDB |
| Keyword Retrieval | BM25 |
| Document Loader | PyPDFLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| Output | JSON |


# Architecture Summary

The architecture is designed around the Retrieval-Augmented Generation (RAG) paradigm.

The workflow consists of:

1. Processing resumes into searchable chunks.
2. Generating embeddings for semantic retrieval.
3. Storing embeddings in ChromaDB.
4. Retrieving relevant resume chunks using Hybrid Search.
5. Ranking candidates based on semantic and keyword relevance.
6. Generating AI-powered reasoning using GPT-4o Mini.
7. Exporting structured JSON results for recruiters.

This modular architecture makes the project easy to understand, maintain, extend, and deploy in future applications.