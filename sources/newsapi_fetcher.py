import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_news(topic: str, num_articles: int = 5) -> list[dict]:
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "sortBy": "publishedAt",
        "pageSize": num_articles,
        "language": "en",
        "apiKey": os.getenv("NEWS_API_KEY")
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    articles = response.json().get("articles", [])
    
    return [
        {
            "title": a["title"],
            "source": a["source"]["name"],
            "description": a["description"],
            "url": a["url"],
            "published_at": a["publishedAt"]
        }
        for a in articles
        if a["title"] and a["description"]  # filter out nulls
    ]