from app import app
from flask import render_template, request, url_for, redirect

@app.route("/")
def index():

    title = "ankesand.com | index"

    sections = ["work", "about", "contact"]

    return render_template("index.html", sections = sections)
