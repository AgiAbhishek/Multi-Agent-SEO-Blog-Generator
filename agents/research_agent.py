# research_agent.py
import requests
from bs4 import BeautifulSoup
import logging

class ResearchAgent:
    """Finds trending HR topics and gathers relevant information."""

    def find_trending_topics(self):
        """
        Fetches trending HR topics from an API or uses fallback topics.
        Returns:
            list: A list of trending topics.
        """
        try:
            url = "https://api.example.com/trending-topics"  # Replace with actual API endpoint
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()["topics"]
            else:
                logging.warning("Failed to fetch trending topics. Using fallback topics.")
                return ["Remote Work Trends", "Employee Engagement", "Hybrid Work Models"]
        except Exception as e:
            logging.error(f"Error fetching trending topics: {e}")
            return ["Remote Work Trends", "Employee Engagement", "Hybrid Work Models"]

    def gather_information(self, topic):
        """
        Gathers information on the selected topic using web scraping or APIs.
        Args:
            topic (str): The topic to research.
        Returns:
            str: The gathered information.
        """
        try:
            url = f"https://www.example.com/search?q={topic.replace(' ', '+')}"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup.get_text()
            else:
                logging.warning(f"Failed to gather information for topic: {topic}")
                return ""
        except Exception as e:
            logging.error(f"Error gathering information: {e}")
            return ""