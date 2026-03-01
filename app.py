from flask import Flask, request, jsonify
from news_fetcher import fetch_news
from summarizer import summarize_news
from datetime import datetime

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    # Validate input
    if not data or "topic" not in data:
        return jsonify({"error": "Missing 'topic' in request body"}), 400

    topic = data["topic"]
    num_articles = int(data.get("num_articles", 5))

    try:
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Request received for topic: {topic}")

        articles = fetch_news(topic, num_articles=num_articles)

        if not articles:
            return jsonify({"error": "No articles found for this topic"}), 404

        summary = summarize_news(topic, articles)

        return jsonify({
            "topic": topic,
            "article_count": len(articles),
            "summary": summary,
            "sources": list(set(a["source"] for a in articles)),
            "generated_at": datetime.now().isoformat()
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)