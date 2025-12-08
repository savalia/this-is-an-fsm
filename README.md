# this-is-an-fsm

[![CI (main)](https://github.com/savalia/this-is-an-fsm/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/savalia/this-is-an-fsm/actions?query=branch%3Amain)
[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](./LICENSE.md)

Finite State Machine using CI including a state of unknown (error handler).

---

Table of contents
- What this project does
- Why this project is useful
- Quick Start (step-by-step tutorial)
- Usage (conceptual example)
- Running tests & CI locally
- Troubleshooting
- Where to get help
- Contributing
- Maintainers
- License

## What this project does

this-is-an-fsm is a small Python library and example set that implements a finite state machine (FSM) with an explicit "unknown" state used as an error handler. The project includes tests and a CI workflow to validate behavior automatically.

Key points:
- Focused, easy-to-read Python implementation of an FSM
- Explicit unknown/error state to capture unexpected events or corrupted state
- CI integration (GitHub Actions) to run tests and linters on the main branch

## Why this project is useful

- Makes stateful logic explicit and maintainable
- Provides a single, consistent path for handling unexpected events via the unknown state
- Simple API and small surface area, making it easy to adapt into services, automation, or CLI tools
- CI-driven development ensures regressions are caught early

## Quick Start — Step-by-step tutorial

This section walks you through getting the project up and running locally and running the tests.

Prerequisites
- Python 3.8 or newer
- Git
- Optional: virtualenv / venv

1) Clone the repository

```bash
git clone https://github.com/savalia/this-is-an-fsm.git
cd this-is-an-fsm
```

2) Create and activate a virtual environment

Linux / macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3) Install dependencies

If the project provides a requirements file:

```bash
pip install -r requirements.txt
```

If the project is packaged for editable install:

```bash
pip install -e .
```

4) Run tests

A common test command used in CI:

```bash
pytest -q
```

5) Run an example

If the repository includes example scripts, run them with Python. If not, follow the conceptual usage below to try the API locally.

## Usage — Conceptual example

The exact API names may differ; adapt the example to the library's actual module and class names.

```python
# Conceptual usage — update imports/names to match the repo
from this_is_an_fsm import FSM

# Define states
states = ["idle", "running", "error", "unknown"]

# Create FSM with initial state
fsm = FSM(states=states, initial="idle")

# Add transitions (event, from_state, to_state)
fsm.add_transition("start", "idle", "running")
fsm.add_transition("fail", "running", "error")
fsm.add_transition("recover", "error", "idle")

# Define unknown-state handler (captures unexpected or corrupted transitions/events)
def handle_unknown(state, event):
    # Example: log and set machine to error or a safe state
    print(f"UNKNOWN: state={{state}} event={{event}}")
    # take corrective action if necessary
    return "error"

fsm.set_unknown_state_handler(handle_unknown)

# Dispatch events
fsm.dispatch("start")
# if an unexpected event occurs, handle_unknown will run
fsm.dispatch("nonexistent_event")
```

## Running CI & Coverage (main branch)

- The CI badge at the top points to the GitHub Actions workflow named `ci.yml` on branch `main`.
- To inspect the workflow, review `.github/workflows/ci.yml` in this repository.
- Typical local commands that mirror CI jobs:
  - `pytest`
  - `flake8` or `pylint` (if configured)
  - `mypy` (if configured)

## Troubleshooting

- Tests failing locally:
  - Ensure the virtual environment is active and dependencies are installed.
  - Run a single test to isolate failures: `pytest tests/test_module.py::test_name -q`.
- CI shows failing badge:
  - Click the CI badge to open Actions and inspect the failing job logs.
  - Reproduce the failing command locally for faster debugging.
- Example API mismatch:
  - If usage examples here don't match the code, open an issue requesting a quickstart example that matches the library's API.

## Where to get help

- Open an issue: ./issues
- If Discussions are enabled, use them for design and usage questions.

## Contributing

Contributions are welcome. A typical workflow:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/my-change`.
3. Run tests and linters locally.
4. Open a pull request against `savalia/this-is-an-fsm:main`.

Please add tests for bug fixes and new features. If this repository contains a CONTRIBUTING.md file, follow that document for additional guidelines.

## Maintainers
- Maintainer: [savalia](https://github.com/savalia)

## License

This project is licensed under the MIT License — see ./LICENSE.md for details.

---

Notes & next steps
- Add a concrete `examples/` directory (if not present) with runnable scripts demonstrating common patterns.
- If you want, I can also create example scripts or additional CI badges for other branches.