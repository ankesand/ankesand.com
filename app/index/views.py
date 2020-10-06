from app import app
from flask import render_template, request, url_for, redirect

@app.route("/")
def index():

    title = "ankesand.com | index"

    sections = ["work", "about", "contact"]

    return render_template("index.html", sections = sections)

#
# future views (per menus - base.html)
#

@app.route("/index/login")
# def login():
def index_login():

    title = "ankesand.com | index - login"

    return "[index/login]"

#
# work
#

@app.route("/work")
def work():

    title = "ankesand.com | work"

    return "[work]"

@app.route("/work/financial")
def financial():

    title = "ankesand.com | work - financial"

    return "[work/financial]"

@app.route("/work/web-scraping")
def web_scraping():

    title = "ankesand.com | work - web-scraping"

    return "[work/web-scraping]"

@app.route("/work/sport")
def sport():

    title = "ankesand.com | work - sport"

    return "[work/sport]"

@app.route("/work/jupyter-notebooks")
def jupyter_notebooks():

    title = "ankesand.com | work - jupyter-notebooks"

    return "[work/jupyter-notebooks]"

@app.route("/work/apis")
def apis():

    title = "ankesand.com | work - apis"

    return "[work/apis]"

#
# about
#

@app.route("/about")
def about():

    title = "ankesand.com | about"

    return "[about]"

@app.route("/about/profile")
def profile():

    title = "ankesand.com | about - profile"

    return "[about/profile]"

@app.route("/about/stack")
def stack():

    title = "ankesand.com | about - stack"

    return "[about/stack]"

@app.route("/about/blog")
def blog():

    title = "ankesand.com | about - blog"

    return "[about/blog]"

@app.route("/about/background")
def background():

    title = "ankesand.com | about - background"

    return "[about/background]"
@app.route("/about/cv-resume")
def cv_resume():

    title = "ankesand.com | about - cv-resume"

    return "[about/cv-resume]"

#
# contact
#

@app.route("/contact")
def contact():

    title = "ankesand.com | contact"

    return "[contact]"

@app.route("/contact/email")
def email():

    title = "ankesand.com | contact - email"

    return "[contact/email]"

@app.route("/contact/github")
def github():

    title = "ankesand.com | contact - github"

    return "[contact/github]"

@app.route("/contact/twitter")
def twitter():

    title = "ankesand.com | contact - twitter"

    return "[contact/twitter]"

@app.route("/contact/linkedin")
def linkedin():

    title = "ankesand.com | contact - linkedin"

    return "[contact/linkedin]"
