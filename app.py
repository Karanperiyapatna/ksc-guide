from flask import Flask, render_template
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
MAX_RECORDS = int(os.getenv("MAX_RECORDS", 3))


# ------------------------------------------------------- Recent Notifications Updation code -------------------------------------------------------

DATA_FILE = "jobs.json"


def load_jobs():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_jobs(jobs):
    with open(DATA_FILE, "w") as f:
        json.dump(jobs, f)


@app.route("/api/add-job", methods=["POST"])
def add_job():
    jobs = load_jobs()

    data = request.json

    new_job = {
        "title": data.get("title"),
        "organization": data.get("organization"),
        "posts": data.get("posts"),
        "location": data.get("location"),
        "post_name": data.get("post_name"),
        "salary": data.get("salary"),
        "published_date": datetime.utcnow().isoformat()
    }

    # insert new record at top
    jobs.insert(0, new_job)

    # keep only last 3
    jobs = jobs[:MAX_RECORDS]

    save_jobs(jobs)

    return jsonify({"message": "Job added successfully"}), 201


@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    jobs = load_jobs()
    return jsonify(jobs)
# ------------------------------------------------------- End Recent Notifications Updation code -------------------------------------------------------


current_affairs = [
    "Government announces new policy reforms",
    "Stock market hits record high"
]

international_news = [
    "Global summit on climate change",
    "New trade agreements signed"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jobs')
def job_page():
    return render_template('jobs.html', jobs=jobs)

@app.route('/current-affairs')
def current_affairs_page():
    return render_template('current_affairs.html', news=current_affairs)

@app.route('/international-news')
def international_news_page():
    return render_template('international_news.html', news=international_news)

@app.route('/updation')
def updation_page():
    return render_template('updation.html')

@app.route('/aboutus')
def aboutus_page():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
