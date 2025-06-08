# AI Blog Post Generator – Interview Project

This project is a simplified AI-powered blog generator built with Flask. It uses mocked SEO data and mocked OpenAI-style content to simulate generating blog posts for any keyword. The app supports a REST API and includes a daily automation feature via APScheduler.

---

## Features

* Flask REST API: `/generate?keyword=...`
* Mocked SEO data with search volume, difficulty, and CPC
* Mocked blog content with placeholder affiliate links
* Saves output as Markdown and metadata JSON
* Daily scheduled generation using APScheduler
* `.env` support (no real API key required)

---

## Setup

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/siddhantgade/ai-blog-generator-interview-SiddhantGade.git
cd ai-blog-generator-interview-SiddhantGade
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate for Mac/Linux
pip install -r requirements.txt
```

### 2. Create `.env` File

Even though the OpenAI API is mocked, a `.env` file is required:

```
OPENAI_API_KEY=sk-mocked-key
```

---

## Usage

### Start the Flask App

```bash
python app.py
```

### Generate a Blog Post

You can call the API from your browser or using curl:

#### Example (Browser)

```
http://localhost:5000/generate?keyword=wireless%20earbuds
```

#### Example (Curl)

```bash
curl "http://localhost:5000/generate?keyword=wireless%20earbuds"
```

### Output Files

Generated files will be saved in the `generated_posts/` folder:

```
generated_posts/
├── wireless_earbuds_2025-06-08_11-32.md
├── wireless_earbuds_2025-06-08_11-32.json
```

Each post includes structured content and associated SEO metadata.

---

## Daily Automation

The app includes a scheduled job that automatically generates a blog post once every 24 hours using APScheduler. The default keyword is:

```python
keyword = "wireless earbuds"
```

The job is triggered on app startup and runs daily. Files are saved in the same `generated_posts/` directory.

---

## Example Blog Post

See `generated_posts/example_wireless_earbuds.md` for a complete sample output:

```
# The Ultimate Guide to Wireless Earbuds

Looking for the best wireless earbuds? You’re in the right place.

## Why Wireless Earbuds?

- High search volume: 54000
- Low competition (difficulty): 36
- Great affiliate potential (Avg. CPC: $1.2)

## Top Picks

1. Product A – [Check it out](https://dummy.link/affiliate1)  
2. Product B – [Learn more](https://dummy.link/affiliate2)

## Final Thoughts

If you're considering buying wireless earbuds, now's the time. Happy shopping!
```

---

## Folder Structure

```
ai-blog-generator-interview-SiddhantGade/
├── app.py
├── ai_generator.py
├── seo_fetcher.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── generated_posts/
    ├── .gitkeep
    └── example_wireless_earbuds.md
```

---

## Future Improvements

If given more time, here’s what I would expand on:

* Use real OpenAI API for content generation
* Add blog category tagging
* Push to a CMS (like Ghost or Medium) via API
* Add a web UI to view past posts
* Implement a keyword suggestion engine

---

## Notes on SEO API Usage

Real SEO APIs were reviewed (SerpApi, KeywordTool, DataForSEO), but due to pricing or access restrictions, the SEO data in this project is mocked for demonstration purposes. The code is designed so that a real SEO API could be plugged in later with minimal changes.
