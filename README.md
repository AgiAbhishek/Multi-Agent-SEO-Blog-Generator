# SEO Blog Generator

A Python-based multi-agent system that generates high-quality, SEO-optimized blog posts on trending HR-related topics.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview
This project is a multi-agent system that automates the creation of SEO-optimized blog posts. It uses multiple agents to:

- Research trending HR topics.
- Plan the blog structure.
- Generate content.
- Optimize for SEO.
- Review and proofread the final output.

The blog post is saved in multiple formats: Markdown, HTML, TXT, and PDF.

## Features
- **Research Agent:** Fetches trending HR topics and gathers relevant information.
- **Content Planning Agent:** Creates a structured outline for the blog post.
- **Content Generation Agent:** Writes the blog post based on the outline.
- **SEO Optimization Agent:** Ensures the content follows SEO best practices.
- **Review Agent:** Proofreads and improves the content quality.
- **Multi-Format Output:** Saves the blog post in Markdown, HTML, TXT, and PDF formats.

## System Architecture
The system consists of the following agents:

1. **Research Agent:** Finds trending topics and gathers information.
2. **Content Planning Agent:** Creates a structured outline.
3. **Content Generation Agent:** Writes the blog post.
4. **SEO Optimization Agent:** Optimizes the content for SEO.
5. **Review Agent:** Proofreads and improves the content.

The agents work sequentially to generate the final blog post.

## Installation
### Prerequisites
- Python 3.8 or higher.
- A Google API key (for the Generative AI module).

### Steps
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/seo-blog-generator.git
   cd seo-blog-generator
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your Google API key to the `.env` file:

   ```bash
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

## Usage
Run the script to generate a blog post:

```bash
python3 main.py
```

The blog post will be saved in the `outputs` directory in the following formats:

- `blog_post.md` (Markdown)
- `blog_post.html` (HTML)
- `blog_post.txt` (Plain Text)
- `blog_post.pdf` (PDF)

## Dependencies
The project uses the following Python libraries:

- `fpdf2`: For generating PDF files.
- `google-generativeai`: For content generation using Google's Generative AI.
- `python-dotenv`: For managing environment variables.
- `requests`: For making HTTP requests.
- `rake-nltk`: For keyword extraction.
- `beautifulsoup4`: For web scraping.

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request.

## Support
If you encounter any issues or have questions, feel free to open an issue on the GitHub repository.
