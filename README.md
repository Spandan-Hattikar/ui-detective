# UI Detective 🕵️

**An AI-powered UI/UX issue detector using Gemma.**

UI Detective analyzes screenshots of websites and identifies potential user-interface and user-experience problems. It provides explanations, severity levels, and suggested CSS fixes.

## Features

- Upload website screenshots for analysis
- Preview the selected screenshot
- Detect potential UI/UX issues
- View issue severity and supporting evidence
- Get suggested CSS fixes

## Tech Stack

- Python and Flask
- HTML, CSS, and JavaScript
- Google Gen AI SDK
- Gemma model


## AI Model

UI Detective uses **Gemma 4 (`gemma-4-26b-a4b-it`)** to analyze uploaded UI screenshots and generate structured findings with severity levels, evidence, and suggested CSS fixes.

The model is accessed through Google's Gen AI SDK. An API key is required to run the analysis.

- Model family: Gemma
- Input: UI screenshot
- Output: UI/UX findings and suggested CSS improvements


## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd hacktober
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Set your API key in PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Never commit your API key or put it directly in your source code.

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## How It Works

1. The user uploads a screenshot.
2. The Flask backend loads the image.
3. The Gemma model analyzes the screenshot.
4. The application displays detected issues and proposed CSS fixes.

## License

This project is intended to be released under the Apache License 2.0. See `LICENSE` for details.

