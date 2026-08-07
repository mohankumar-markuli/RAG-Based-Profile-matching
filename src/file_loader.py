"""
Loads all resume PDF files from the configured directory.
"""

from pathlib import Path
from typing import List

from tqdm import tqdm
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from config import RESUME_DIR


class ResumeLoader:
    """
    Loads all resumes from the resume directory.
    """

    def __init__(self, resume_dir: Path = RESUME_DIR):
        self.resume_dir = resume_dir

    def get_resume_files(self) -> List[Path]:
        """
        Returns all PDF files present in the resume directory.
        """

        resume_files = sorted(self.resume_dir.glob("*.pdf"))

        if not resume_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.resume_dir}"
            )

        return resume_files

    def load_documents(self) -> List[Document]:
        """
        Loads all resumes as LangChain Document objects.
        """

        all_documents = []

        resume_files = self.get_resume_files()

        for resume_path in tqdm(
            resume_files,
            desc="Loading Resumes"
        ):

            loader = PyPDFLoader(str(resume_path))

            documents = loader.load()

            for document in documents:

                document.metadata["resume_name"] = resume_path.stem

                document.metadata["resume_path"] = str(resume_path)

            all_documents.extend(documents)

        return all_documents