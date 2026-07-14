import streamlit as st

from agent import run_application_agent
from stage_actions import SUPPORTED_STAGES
from tools.tracker_csv import load_tracker


st.set_page_config(
    page_title="TechNeeks Job Agent",
    page_icon="🧠",
)

st.title("🧠 TechNeeks Job Application Agent")

build_tab, tracker_tab = st.tabs(
    [
        "Build application pack",
        "Application tracker",
    ]
)


with build_tab:
    job_url = st.text_input("Job URL")

    pasted_job_description = st.text_area(
        "Or paste the job description",
        height=200,
    )

    candidate_profile = st.text_area(
        "Paste your CV or candidate profile",
        height=250,
    )

    stage = st.selectbox(
        "Application stage",
        SUPPORTED_STAGES,
    )

    mock_mode = st.checkbox(
        "Use mock mode",
        value=True,
    )

    if st.button("Build application pack"):
        if not candidate_profile:
            st.error("Add a candidate profile.")

        elif not job_url and not pasted_job_description:
            st.error(
                "Add a job URL or job description."
            )

        else:
            try:
                with st.spinner("Running workflow..."):
                    result = run_application_agent(
                        job_url=job_url,
                        pasted_job_description=pasted_job_description,
                        candidate_profile=candidate_profile,
                        stage=stage,
                        mock_mode=mock_mode,
                    )

            except Exception as error:
                st.error(f"The workflow failed: {error}")

            else:
                st.success("Application saved.")

                st.subheader("Role summary")
                st.write(result["role_summary"])

                st.subheader("Application stage")
                st.write(result["stage"])

                st.subheader("Match analysis")
                st.write(result["match_analysis"])

                st.subheader("CV suggestions")
                st.write(result["cv_suggestions"])

                st.subheader("Cover letter")
                st.write(result["cover_letter"])

                st.subheader("Next action")
                st.write(result["next_action"])


with tracker_tab:
    st.header("Application tracker")

    tracker = load_tracker()

    st.dataframe(
        tracker,
        use_container_width=True,
    )
