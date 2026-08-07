# Project Structure

This document describes the complete repository structure and explains the purpose and responsibility of every folder and source file in the project.

# Repository Structure

```text
RAG-Based-Profile-Matching/
│
├── README.md
├── requirements.txt
├── .env
│
├── notebook/
│   └── Resume_RAG.ipynb
│
├── docs/
│   ├── INSTALLATION.md
│   ├── SETUP.md
│   ├── EXECUTION.md
│   ├── PROJECT_STRUCTURE.md
│   ├── WORKFLOW.md
│   └── ARCHITECTURE.md
│
├── data/
│   ├── resumes/
│   └── job_descriptions/
│
├── chroma_db/
│
├── outputs/
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── file_loader.py
    ├── chunker.py
    ├── vector_store.py
    ├── metadata_extractor.py
    ├── hybrid_search.py
    ├── scoring.py
    ├── reasoning.py
    ├── resume_rag.py
    ├── job_matcher.py
    ├── utils.py
    └── test.py
```
# Directory Overview

| Directory | Purpose |
|-----------|---------|
| notebook | Jupyter Notebook implementation with detailed explanations |
| docs | Complete project documentation |
| data | Resume PDFs and Job Description files |
| chroma_db | Persistent ChromaDB vector database |
| outputs | Generated JSON output |
| src | Complete source code implementation |

# Source Code Architecture

Each module performs one independent responsibility, making the project modular, reusable, and easy to maintain.

## __init__.py

### Purpose

Marks the **src** directory as a Python package.

### Responsibilities

- Initializes the package
- Enables module imports
- Stores package metadata (optional)

### Used By

All Python modules.

## config.py

### Purpose

Central configuration module of the project.

### Responsibilities

- Load environment variables
- Initialize OpenRouter LLM
- Initialize Embedding Model
- Read ChromaDB configuration
- Configure chunk size
- Configure chunk overlap
- Store project directory paths

### Inputs

```
.env
```

### Outputs

- LLM Instance
- Embedding Model
- Configuration Variables

### Imported By

Almost every module.

## file_loader.py

### Purpose

Loads all resume PDF files from the dataset.

### Responsibilities

- Scan the resume directory
- Load PDF files
- Extract text using PyPDFLoader
- Convert resumes into LangChain Documents
- Attach metadata

### Input

```text
data/resumes/
```

### Output

```python
List[Document]
```

### Metadata Added

- Resume Name
- Resume Path
- Page Number

## chunker.py

### Purpose

Splits resume documents into smaller chunks for embedding generation.

### Responsibilities

- Initialize RecursiveCharacterTextSplitter
- Split documents
- Preserve metadata
- Return chunked documents

### Input

```python
LangChain Documents
```

### Output

```python
Chunked Documents
```

### Configuration

- Chunk Size
- Chunk Overlap

## vector_store.py

### Purpose

Creates and manages the ChromaDB vector database.

### Responsibilities

- Generate embeddings
- Create ChromaDB
- Persist vector database
- Load existing vector database
- Perform semantic similarity search

### Input

```python
Chunked Documents
```

### Output

- ChromaDB
- Retriever
- Semantic Search Results

## metadata_extractor.py

### Purpose

Extracts structured candidate information using the LLM.

### Responsibilities

- Extract Candidate Name
- Extract Skills
- Extract Experience
- Extract Education
- Return structured metadata

### Input

Resume Text

### Output

```json
{
    "candidate_name": "",
    "skills": [],
    "experience_years": 0,
    "education": ""
}
```

### LLM Used

OpenRouter GPT-4o Mini

## hybrid_search.py

### Purpose

Implements the Hybrid Search strategy.

### Responsibilities

- Semantic Search
- BM25 Keyword Search
- Merge search results
- Aggregate candidate information

### Input

Job Description

### Output

Candidate Dictionary

### Search Techniques

- Semantic Search (ChromaDB)
- BM25 Search
- Hybrid Search

## scoring.py

### Purpose

Ranks retrieved candidates.

### Responsibilities

- Normalize search scores
- Calculate weighted score
- Rank candidates
- Generate match score (0–100)

### Scoring Formula

```text
Final Score = 60% Semantic Score + 40% BM25 Score
```

### Output

Ranked Candidate DataFrame

## reasoning.py

### Purpose

Generates AI-powered explanations for candidate matching.

### Responsibilities

- Compare Resume
- Compare Job Description
- Identify Matching Skills
- Identify Missing Skills
- Generate Recruiter-friendly Reasoning

### Input

- Resume
- Job Description

### Output

```json
{
    "matched_skills": [],
    "missing_skills": [],
    "reasoning": ""
}
```

### LLM Used

OpenRouter GPT-4o Mini

## resume_rag.py

### Purpose

Main entry point for building the RAG pipeline.

### Responsibilities

- Load resumes
- Chunk documents
- Generate embeddings
- Create ChromaDB
- Persist vector database

### Execution

```bash
python resume_rag.py
```

### Output

Persistent ChromaDB Vector Database

## job_matcher.py

### Purpose

Main entry point for candidate matching.

### Responsibilities

- Load Job Description
- Load ChromaDB
- Perform Semantic Search
- Perform BM25 Search
- Execute Hybrid Search
- Rank Candidates
- Generate Match Reasoning
- Export JSON Results

### Execution

```bash
python job_matcher.py
```

### Output

```text
outputs/job_matching_results.json
```

## utils.py

### Purpose

Contains reusable helper functions used across the project.

### Typical Functions

- Save JSON
- Read Job Description
- Clean LLM Responses
- Utility Functions

## test.py

### Purpose

Integration testing.

### Responsibilities

Tests the complete pipeline by executing:

- Resume Loading
- Document Chunking
- ChromaDB Creation
- Semantic Search
- Hybrid Search
- Candidate Ranking
- Metadata Extraction
- AI Match Reasoning

This file is intended only for development and debugging.

# Data Directory

## resumes/

Stores all candidate resumes.

Example:

```text
john_doe.pdf

alice_smith.pdf

david_lee.pdf
```

## job_descriptions/

Stores all sample Job Descriptions.

Example:

```text
jd_data_scientist.txt

jd_ml_engineer.txt

jd_ai_product_manager.txt
```

The application automatically detects every `.txt` file in this directory.

# Output Directory

Generated matching results are stored inside:

```text
outputs/
└── job_matching_results.json
```

# ChromaDB Directory

The vector database is automatically generated after executing:

```bash
python resume_rag.py
```

Stored inside:

```text
chroma_db/
```

# Module Dependency Flow

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
      │
      ▼
job_matching_results.json
```

# Next Documentation

For a detailed explanation of the complete Resume Matching pipeline, refer to:

➡️ **[Workflow](WORKFLOW.md)**