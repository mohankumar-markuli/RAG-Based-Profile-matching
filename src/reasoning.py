"""
Generates recruiter-friendly reasoning for candidate matches.
"""

import json

from langchain_core.prompts import ChatPromptTemplate

from config import llm


class CandidateReasoner:

    def __init__(self):

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an expert Technical Recruiter.

Analyze the candidate resume against the given Job Description.

Job Description:
{job_description}

Candidate Resume:
{resume}

Return ONLY valid JSON in the following format:

{{
    "matched_skills": [],
    "missing_skills": [],
    "reasoning": ""
}}
"""
        )

    def generate_reasoning(
        self,
        job_description,
        resume_text
    ):

        messages = self.prompt.format_messages(
            job_description=job_description,
            resume=resume_text
        )

        response = llm.invoke(messages)

        response_text = (
            response.content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:

            return json.loads(response_text)

        except Exception:

            return {

                "matched_skills": [],

                "missing_skills": [],

                "reasoning": response.content

            }