import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class ContentGenerationAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-pro')  # Updated model name

    def generate_content(self, outline):
        try:
            response = self.model.generate_content(
                f"Write a 2000-word blog post based on the following outline:\n{outline}"
            )
            content = response.text
            return content
        except Exception as e:
            print("Failed to connect to Gemini API:", e)
            return "Default Content: This is a placeholder blog post."  # Fallback content