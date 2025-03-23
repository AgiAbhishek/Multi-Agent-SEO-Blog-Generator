# seo_agent.py
from rake_nltk import Rake
import logging

class SEOOptimizationAgent:
    """Ensures the content follows SEO best practices."""

    def extract_keywords(self, text, num_keywords=5):
        """
        Extracts keywords from the content using RAKE.
        Args:
            text (str): The content to analyze.
            num_keywords (int): The number of keywords to extract.
        Returns:
            list: A list of extracted keywords.
        """
        rake = Rake()
        rake.extract_keywords_from_text(text)
        return rake.get_ranked_phrases()[:num_keywords]

    def optimize_content(self, content):
        """
        Optimizes the content for SEO by adding keywords and ensuring proper structure.
        Args:
            content (str): The content to optimize.
        Returns:
            str: The optimized content.
        """
        try:
            keywords = self.extract_keywords(content)
            # Add keywords to the content (example implementation)
            optimized_content = content + "\n\nKeywords: " + ", ".join(keywords)
            return optimized_content
        except Exception as e:
            logging.error(f"Error optimizing content: {e}")
            return content