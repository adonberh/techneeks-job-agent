from pathlib import Path


PROFILE_PATH = Path("outputs/candidate_profile.txt")


def save_candidate_profile(profile_text: str) -> None:
    PROFILE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    PROFILE_PATH.write_text(
        profile_text.strip(),
        encoding="utf-8",
    )


def load_candidate_profile() -> str | None:
    if not PROFILE_PATH.exists():
        return None

    profile_text = PROFILE_PATH.read_text(
        encoding="utf-8",
    ).strip()

    return profile_text or None


def delete_candidate_profile() -> None:
    if PROFILE_PATH.exists():
        PROFILE_PATH.unlink()
