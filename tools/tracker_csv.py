import os
import pandas as pd

from stage_actions import choose_stage_action


TRACKER_PATH = "outputs/applications.csv"

COLUMNS = [
    "date_added",
    "company",
    "role_title",
    "job_url",
    "stage",
    "match_score",
    "next_action",
]


def ensure_tracker_exists():
    os.makedirs("outputs", exist_ok=True)

    if not os.path.exists(TRACKER_PATH):
        tracker = pd.DataFrame(columns=COLUMNS)
        tracker.to_csv(TRACKER_PATH, index=False)


def append_application(application: dict):
    ensure_tracker_exists()

    tracker = pd.read_csv(TRACKER_PATH)

    new_row = {
        column: application.get(column, "")
        for column in COLUMNS
    }

    tracker = pd.concat(
        [tracker, pd.DataFrame([new_row])],
        ignore_index=True,
    )

    tracker.to_csv(TRACKER_PATH, index=False)


def load_tracker():
    ensure_tracker_exists()
    return pd.read_csv(TRACKER_PATH)


def get_application(
    company: str,
    role_title: str,
) -> dict | None:
    tracker = load_tracker()

    matches = tracker[
        (tracker["company"] == company)
        & (tracker["role_title"] == role_title)
    ]

    if matches.empty:
        return None

    return matches.iloc[-1].to_dict()


def update_application_stage(
    company: str,
    role_title: str,
    new_stage: str,
) -> bool:
    ensure_tracker_exists()

    tracker = pd.read_csv(TRACKER_PATH)

    matches = (
        (tracker["company"] == company)
        & (tracker["role_title"] == role_title)
    )

    if not matches.any():
        return False

    latest_index = tracker[matches].index[-1]

    tracker.loc[latest_index, "stage"] = new_stage
    tracker.loc[latest_index, "next_action"] = choose_stage_action(
        new_stage
    )

    tracker.to_csv(TRACKER_PATH, index=False)

    return True
