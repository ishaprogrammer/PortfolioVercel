from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/resume")
def download_resume():
    return render_template('resume.html')

