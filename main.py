import os
import re
import logging
import random
from dotenv import load_dotenv
from agents.research_agent import ResearchAgent
from agents.planning_agent import ContentPlanningAgent
from agents.generation_agent import ContentGenerationAgent
from agents.seo_agent import SEOOptimizationAgent
from agents.review_agent import ReviewAgent

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables from .env file
load_dotenv()

def save_as_markdown(content, filename):
    """Save the content as a markdown file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    logging.info(f"Blog post saved as {filename}")

def save_as_html(content, filename):
    """Save the content as an HTML file."""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog Post</title>
        <style>
            body {{ max-width: 800px; margin: 20px auto; padding: 20px; }}
            img {{ max-width: 100%; }}
            pre {{ overflow-x: auto; }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    logging.info(f"Blog post saved as {filename}")

def save_as_txt(content, filename):
    """Save the content as a plain text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    logging.info(f"Blog post saved as {filename}")

def save_as_pdf(content, filename):
    """Save the content as a PDF file with improved layout handling."""
    try:
        # Clean content
        clean_content = re.sub(r"<[^>]*>", "", content)  # Remove HTML tags
        clean_content = re.sub(r"\*\*|```", "", clean_content)  # Remove markdown formatting

        # Create PDF with portrait orientation
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_margins(left=15, top=15, right=15)
        pdf.set_font("helvetica", size=12)  # Base font size

        # Configure auto page break
        pdf.set_auto_page_break(auto=True, margin=15)

        def add_formatted_line(line):
            """Helper to handle text wrapping and formatting."""
            current_width = pdf.w - pdf.l_margin - pdf.r_margin
            pdf.multi_cell(
                w=current_width,
                h=10,  # Line height
                txt=line,
                border=0,
                align='L',
                fill=False,
                new_x=XPos.LMARGIN,  # Use XPos from fpdf2
                new_y=YPos.NEXT  # Use YPos from fpdf2
            )

        # Split content into lines
        lines = clean_content.split("\n")
        for line in lines:
            line = line.strip()
            if not line:  # Skip empty lines
                pdf.ln(5)  # Add a small space for empty lines
                continue

            if line.startswith("# "):  # Heading level 1
                pdf.set_font("helvetica", "B", 16)
                add_formatted_line(line[2:].strip())
                pdf.ln(5)  # Add space after heading
                pdf.set_font("helvetica", size=12)
            elif line.startswith("## "):  # Heading level 2
                pdf.set_font("helvetica", "B", 14)
                add_formatted_line(line[3:].strip())
                pdf.ln(5)
                pdf.set_font("helvetica", size=12)
            elif line.startswith("- "):  # Bullet points
                pdf.set_font("helvetica", size=12)
                pdf.cell(10)  # Indent for bullet points
                add_formatted_line("• " + line[2:].strip())
            elif line.startswith("**"):  # Bold text
                pdf.set_font("helvetica", "B", 12)
                add_formatted_line(line.strip("*").strip())
                pdf.set_font("helvetica", size=12)
            else:  # Regular text
                pdf.set_font("helvetica", size=12)
                add_formatted_line(line)

        # Save the PDF
        pdf.output(filename)
        logging.info(f"Blog post saved as {filename}")
    except Exception as e:
        logging.error(f"Failed to save as PDF: {e}")

def main():
    logging.info("Starting the SEO Blog Generator...")
    
    # Step 1: Research Agent
    research_agent = ResearchAgent()
    topics = research_agent.find_trending_topics()
    logging.info(f"Trending Topics: {topics}")
    
    if not topics:
        logging.warning("No trending topics found. Using fallback topics.")
        topics = ["Remote Work Trends", "Employee Engagement", "Hybrid Work Models"]
    
    selected_topic = random.choice(topics)  # Randomly select a topic
    research_data = research_agent.gather_information(selected_topic)
    logging.info(f"Research Data: {research_data}")
    
    # Step 2: Content Planning Agent
    planning_agent = ContentPlanningAgent()
    outline = planning_agent.create_outline(research_data)
    logging.info(f"Generated Outline: {outline}")
    
    # Step 3: Content Generation Agent
    generation_agent = ContentGenerationAgent()
    content = generation_agent.generate_content(outline)
    logging.info(f"Generated Content: {content}")
    
    # Step 4: SEO Optimization Agent
    seo_agent = SEOOptimizationAgent()
    optimized_content = seo_agent.optimize_content(content)
    logging.info(f"Optimized Content: {optimized_content}")
    
    # Step 5: Review Agent
    review_agent = ReviewAgent()
    final_content = review_agent.proofread(optimized_content)
    logging.info(f"Final Content: {final_content}")
    
    # Create outputs directory
    os.makedirs("outputs", exist_ok=True)
    
    # Save in multiple formats
    save_as_markdown(final_content, "outputs/blog_post.md")
    save_as_html(final_content, "outputs/blog_post.html")
    save_as_txt(final_content, "outputs/blog_post.txt")
    save_as_pdf(final_content, "outputs/blog_post.pdf")

if __name__ == "__main__":
    main()