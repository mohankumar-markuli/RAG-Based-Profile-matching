# RAG-Based Resume Profile Matching System

A **Retrieval-Augmented Generation (RAG)** based Resume Profile Matching System that intelligently matches candidate resumes with job descriptions using **Semantic Search**, **Hybrid Search (Semantic + BM25)**, **Large Language Models (LLMs)**, and **Vector Databases**.

The project indexes candidate resumes into **ChromaDB**, retrieves the most relevant resumes for a given Job Description (JD), ranks candidates using semantic similarity and keyword matching, generates AI-powered reasoning for each candidate, and exports the results as structured JSON.

## Project Objectives

This project demonstrates how Retrieval-Augmented Generation (RAG) can be applied to automate resume screening and candidate matching.

The system performs:

- Resume PDF Processing
- Intelligent Document Chunking
- Embedding Generation
- ChromaDB Vector Database Creation
- Metadata Extraction
- Semantic Search
- Hybrid Search (Semantic + BM25)
- Candidate Ranking
- AI-powered Match Reasoning
- JSON Output Generation


## Part A – RAG System Setup

- Resume Loading
- Intelligent Chunking
- Embedding Generation
- ChromaDB Vector Database
- Metadata Extraction
- Persistent Vector Store

## Part B – Job Matching Engine

- Semantic Search
- Hybrid Search
- Top-K Resume Retrieval
- Candidate Ranking
- Match Score (0–100)
- AI-generated Match Reasoning
- JSON Output

# Features

- Resume PDF Processing
- LangChain Integration
- ChromaDB Vector Database
- HuggingFace Sentence Transformer Embeddings
- OpenRouter GPT-4o Mini
- Recursive Character Text Chunking
- Semantic Search
- BM25 Keyword Search
- Hybrid Retrieval
- Candidate Match Scoring
- AI-generated Recruiter Feedback
- Structured JSON Output
- Modular Source Code
- Jupyter Notebook Implementation

# Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Framework | LangChain |
| LLM | OpenRouter GPT-4o Mini |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Database | ChromaDB |
| Keyword Search | BM25 |
| PDF Loader | PyPDFLoader |
| Chunking | RecursiveCharacterTextSplitter |
| Notebook | Jupyter Notebook |
| Output Format | JSON |

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

# Documentation

Comprehensive project documentation is available in the **docs** directory.

| Document | Description |
|----------|-------------|
| 📥 [Installation Guide](docs/INSTALLATION.md) | Install Python, create a virtual environment, and install project dependencies. |
| ⚙️ [Project Setup](docs/SETUP.md) | Configure the `.env` file, organize the dataset, and prepare the project for execution. |
| ▶️ [Execution Guide](docs/EXECUTION.md) | Run the project using either the Jupyter Notebook or the modular Python source code. |
| 📁 [Project Structure](docs/PROJECT_STRUCTURE.md) | Understand the repository layout and the responsibility of every source file. |
| 🔄 [Workflow](docs/WORKFLOW.md) | Learn the end-to-end RAG workflow, from resume ingestion to candidate ranking and JSON output. |
| 🏗️ [Architecture](docs/ARCHITECTURE.md) | Explore the system architecture, module interactions, and complete processing pipeline. |

# Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/mohankumar-markuli/RAG-Based-Profile-Matching.git

cd RAG-Based-Profile-Matching
```

## 2. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
python3 -m venv venv
```

## 3. Activate the Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```


## 5. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENROUTER_API_KEY=your_openrouter_api_key

LLM_MODEL=openai/gpt-4o-mini

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

VECTOR_STORE_DIR=./chroma_db

CHUNK_SIZE=1000

CHUNK_OVERLAP=200
```

## 6. Add Resume PDFs

Copy all resumes into

```text
data/resumes/
```

## 7. Add Job Descriptions

Copy all Job Descriptions into

```text
data/job_descriptions/
```

# Running the Project

The project can be executed in two ways.


## Method 1 — Jupyter Notebook

Open

```text
notebook/Resume_RAG.ipynb
```

Launch Jupyter Notebook.

```bash
jupyter notebook
```

Run every notebook cell sequentially.

The notebook demonstrates the complete RAG pipeline with intermediate outputs and explanations.

## Method 2 — Source Code

### Step 1 — Build the Vector Database

Navigate to the source folder.

```bash
cd src
```

Run

```bash
python resume_rag.py
```

This performs:

- Resume Loading
- Document Chunking
- Embedding Generation
- ChromaDB Creation
- Vector Database Persistence

---

### Step 2 — Match Candidates

Run

```bash
python job_matcher.py
```

The application allows you to:

- Select an existing Job Description from `data/job_descriptions/`
- OR
- Paste a custom Job Description

The system then performs:

- Semantic Search
- BM25 Keyword Search
- Hybrid Search
- Candidate Ranking
- Match Reasoning
- JSON Output Generation


# Output

The generated results are stored in

```text
outputs/
└── job_matching_results.json
```

Example

```json
{
    "job_description": "...",
    "top_matches": [
        {
            "candidate_name": "John Doe",
            "resume_path": "data/resumes/john_doe.pdf",
            "match_score": 94.6,
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
