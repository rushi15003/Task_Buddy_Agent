# gemini_wrapper.py

import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Create the model (using Gemini Pro)
model = genai.GenerativeModel("gemini-2.0-flash")

def call_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error using Gemini API: {e}"
