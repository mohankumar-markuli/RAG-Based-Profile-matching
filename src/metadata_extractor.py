"""
Extract structured metadata from resumes using the LLM.
"""

import json
from typing import Dict

from langchain_core.prompts import ChatPromptTemplate

from config import llm


class MetadataExtractor:
    """
    Extract structured metadata from resume text.
    """

    def __init__(self):

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an expert HR Resume Parser.

Extract the following information from the resume.

Return ONLY valid JSON.

{{
    "candidate_name":"",
    "skills":[],
    "experience_years":0,
    "education":""
}}

Resume:

{resume}
"""
        )

    def extract_metadata(
        self,
        resume_text: str
    ) -> Dict:

        prompt = self.prompt.format_messages(
            resume=resume_text
        )

        response = llm.invoke(prompt)

        response_text = response.content.strip()

        # Remove markdown if present
        response_text = (
            response_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:

            metadata = json.loads(response_text)

        except Exception:

            metadata = {
                "candidate_name": "",
                "skills": [],
                "experience_years": 0,
                "education": ""
            }

        return metadata