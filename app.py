import streamlit as st

from agent import run_application_agent
from stage_actions import SUPPORTED_STAGES
from tools.candidate_profile import (
    delete_candidate_profile,
    load_candidate_profile,
    save_candidate_profile,
)
from tools.read_cv import read_uploaded_cv
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

    cv_source = st.radio(
        "Choose your CV source",
        [
            "Upload or paste a CV",
            "Use my saved CV",
        ],
    )

    candidate_profile = ""
    cv_error = None
    save_cv = False

    if cv_source == "Upload or paste a CV":
        uploaded_cv = st.file_uploader(
            "Upload your CV",
            type=["pdf", "docx", "txt"],
        )

        pasted_cv = st.text_area(
            "Or paste your CV",
            placeholder="Paste the full text of your CV here.",
            height=250,
        )

        candidate_profile = pasted_cv.strip()

        if uploaded_cv is not None:
            try:
                candidate_profile = read_uploaded_cv(uploaded_cv)
                st.success(f"CV loaded: {uploaded_cv.name}")

            except ValueError as error:
                cv_error = str(error)
                candidate_profile = ""
                st.error(cv_error)

        save_cv = st.radio(
            "How should the app use this CV?",
            [
                "Use for this application only",
                "Save for future applications",
            ],
        ) == "Save for future applications"

    else:
        saved_profile = load_candidate_profile()

        if saved_profile:
            candidate_profile = saved_profile
            st.success("Your saved CV is ready to use.")

            if st.button("Delete saved CV"):
                delete_candidate_profile()
                st.success("Your saved CV has been deleted.")
                st.rerun()

        else:
            st.warning(
                "No saved CV was found. Upload or paste a CV first."
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
        if cv_error:
            st.error(
                "Please upload a readable CV or remove the file "
                "and paste your CV."
            )

        elif not candidate_profile:
            st.warning(
                "Please upload, paste or select a saved CV."
            )

        elif not job_url and not pasted_job_description:
            st.error(
                "Add a job URL or job description."
            )

        else:
            if save_cv:
                save_candidate_profile(candidate_profile)
                st.success(
                    "Your CV text has been saved for future applications."
                )

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
