# TechNeeks BUILD_001: Job Assistant

This is the starter project from the TechNeeks AGENT TALK workshop.

We built a simple Job Application Agent in about an hour.

It is not a finished product.

It is a starting point.

The challenge is to make it more useful.

---

## What this app does

The app helps with a basic job application workflow.

It can:

- take a job URL or pasted job description
- take a CV or candidate profile
- analyse the role
- suggest CV improvements
- draft application material
- recommend a next action
- save the application to a CSV tracker
- record the current application stage

The basic flow is:

```text
job description
↓
candidate profile
↓
role analysis
↓
application pack
↓
tracker
```

---

## Is this an AI agent?

The honest answer: it is a simple agentic workflow.

Python controls the sequence of steps.

The LLM handles the language-heavy work.

The app introduces a few useful building blocks:

```text
LLM + tools + state + orchestration
```

In this project:

- the LLM analyses and writes
- the tools scrape job pages and save applications
- the state is stored in the tracker
- the orchestration decides what happens and in what order

A more advanced version could let the system inspect state, choose approved actions, use tools, update the tracker, and decide what to do next.

That is where it starts to feel more like an agent.

---

## Project structure

```text
.
├── app.py
├── agent.py
├── llm.py
├── prompts.py
├── requirements.txt
├── tools/
│   ├── scrape_job.py
│   └── tracker_csv.py
└── outputs/
```

### Key files

- `app.py` — Streamlit interface
- `agent.py` — main workflow logic
- `llm.py` — mock or live LLM call
- `prompts.py` — prompt text
- `tools/scrape_job.py` — reads and cleans job page text
- `tools/tracker_csv.py` — saves and loads applications
- `outputs/` — stores generated tracker files

---

## Requirements

You need:

- Python 3.10 or later
- pip
- a terminal
- a web browser

---

## Run it locally

Clone the repo:

```bash
git clone REPO-LINK-HERE
cd REPO-FOLDER-HERE
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the app:

```bash
python -m streamlit run app.py
```

Streamlit should open the app in your browser.

The local address is usually:

```text
http://localhost:8501
```

---

## Using the app

1. Open the **Build application pack** tab.
2. Add a job URL or paste a job description.
3. Paste a CV or candidate profile.
4. Leave mock mode enabled if you do not have a live model connected.
5. Select **Build application pack**.
6. Review the output.
7. Open the **Application tracker** tab.
8. Check that the application was saved.

---

## Mock mode

Mock mode lets the app run without:

- an API key
- a live LLM provider
- model usage costs

The mock response is hard-coded.

It is useful for understanding the flow of the app.

It does not perform real analysis of the job description or candidate profile.

To connect a live model, update `llm.py`.

Do not commit API keys.

---

## BUILD_001 challenge

This repo is also the starting point for the first TechNeeks build challenge.

The challenge:

## Make the Job Assistant more useful.

You can:

- fork the repo
- raise a PR
- build your own version from the starter project

Your version could include:

- a better UI
- live LLM integration
- structured JSON outputs
- better job-page extraction
- interview stage tracking
- interview preparation
- follow-up reminders
- duplicate detection
- Notion or Google Sheets integration
- a database instead of CSV
- tests
- better validation
- a completely different workflow

The starter app is just the starting point.

---

## How to enter

To enter the challenge, send:

1. your PR link or forked repo link
2. a short write-up explaining what you changed and why
3. instructions for how to run or view your version

Screenshots or a short demo video are strongly encouraged.

Your write-up should answer:

- What did you change?
- Why did you choose that improvement?
- How does your version work?
- What would you improve with more time?
- What AI tools helped you, if any?

The winning build will receive:

- £30 Amazon voucher
- TechNeeks feature
- chance to demo at a future TechNeeks session

Most code does not automatically win.

We care about useful ideas, clear thinking, and working demos.

---

## Responsible use

Do not use this app to invent experience, qualifications, skills, projects, or employment history.

Generated application material should be reviewed before use.

CVs can contain personal information, so be careful what you send to external model providers.

Job pages and pasted text should be treated as untrusted input.

No application should be submitted automatically without human review.

---

## Workshop guide

The full workshop guide is here:

```text
WORKSHOP-GUIDE-LINK-HERE
```

---

## Contributing

This project is designed to be extended.

A simple contribution flow:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the app locally.
5. Open a pull request with a clear explanation of what changed.

---

## Licence

MIT.

---

## TechNeeks

TechNeeks is a community for people who want to learn, build, and connect.

Hackathon meets the cookout.

https://jointechneeks.org