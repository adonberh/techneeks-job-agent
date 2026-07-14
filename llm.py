import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def call_llm(
    prompt: str,
    mock_mode: bool = True,
) -> str:
    if mock_mode:
        return mock_response()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not configured."
        )

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text


def mock_response() -> str:
    return """
Role Summary:
Build AI-enabled internal software tools.

Company:
ExampleTech

Role:
Junior AI Engineer

Candidate Match Analysis:
The candidate has useful Python and API experience.

Match Score:
78

CV Suggestions:
Emphasise practical projects and measurable outcomes.

Cover Letter:
Dear Hiring Team,

I am interested in this role because it combines software engineering and practical AI.

Best regards,
Candidate

Next Action:
Review the application and apply within 48 hours.
"""
