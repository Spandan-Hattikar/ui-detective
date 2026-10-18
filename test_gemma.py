
import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("API key is missing. Set GEMINI_API_KEY in your terminal.")

client = genai.Client(api_key=api_key)

print("Testing Gemma...")

response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents="Reply with exactly: UI Detective is ready!"
)

print("\nGemma replied:")
print(response.text)
