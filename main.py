import argparse
from news_fetcher import fetch_news
from summarizer import summarize_news
from datetime import datetime
import os

def save_output(topic: str, summary: str, output_format: str):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    slug = topic.replace(' ', '_')
    
    if output_format == "markdown":
        filename = f"briefing_{slug}_{timestamp}.md"
        with open(filename, "w") as f:
            f.write(f"# 📰 AI News Briefing: {topic}\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write("---\n\n")
            f.write(summary)
        print(f"\n💾 Saved to {filename}")
    else:
        filename = f"briefing_{slug}_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write(f"BRIEFING: {topic}\n")
            f.write(f"Generated: {datetime.now()}\n\n")
            f.write(summary)
        print(f"\n💾 Saved to {filename}")

def run(topic: str, num_articles: int, output_format: str, save: bool):
    print(f"\n🔍 Fetching news about: {topic}\n")
    
    articles = fetch_news(topic, num_articles=num_articles)
    
    if not articles:
        print("No articles found. Try a different topic.")
        return
    
    print(f"✅ Found {len(articles)} articles. Summarizing...\n")
    print("=" * 60)
    print(f"📰 AI NEWS BRIEFING: {topic.upper()}")
    print(f"🕐 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60 + "\n")
    
    summary = summarize_news(topic, articles)  # streaming happens inside here
    
    print("\n" + "=" * 60)
    
    if save:
        save_output(topic, summary, output_format)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI News Summarizer")
    
    parser.add_argument("--topic", type=str, required=True, help="Topic to search news for")
    parser.add_argument("--articles", type=int, default=5, help="Number of articles to fetch (default: 5)")
    parser.add_argument("--output", type=str, choices=["text", "markdown"], default="text", help="Output format (default: text)")
    parser.add_argument("--save", action="store_true", help="Save output to file")
    
    args = parser.parse_args()
    
    run(
        topic=args.topic,
        num_articles=args.articles,
        output_format=args.output,
        save=args.save
    )