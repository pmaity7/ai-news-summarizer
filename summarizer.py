import requests

def summarize_news(topic: str, articles: list[dict]) -> str:
    articles_text = ""
    for i, article in enumerate(articles, 1):
        articles_text += f"""
Article {i}:
Title: {article['title']}
Source: {article['source']}
Summary: {article['description']}
URL: {article['url']}
---"""

    prompt = f"""You are a professional news analyst. I'll give you a list of recent news articles about "{topic}".

Your job is to produce a clean, structured briefing with:
1. A 2-3 sentence executive summary of the overall narrative
2. 3-5 key developments, each explained in 1-2 sentences
3. One "why it matters" insight at the end

Here are the articles:
{articles_text}

Write the briefing now:"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": True        # streaming enabled
        },
        stream=True               # stream the HTTP response too
    )

    response.raise_for_status()
    
    full_response = ""
    
    for line in response.iter_lines():
        if line:
            import json
            chunk = json.loads(line)
            token = chunk.get("response", "")
            print(token, end="", flush=True)  # print each token as it arrives
            full_response += token
            
            if chunk.get("done"):
                break
    
    return full_response