import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class ContentPlanningAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        print("Loaded GEMINI_API_KEY:", self.api_key)  # Debug statement
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')  # Updated model name

    def create_outline(self, research_data):
        try:
            response = self.model.generate_content(
                f"Create a detailed blog outline for the following research data:\n{research_data}"
            )
            outline = response.text
            return outline
        except Exception as e:
            print("Failed to connect to Gemini API:", e)
            return "Default Outline: Introduction, Body, Conclusion"  # Fallback outline