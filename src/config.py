"""
Project Configuration

Loads environment variables, initializes AI models,
and defines all project-wide paths and constants.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from langchain_openrouter import ChatOpenRouter
from langchain_huggingface import HuggingFaceEmbeddings

# ============================================================
# Load Environment Variables
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# ============================================================
# API Keys
# ============================================================

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

# ============================================================
# Models
# ============================================================

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "openai/gpt-4o-mini"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

# ============================================================
# Document Processing
# ============================================================

CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", 1000)
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", 200)
)

# ============================================================
# Directories
# ============================================================

DATA_DIR = BASE_DIR / "data"

RESUME_DIR = DATA_DIR / "resumes"

JOB_DESCRIPTION_DIR = DATA_DIR / "job_descriptions"

OUTPUT_DIR = BASE_DIR / "outputs"

VECTOR_STORE_DIR = BASE_DIR / os.getenv(
    "VECTOR_STORE_DIR",
    "data/chroma_db"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

VECTOR_STORE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# Embedding Model
# ============================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ============================================================
# LLM
# ============================================================

llm = ChatOpenRouter(
    model=LLM_MODEL,
    api_key=OPENROUTER_API_KEY,
    temperature=0.2,
    max_tokens=150
)

# ============================================================
# Retrieval
# ============================================================

TOP_K = 10