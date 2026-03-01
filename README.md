# 📰 AI News Summarizer

A local AI pipeline that fetches news from multiple sources, summarizes them using a local LLM (Ollama + LLaMA 3.2), and emails a daily briefing via n8n.

## Architecture
- **News Sources:** NewsAPI + HackerNews
- **LLM:** LLaMA 3.2 running locally via Ollama (no API costs)
- **API:** Flask REST endpoint
- **Automation:** n8n workflow (scheduled daily email)

## Setup

### Prerequisites
- Python 3.9+
- Ollama installed and running
- n8n (Docker)
- NewsAPI key (newsapi.org)

### Installation
```bash
git clone https://github.com/yourusername/ai-news-summarizer
cd ai-news-summarizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file:
```
NEWS_API_KEY=your_key_here
```

### Run
```bash
# Start Ollama
ollama serve

# Start Flask API
python app.py

# Or use CLI directly
python main.py --topic "AI agents" --articles 5 --output markdown --save
```

## Project Structure
```
├── app.py                  # Flask REST API
├── main.py                 # CLI interface
├── news_fetcher.py         # Aggregates all sources
├── summarizer.py           # Ollama LLM integration
└── sources/
    ├── newsapi_fetcher.py
    └── hackernewsapi_fetcher.py
```