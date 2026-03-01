import requests

def fetch(topic: str, num_articles: int = 5) -> list[dict]:
    try:
        # Search HackerNews via Algolia API (official HN search)
        response = requests.get(
            "https://hn.algolia.com/api/v1/search",
            params={
                "query": topic,
                "tags": "story",
                "hitsPerPage": num_articles
            }
        )
        response.raise_for_status()
        hits = response.json().get("hits", [])

        return [
            {
                "title": h.get("title", ""),
                "source": "HackerNews",
                "description": h.get("story_text") or h.get("title", ""),
                "url": h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                "published_at": h.get("created_at", "")
            }
            for h in hits
            if h.get("title")
        ]
    except Exception as e:
        print(f"[HackerNews] Error: {e}")
        return []