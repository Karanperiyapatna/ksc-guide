from flask import Flask, render_template
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
import json
import uuid

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)


app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
MAX_RECORDS = int(os.getenv("MAX_RECORDS", 10))


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

	import uuid

	new_job = {
		"id": str(uuid.uuid4()),
		"title": data.get("title"),
		"organization": data.get("organization"),
		"post_name": data.get("post_name"),
		"vacancy": data.get("vacancy"),
		"qualification": data.get("qualification"),
		"salary": data.get("salary"),
		"last_date": data.get("last_date"),
		"apply_link": data.get("link"),
		"category": data.get("category"),
		"content": data.get("content")
	}

	jobs.insert(0, new_job)

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

@app.route('/studymaterial')
def studymaterial_page():
	return render_template('studymaterial.html')

@app.route('/banking')
def banking_page():
	return render_template('banking.html')

@app.route('/privatejobs')
def privatejob_page():
	return render_template('private_job.html')

@app.route('/karnataka_jobs')
def karnataka_jobs_page():
	return render_template('karnataka_jobs.html')

@app.route('/central_jobs')
def central_jobs_page():
	return render_template('central_jobs.html')

@app.route('/recruitments')
def recruitments_page():
	return render_template('recruitments.html')


@app.route('/testing')
def testing_page():
	return render_template('testing.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
