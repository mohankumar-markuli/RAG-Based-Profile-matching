# Installation Guide

This guide explains how to install the **RAG-Based Resume Profile Matching System** on your local machine.


# System Requirements

Before installing the project, ensure your system meets the following requirements.

| Software | Version |
|----------|----------|
| Python | 3.11 or above |
| Git | Latest Version |
| Visual Studio Code (Recommended) | Latest |
| Jupyter Notebook | Latest |
| OpenRouter API Key | Required |

# Clone the Repository

Clone the GitHub repository.

```bash
git clone https://github.com/<your-username>/RAG-Based-Profile-Matching.git
```

Navigate to the project directory.

```bash
cd RAG-Based-Profile-Matching
```


# Create a Virtual Environment

Creating a virtual environment keeps the project dependencies isolated from your global Python installation.

### Windows

```bash
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

# Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

After activation, your terminal should display something similar to:

```text
(venv)
```


# Upgrade pip (Optional)

It is recommended to update **pip** before installing the project dependencies.

```bash
python -m pip install --upgrade pip
```


# Install Project Dependencies

Install all required libraries using the provided **requirements.txt** file.

```bash
pip install -r requirements.txt
```

This installs all required libraries, including:

- LangChain
- LangChain Community
- LangChain HuggingFace
- ChromaDB
- Sentence Transformers
- Rank BM25
- PyMuPDF
- Python Dotenv
- Pandas
- NumPy
- tqdm
- Jupyter Notebook



# Verify Installation

Verify your Python installation.

```bash
python --version
```

Example:

```text
Python 3.11.9
```



Verify that the required packages have been installed.

```bash
pip list
```

You should see packages similar to:

```text
chromadb

langchain

langchain-community

langchain-huggingface

langchain-text-splitters

sentence-transformers

rank-bm25

pymupdf

pandas

numpy

python-dotenv
```

# Verify the Project Structure

After cloning the repository, your project should resemble the following structure:

```text
RAG-Based-Profile-Matching/
│
├── README.md
├── requirements.txt
├── .env
│
├── notebook/
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

# Next Step

Once the installation is complete, proceed to the project configuration guide.

➡️ **[Project Setup Guide](SETUP.md)**