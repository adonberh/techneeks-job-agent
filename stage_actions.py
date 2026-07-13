SUPPORTED_STAGES = [
    "Discovered",
    "Application Drafted",
    "Applied",
    "Recruiter Screen",
    "Technical Interview",
    "Final Interview",
    "Rejected",
    "Offer",
]


def choose_stage_action(stage: str) -> str:
    if stage == "Discovered":
        return "Review the role and decide whether to apply."

    if stage == "Application Drafted":
        return "Review the application materials before submitting."

    if stage == "Applied":
        return "Check whether a follow-up is needed."

    if stage == "Recruiter Screen":
        return "Prepare an introduction and questions for the recruiter."

    if stage == "Technical Interview":
        return "Prepare technical and behavioural interview questions."

    if stage == "Final Interview":
        return "Prepare examples about impact, motivation, and teamwork."

    if stage == "Rejected":
        return "Record lessons and consider requesting feedback."

    if stage == "Offer":
        return "Review the offer and prepare negotiation questions."

    return "Review the application."
