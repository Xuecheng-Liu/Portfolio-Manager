from flask import Flask, render_template, request

app = Flask(__name__)


# end point for the main page
@app.route("/")
def home():
    return render_template("home.html")


# endpoint for new investor
@app.route("/new")
def new():
    return render_template("new.html")


# endpoint for experienced investor
@app.route("/old", methods=["GET", "POST"])
def old():
    if request.method == "POST":
        print(request.form.getlist("sector"))
    return render_template("old.html")

# @app.route("/", methods=["GET", "POST"])
# def new2():
#     if request.method == "POST":
#         print(request.form.getlist("hello"))
#     return render_template("check.html")
