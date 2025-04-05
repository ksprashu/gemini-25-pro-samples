# AI Studio Gemini API Integration

This project demonstrates how to use the **Gemini API** in 3 distinct ways.
1) Using an API key obtained from **Google AI Studio**.
2) Using the SDK to invoke the model from **Google Cloud Vertex AI**.
3) Using an API key obtained from **Google Cloud Vertex AI**

It includes Python modules for setting up configuration, making authenticated requests to Gemini, and formatting responses.

[Companion blog](https://blog.prashu.com/3-ways-to-use-gemini-2-5-pro-experimental-b84952cc4deb)

**Disclaimer:**
_This code is a demonstration provided for educational purposes. It is intended to showcase a specific concept or functionality. Please note that this is not production-ready code. For best practices and detailed guidance on how to use similar implementations in a production environment, refer to the official documentation and resources._

---

## 📦 Features

- Fetch responses from Gemini using your API key
- Modular layout with clear separation of config and execution
- Pre-configured development environment with:
  - Code formatter: `black`
  - Linter + auto-fixer: `ruff`
  - Type checker: `mypy`
  - Git hooks via `pre-commit`

---

## ✅ Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) installed (`pip install uv`)
- A valid **Gemini API key** for AI Studio usage, stored in environment variables or `gemini25/config.py`.
- For **Vertex AI SDK usage (`vertex_sdk.py`)**:
   - **Google Cloud Project:** You need a Google Cloud project with billing enabled.
   - **Enable Vertex AI API:** Ensure the [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com) is enabled for your project.
   - **Application Default Credentials (ADC):** Set up ADC for authentication. The easiest way for local development is often to run:
     ```bash
     gcloud auth application-default login
     ```
     See the [Google Cloud ADC documentation](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details and other methods.
- For **Vertex AI API Key usage (`vertex_apikey.py`)**:
   - A valid **Vertex AI API key** stored in environment variables or `gemini25/config.py`.

---

## 🌍 Setting Environment Variables

Before running any of the scripts, ensure that the required environment variables are set. Example:

```bash
export GEMINI_API_KEY="your-api-key-here"
export VERTEX_API_KEY="your-api-key-here"
```

Alternatively, create a `.env` file in the project root:

```
GEMINI_API_KEY=your-api-key-here
VERTEX_API_KEY=your-api-key-here
```

You can use a library like [`python-dotenv`](https://pypi.org/project/python-dotenv/) to automatically load this file into your environment.

---

## 🚀 Setup Instructions

### Step 1: Create and Activate a Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

### Step 2: Install Dependencies

```bash
uv pip install .
```

Or using Poetry (alternative):

```bash
poetry install --with dev
```

---



## 🔧 Running the Scripts

Each of the following Python files in `gemini25/` can be executed directly:

### `aistudio_apikey.py`
```bash
poetry run python gemini25/aistudio_apikey.py
```

### `vertex_sdk.py`
```bash
poetry run python gemini25/vertex_sdk.py
```

### `vertex_apikey.py`
```bash
poetry run python gemini25/vertex_apikey.py
```

Ensure the correct environment variables are set before running any script.

---

## 🧪 Development Workflow

### Format Code

```bash
poetry run black .
poetry run ruff format .
```

### Lint Code (and auto-fix)

```bash
poetry run ruff check . --fix
```

### Type Check

```bash
poetry run mypy gemini25/
```

---

## 🔀 Pre-Commit Hooks

This project uses `pre-commit` to auto-format and check code quality before each commit.

### Enable Git Hooks

```bash
pre-commit install
pre-commit run --all-files
```

---

## 🧐 Notes

- API keys and secrets should not be committed to version control. Use `.env`, `config.py`, or secret management solutions.
- Make sure to add `__init__.py` in all source folders to ensure proper packaging.

---

## 📜 License

MIT License © Prashanth Subrahmanyam

---
