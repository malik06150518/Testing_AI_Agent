# AI Test Automation Agent (Mocked)

A **mocked AI agent** for test automation. It is a rule-based planner, not a real LLM,
that mimics how an AI testing agent works: it reads a plain-English test goal, inspects
the page, decides the next action, executes it and verifies the result.

Built with **Python, pytest and Playwright**. No API key or paid service is required.

## How it works
1. A test goal is written in plain English, e.g.
   `Log in with username 'tomsmith' and password 'SuperSecretPassword!', then verify 'You logged into a secure area!' is shown`
2. The planner parses the goal into steps.
3. For each step it reads the page's accessibility snapshot and finds the matching element.
4. Playwright performs the action (fill, click) and verifies the expected text.
5. A test passes only if at least one verification succeeds.

## Project structure
```
agent/planner.py     parses goals and picks page elements
agent/runner.py      the agent loop that runs the steps
demo_app/login.html  demo page under test
tests/               pytest tests with plain-English goals
conftest.py          local demo server and the ai_agent fixture
pytest.ini           pytest and browser options
```

## Setup
```bash
pip install pytest pytest-playwright
playwright install chromium
```

## Run
```bash
pytest -v
pytest --headed --browser-channel chrome   # watch it in Google Chrome
```

## Supported goal steps
- `log in with username 'u' and password 'p'`
- `type 'value' into the 'Field' field`
- `click 'Name'`
- `verify 'text' is shown`

Every goal must include a verify step.

## Limitations
This is a demonstration, not a real AI. It only understands the phrases above and does
not interpret free-form instructions.
