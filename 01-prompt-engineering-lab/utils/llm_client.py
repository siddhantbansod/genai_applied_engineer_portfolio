from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model_name = "gemini-3-flash-preview"


def ask_llm(prompt: str) -> str:
        response = client.models.generate_content(model=model_name, contents=prompt)
        return response.text

