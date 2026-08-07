# Project Execution Guide

This guide explains how to execute the **RAG-Based Resume Profile Matching System** using both available approaches.

The project supports two execution methods:

1. **Jupyter Notebook** – Step-by-step implementation with explanations and intermediate outputs.
2. **Python Source Code** – Modular implementation suitable for end-to-end execution.

Before running the project, ensure you have completed the setup described in **[SETUP.md](SETUP.md)**.

# Execution Methods

| Method | Description | Recommended For |
|----------|-------------|-----------------|
| Method 1 | Jupyter Notebook | Learning, Demonstration, Experimentation |
| Method 2 | Python Source Code | End-to-End Project Execution |

# Method 1 – Execute Using Jupyter Notebook

The notebook contains the complete implementation of the Resume Matching pipeline along with detailed markdown explanations and intermediate outputs.

Location:

```text
notebook/
└── Resume_RAG.ipynb
```

## Step 1 – Launch Jupyter Notebook

From the project root directory, run:

```bash
jupyter notebook
```

## Step 2 – Open the Notebook

Open:

```text
Resume_RAG.ipynb
```

## Step 3 – Run All Cells Sequentially

Execute every notebook cell from top to bottom.

The notebook performs the following operations:

```text
Load Resume PDFs
        │
        ▼
Document Chunking
        │
        ▼
Embedding Generation
        │
        ▼
ChromaDB Creation
        │
        ▼
Metadata Extraction
        │
        ▼
Read Job Description
        │
        ▼
Semantic Search
        │
        ▼
Hybrid Search
        │
        ▼
Candidate Ranking
        │
        ▼
AI Match Reasoning
        │
        ▼
JSON Output
```

## Notebook Features

The notebook demonstrates:

- Resume Loading
- PDF Parsing
- Chunk Generation
- Embedding Creation
- ChromaDB Storage
- Metadata Extraction
- Semantic Search
- Hybrid Search
- Candidate Ranking
- Match Reasoning
- JSON Generation

It also displays intermediate outputs after every major step for easier understanding.

# Method 2 – Execute Using Python Source Code

The modular implementation separates each stage of the RAG pipeline into reusable source files.

Navigate to the source directory:

```bash
cd src
```

The execution consists of two phases.


# Phase 1 – Build the Vector Database

Run:

```bash
python resume_rag.py
```

## What Happens?

The script performs the following operations:

```text
Load Resume PDFs
        │
        ▼
Read PDF Pages
        │
        ▼
Split Documents into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Create ChromaDB
        │
        ▼
Persist Vector Database
```

## Expected Console Output

```text
================================================================================
Resume RAG Pipeline
================================================================================

Loaded 120 pages.

Created 356 chunks.

Indexed 356 chunks.

Vector Database Successfully Created.
```

# Phase 2 – Run the Job Matching Engine

After building the vector database, execute:

```bash
python job_matcher.py
```

# Select a Job Description

The application automatically scans the following directory:

```text
data/job_descriptions/
```

Example:

```text
Available Job Descriptions

1. jd_ai_product_manager

2. jd_data_scientist

3. jd_ml_engineer

4. Enter Custom Job Description
```

## Option 1 – Use an Existing Job Description

Enter the corresponding number.

Example:

```text
Select Option: 2
```

The application loads:

```text
data/job_descriptions/jd_data_scientist.txt
```

## Option 2 – Enter a Custom Job Description

Select:

```text
4
```

Paste your own Job Description.

Example:

```text
Looking for a Machine Learning Engineer with experience in

Python

Machine Learning

TensorFlow

Docker

AWS

SQL
```

Press **Enter** twice to finish.

# Job Matching Workflow

After selecting the Job Description, the system performs:

```text
Read Job Description
        │
        ▼
Load ChromaDB
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
Candidate Aggregation
        │
        ▼
Candidate Ranking
        │
        ▼
Calculate Match Score
        │
        ▼
Generate AI Reasoning
        │
        ▼
Generate JSON Output
```

# Generated Output

The results are automatically saved to:

```text
outputs/
└── job_matching_results.json
```

Example:

```json
{
    "job_description": "...",
    "top_matches": [
        {
            "candidate_name": "John Doe",
            "resume_path": "data/resumes/john_doe.pdf",
            "match_score": 94.8,
            "matched_skills": [
                "Python",
                "Machine Learning",
                "Docker"
            ],
            "relevant_excerpts": [
                "...",
                "..."
            ],
            "reasoning": "Strong candidate with relevant Machine Learning and cloud experience."
        }
    ]
}
```

# Complete Execution Flow

```text
Method 1

Resume_RAG.ipynb
        │
        ▼
Run Notebook Cells
        │
        ▼
Observe Intermediate Outputs
        │
        ▼
Generate Final Results

──────────────────────────────────────────────────────────────

Method 2

python resume_rag.py
        │
        ▼
Build ChromaDB
        │
        ▼
python job_matcher.py
        │
        ▼
Select Job Description
        │
        ▼
Hybrid Resume Matching
        │
        ▼
Generate JSON Output
```

# Execution Summary

| Step | Script | Purpose |
|------|--------|----------|
| 1 | `resume_rag.py` | Loads resumes, generates embeddings, and builds the ChromaDB vector database. |
| 2 | `job_matcher.py` | Reads the Job Description, retrieves matching resumes, ranks candidates, generates reasoning, and exports the results. |


# Next Documentation

For a detailed explanation of the repository layout and each source file, refer to:

➡️ **[Project Structure](PROJECT_STRUCTURE.md)**