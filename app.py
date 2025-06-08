from flask import Flask, request, jsonify
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
import json

app = Flask(__name__)
POSTS_DIR = "generated_posts"
os.makedirs(POSTS_DIR, exist_ok=True)

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400

    seo = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo)

    filename = f"{POSTS_DIR}/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    return jsonify({
        "keyword": keyword,
        "seo": seo,
        "blog_post": content
    })

@app.route('/favicon.ico')
def favicon():
    return '', 204

def daily_job():
    keyword = "wireless earbuds"
    seo = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M")
    safe_keyword = keyword.replace(' ', '_')

    # Save markdown file
    md_filename = f"{POSTS_DIR}/{safe_keyword}_{now}.md"
    with open(md_filename, 'w', encoding='utf-8') as f:
        f.write(content)

    # Save metadata JSON
    json_filename = f"{POSTS_DIR}/{safe_keyword}_{now}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump({
            "keyword": keyword,
            "generated_at": now,
            "seo": seo,
            "content": content
        }, f, indent=2)

    print(f"[{datetime.now()}] Scheduled blog post saved: {md_filename}")

# Start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=daily_job, trigger="interval", days=1)
scheduler.start()


if __name__ == "__main__":
    app.run(debug=True)
