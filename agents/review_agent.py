import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class ReviewAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')  # Updated model name

    def proofread(self, content):
        try:
            response = self.model.generate_content(
                f"Proofread and improve the following content:\n{content}"
            )
            improved_content = response.text
            return improved_content
        except Exception as e:
            print("Failed to connect to Gemini API:", e)
            return content  # Fallback to the original content