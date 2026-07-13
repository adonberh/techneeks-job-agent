def call_llm(
    prompt: str,
    mock_mode: bool = True,
) -> str:
    if mock_mode:
        return mock_response()

    raise NotImplementedError(
        "Live LLM mode is not configured."
    )


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