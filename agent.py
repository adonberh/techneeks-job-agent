from datetime import datetime

from llm import call_llm
from prompts import build_application_prompt
from stage_actions import choose_stage_action
from tools.scrape_job import scrape_job_url
from tools.tracker_csv import append_application


def run_application_agent(
    job_url: str,
    pasted_job_description: str,
    candidate_profile: str,
    stage: str,
    mock_mode: bool = True,
) -> dict:
    state = {
        "job_url": job_url,
        "candidate_profile": candidate_profile,
    }

    if job_url:
        scrape_result = scrape_job_url(job_url)

        if scrape_result["success"]:
            job_description = scrape_result["text"]
            state["job_source"] = "url"
        else:
            job_description = pasted_job_description
            state["job_source"] = "manual_paste"
    else:
        job_description = pasted_job_description
        state["job_source"] = "manual_paste"

    if not job_description:
        raise ValueError(
            "Add a job URL or paste a job description."
        )

    prompt = build_application_prompt(
        job_description=job_description,
        candidate_profile=candidate_profile,
    )

    model_output = call_llm(
        prompt,
        mock_mode=mock_mode,
    )

    result = parse_output(model_output)

    result["stage"] = stage
    result["next_action"] = choose_stage_action(stage)

    application = {
        "date_added": datetime.now().strftime("%Y-%m-%d"),
        "company": result["company"],
        "role_title": result["role_title"],
        "job_url": job_url,
        "stage": result["stage"],
        "match_score": result["match_score"],
        "next_action": result["next_action"],
    }

    append_application(application)

    return result


def parse_output(text: str) -> dict:
    return {
        "role_summary": get_section(text, "Role Summary"),
        "company": get_section(text, "Company"),
        "role_title": get_section(text, "Role"),
        "match_analysis": get_section(
            text,
            "Candidate Match Analysis",
        ),
        "match_score": get_section(
            text,
            "Match Score",
        ),
        "cv_suggestions": get_section(
            text,
            "CV Suggestions",
        ),
        "cover_letter": get_section(
            text,
            "Cover Letter",
        ),
        "next_action": get_section(
            text,
            "Next Action",
        ),
    }


def get_section(text: str, heading: str) -> str:
    headings = [
        "Role Summary",
        "Company",
        "Role",
        "Candidate Match Analysis",
        "Match Score",
        "CV Suggestions",
        "Cover Letter",
        "Next Action",
    ]

    marker = f"{heading}:"

    if marker not in text:
        return ""

    section = text.split(marker, 1)[1]

    end = len(section)

    for other_heading in headings:
        other_marker = f"{other_heading}:"

        if other_heading == heading:
            continue

        position = section.find(other_marker)

        if 0 < position < end:
            end = position

    return section[:end].strip()
