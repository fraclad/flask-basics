from app import app
from flask import render_template, request, redirect
from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    my_name = "Budiman"

    age = 10

    langs = ["Python", "R", "C++", "MATLAB"]

    friends = {
        "Dude":30,
        "Bruh":45,
        "minor": 12
    }

    colors = ('beige', 'yellow')

    cool = True

    class GitRemote:
        def __init__(self, name, desc, url) -> None:
            self.name = name
            self.desc = desc
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name = "Flask Jinja", 
        desc = "template design for class",
        url = "www.yeetlmaobruh.co.id"
    )

    def repeat(x, qty):
        return x * qty

    date = datetime.utcnow()

    my_html = "<h1>THIS IS SOME HTML</h1>"


    return render_template(
        "public/jinja.html", my_name = my_name, age = age, 
        langs = langs, friends = friends, colors = colors, 
        cool = cool, GitRemote = GitRemote, my_remote = my_remote,
        repeat = repeat, date = date, my_html = my_html)

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/sign-up", methods = ["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form

        username = req["username"]
        email = req["email"]
        password = req["password"]

        print(username, email, password)

        return redirect(request.url)

    return render_template("public/sign_up.html")