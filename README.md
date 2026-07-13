# techneeks-job-agent
# TechNeeks Job Application Agent

A beginner-friendly workshop project for learning how AI applications combine:

```text
LLM + tools + state + orchestration
```

The project builds a small job application assistant that can read a job description, compare it with a candidate profile, generate application material, and save the application to a tracker.

It is designed as an introduction to AI agents and agentic workflows for people with basic Python knowledge.

## What the project does

The application can:

* accept a job URL
* attempt to read the job page
* fall back to a pasted job description
* accept a CV or candidate profile
* analyse the role using an LLM
* suggest CV improvements
* draft a cover letter
* recommend a next action
* save the application to a CSV tracker
* record the current application stage

The workflow is:

```text
Job URL or pasted description
↓
Read the job information
↓
Compare it with the candidate profile
↓
Generate application material
↓
Save the application
↓
Track the current stage and next action
```

## Is this an AI agent?

The first version is best described as a:

> **stateful, tool-using AI workflow**

Python controls the sequence of actions, while the LLM performs the language-heavy analysis.

The project demonstrates several important building blocks used in agent systems:

* a goal
* tools
* state
* orchestration
* an LLM
* a user interface

A more advanced version could allow the model to choose between approved tools, retrieve previous application state, retry failed actions, and continue until a completion condition is met.

## Workshop goal

By completing the project, participants should understand:

* the difference between an LLM and an AI application
* how tools extend what an LLM-based system can do
* how state allows information to persist between runs
* how orchestration controls a multi-step workflow
* how a simple workflow can be extended into a more agentic system

You do not need to be an AI engineer.

You should be able to read basic Python and follow terminal instructions.

## Project structure

```text
techneeks-job-agent/
├── app.py
├── agent.py
├── llm.py
├── prompts.py
├── requirements.txt
│
├── tools/
│   ├── __init__.py
│   ├── scrape_job.py
│   └── tracker_csv.py
│
└── outputs/
```

### `app.py`

Contains the Streamlit user interface.

### `agent.py`

Controls the order of the workflow.

### `llm.py`

Contains the model integration and mock response.

### `prompts.py`

Contains the instructions sent to the model.

### `tools/scrape_job.py`

Attempts to retrieve and clean text from a job page.

### `tools/tracker_csv.py`

Creates, loads, and updates the application tracker.

### `outputs/`

Stores generated files such as the CSV tracker.

## Requirements

* Python 3.10 or later
* `pip`
* a terminal
* a web browser

The project uses:

* Streamlit
* Requests
* Beautiful Soup
* pandas

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/techneeks-job-agent.git
cd techneeks-job-agent
```

### Create a virtual environment

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

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the application

```bash
python -m streamlit run app.py
```

Streamlit should open the application in your browser.

The local address will usually be:

```text
http://localhost:8501
```

## Using the application

1. Open the **Build application pack** tab.
2. Add a job URL or paste a job description.
3. Paste a CV or candidate profile.
4. Leave mock mode enabled for the workshop version.
5. Select **Build application pack**.
6. Review the generated output.
7. Open the **Application tracker** tab.
8. Confirm that the application was saved.

## Mock mode

Mock mode allows the application to run without:

* an API key
* an external LLM provider
* model usage charges
* an internet connection for model calls

The mock response is hard-coded.

It is intended to demonstrate the architecture and application flow. It does not perform real analysis of the job description or candidate profile.

To use a live model, replace the implementation in `llm.py` with an API call to your chosen provider.

## Core concepts

### LLM

The Large Language Model handles language-based work such as:

* summarising a role
* comparing a role with a candidate profile
* identifying gaps
* drafting a cover letter

The LLM is one component of the application.

### Tools

Tools are functions or services that perform specific actions.

This project includes tools for:

```python
scrape_job_url()
append_application()
load_tracker()
```

### State

State is information the system knows about the current process.

Example:

```python
{
    "company": "ExampleTech",
    "role_title": "Junior AI Engineer",
    "stage": "Application Drafted",
    "match_score": 78,
    "next_action": "Review and apply within 48 hours"
}
```

The CSV tracker provides simple persistent state because the application data remains available after the program stops.

### Orchestration

Orchestration is the code that controls what happens and in what order.

In this project:

```text
try the job URL
↓
use scraped or pasted text
↓
build the prompt
↓
call the LLM
↓
parse the response
↓
save the application
```

The orchestration logic lives primarily in `agent.py`.

## Current limitations

This is a learning project rather than a production-ready job application platform.

Current limitations include:

* the model does not choose which tools to use
* the workflow follows a fixed sequence
* mock mode does not analyse user input
* the heading-based response parser is fragile
* CSV is not suitable for large or multi-user applications
* duplicate applications are not prevented
* stored application stages do not yet control later behaviour
* many job websites block simple scraping
* generated claims are not automatically checked against the CV
* no application should be submitted automatically

## Possible extensions

### Add a live LLM

Connect `call_llm()` to a model provider.

Keep API keys in environment variables rather than storing them in source code.

### Use structured output

Ask the model to return JSON:

```json
{
  "company": "ExampleTech",
  "role_title": "Junior AI Engineer",
  "match_score": 78,
  "next_action": "Review and apply within 48 hours"
}
```

Validate the response before saving it.

### Add application stage logic

Allow the system to behave differently depending on the current stage.

Examples:

```python
if stage == "Applied":
    check_follow_up_date()

if stage == "Technical Interview":
    generate_interview_questions()
```

### Update existing applications

Add tools to:

* load an application
* move it to a new stage
* update its next action
* retain a history of changes

### Add scheduled job discovery

Run a daily process that:

```text
searches for jobs
↓
scores each match
↓
removes duplicates
↓
saves strong matches
↓
creates a summary
```

### Replace CSV with a database

SQLite is a useful local next step.

A larger deployed application could use PostgreSQL, Supabase, or another managed database.

### Add a controlled agent loop

A more agentic version could:

```text
observe state
↓
choose an approved action
↓
use a tool
↓
update state
↓
check progress
↓
continue or stop
```

External actions such as sending emails or submitting applications should require human approval.

## Responsible use

Do not use the system to invent qualifications, employment history, or skills.

Generated application material should be reviewed and edited by the candidate before use.

When connecting a live model, be aware that CVs may contain personal information. Users should understand:

* what information is stored
* what information is sent to an external model
* how their information can be deleted
* which external services are involved

Job pages and other web content should be treated as untrusted input.

## Workshop guide

The full workshop guide explains:

* chatbots and agents
* LLMs
* tools
* state
* orchestration
* the project code
* possible extensions into a more agentic system

Add a link here once the guide has been published:

```text
WORKSHOP-GUIDE-LINK
```

## Contributing

This repository is designed to be extended.

Possible contributions include:

* improving the interface
* adding structured model output
* integrating a live model
* improving job-page extraction
* adding stage-specific actions
* replacing CSV storage
* adding tests
* improving validation and error handling
* adding accessibility improvements

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the application locally.
5. Open a pull request describing what you changed.

## Challenge

Build on the starter project and create a more useful version of the job application assistant.

Your version could include:

* a better user interface
* real model integration
* structured outputs
* application-stage logic
* interview preparation
* job discovery
* duplicate detection
* reminders
* a database
* improved safety or validation

Document:

* what you changed
* why you changed it
* how your version works
* what role AI tools played in your development process

A working demo, short video, or written walkthrough is encouraged.

## Licence

Choose a licence before publishing the repository.

For an open-source workshop project, the MIT Licence is a common simple option.

## Acknowledgements

Created as part of the TechNeeks AI Agents Workshop.

The project is intended to help beginners understand how practical AI systems combine models, tools, state, and software orchestration.

