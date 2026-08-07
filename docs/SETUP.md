# Project Setup Guide

This guide explains how to configure the **RAG-Based Resume Profile Matching System** after completing the installation.

Before proceeding, ensure you have completed the installation steps described in **[INSTALLATION.md](INSTALLATION.md)**.

# Configure Environment Variables

The project uses a **.env** file to store API keys and configuration values.

Create a file named:

```text
.env
```

in the project root directory.

Example:

```env
# ============================================================
# OpenRouter Configuration
# ============================================================

OPENROUTER_API_KEY=your_openrouter_api_key

LLM_MODEL=openai/gpt-4o-mini

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# ============================================================
# Vector Database Configuration
# ============================================================

VECTOR_STORE_DIR=./chroma_db

# ============================================================
# Document Processing Configuration
# ============================================================

CHUNK_SIZE=1000

CHUNK_OVERLAP=200
```

# Environment Variable Description

| Variable | Description |
|----------|-------------|
| OPENROUTER_API_KEY | API key used to access OpenRouter LLMs |
| LLM_MODEL | Language model used for metadata extraction and reasoning |
| EMBEDDING_MODEL | Sentence Transformer model used to generate vector embeddings |
| VECTOR_STORE_DIR | Directory where ChromaDB stores vector embeddings |
| CHUNK_SIZE | Maximum number of characters in each document chunk |
| CHUNK_OVERLAP | Number of overlapping characters between consecutive chunks |


# Project Directory Structure

Ensure the project has the following structure before execution.

```text
RAG-Based-Profile-Matching/
│
├── .env
├── requirements.txt
├── README.md
│
├── notebook/
│   └── Resume_RAG.ipynb
│
├── docs/
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
```

# Add Resume Dataset

Copy all candidate resumes into the following directory:

```text
data/resumes/
```

Example:

```text
data/
└── resumes/
    ├── john_doe.pdf
    ├── alice_smith.pdf
    ├── david_lee.pdf
    ├── emily_davis.pdf
    └── ...
```

The system automatically loads all PDF files from this folder.

# Add Job Descriptions

Copy all Job Description files into:

```text
data/job_descriptions/
```

Example:

```text
data/
└── job_descriptions/
    ├── jd_data_scientist.txt
    ├── jd_ml_engineer.txt
    ├── jd_ai_product_manager.txt
    └── jd_backend_engineer.txt
```

The application automatically lists all available Job Descriptions during execution.

# ChromaDB Directory

The vector database will be automatically created inside:

```text
chroma_db/
```

Example:

```text
chroma_db/
├── chroma.sqlite3
├── ...
```

No manual setup is required.

# Output Directory

The generated results are automatically saved inside:

```text
outputs/
```

Example:

```text
outputs/
└── job_matching_results.json
```

If the directory does not exist, it will be created automatically.


# Verify Configuration

Verify that:

- Python environment is activated.
- `.env` file exists.
- OpenRouter API key has been added.
- Resume PDFs are available inside `data/resumes/`.
- Job Descriptions are available inside `data/job_descriptions/`.
- All required dependencies are installed.

# Configuration Checklist

| Configuration | Status |
|--------------|--------|
| Python Installed | ✅ |
| Virtual Environment Activated | ✅ |
| Dependencies Installed | ✅ |
| `.env` Configured | ✅ |
| OpenRouter API Key Added | ✅ |
| Resume Dataset Added | ✅ |
| Job Descriptions Added | ✅ |
| Project Directory Verified | ✅ |

# Ready to Execute

After completing the setup, the project is ready to run using either of the following methods:

- **Jupyter Notebook** (`notebook/Resume_RAG.ipynb`)
- **Python Source Code** (`resume_rag.py` and `job_matcher.py`)

Refer to the execution guide for detailed instructions.

➡️ **[Execution Guide](EXECUTION.md)**