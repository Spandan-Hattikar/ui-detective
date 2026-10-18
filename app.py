
import os
import json
from io import BytesIO

from flask import Flask, render_template, request, jsonify
from google import genai
from PIL import Image

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024  # 8 MB

MODEL_NAME = "gemma-4-26b-a4b-it"


def analyze_screenshot(image):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing.")

    client = genai.Client(api_key=api_key)

    prompt = """
You are UI Detective, an expert UI/UX reviewer.
Analyze this website screenshot for visible interface problems.

Return ONLY valid JSON in this exact structure:
{
  "summary": "A brief overall assessment",
  "findings": [
    {
      "severity": "High",
      "title": "Short issue title",
      "evidence": "What is visibly wrong in the screenshot",
      "fix": "A practical improvement",
      "css": "Optional suggested CSS"
    }
  ]
}

Return 3 to 5 findings. Use only High, Medium, or Low severity.
Only report issues supported by the screenshot. Do not claim to inspect
HTML, JavaScript, accessibility tree, or actual functionality.
If no clear issues are visible, suggest reasonable visual improvements.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image]
    )

    text = response.text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        text = text.rsplit("```", 1)[0]

    result = json.loads(text)
    if not isinstance(result.get("findings"), list):
        raise ValueError("Gemma returned an unexpected response.")

    return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    uploaded = request.files.get("screenshot")
    if not uploaded or not uploaded.filename:
        return jsonify({"error": "Please upload a screenshot."}), 400

    try:
        image = Image.open(BytesIO(uploaded.read())).convert("RGB")
        result = analyze_screenshot(image)
        return jsonify(result)
    except json.JSONDecodeError:
        return jsonify({
            "error": "The AI returned an unreadable response. Please try again."
        }), 502
    except Exception as exc:
        print("Analysis error:", repr(exc))
        return jsonify({
            "error": "Analysis failed. Check the VS Code terminal for details."
        }), 500


@app.errorhandler(413)
def file_too_large(_error):
    return jsonify({"error": "Image is too large. Maximum size is 8 MB."}), 413


if __name__ == "__main__":
    app.run(debug=True)
