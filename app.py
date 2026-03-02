from flask import Flask, render_template

app = Flask(__name__)

# Sample Data
jobs = [
    {"title": "Software Developer", "company": "ABC Tech"},
    {"title": "Data Analyst", "company": "XYZ Corp"}
]

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
