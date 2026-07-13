import os
import pandas as pd


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