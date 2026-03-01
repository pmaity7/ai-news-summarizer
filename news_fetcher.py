from sources import fetch_news
from sources import newsapi_fetcher, hackernewsapi_fetcher

def fetch_news(topic: str, num_articles: int = 5) -> list[dict]:
    print("  📡 Fetching from NewsAPI...")
    num_articles = int(num_articles)
    newsapi_results = newsapi_fetcher.fetch_news(topic, num_articles)

    print("  📡 Fetching from HackerNews...")
    hn_results = hackernewsapi_fetcher.fetch(topic, num_articles)

    # Combine both sources
    all_articles = newsapi_results + hn_results

    # Deduplicate by title (lowercased)
    seen_titles = set()
    unique_articles = []
    for article in all_articles:
        title_key = article["title"].lower().strip()
        if title_key not in seen_titles:
            seen_titles.add(title_key)
            unique_articles.append(article)

    print(f"  ✅ Total unique articles: {len(unique_articles)}")
    return unique_articles[:num_articles * 2]  # cap total results