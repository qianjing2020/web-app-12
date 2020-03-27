# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("Visited the home page.")
    return render_template("prepare_to_predict.html")

@home_routes.route("/hello")
# replaced @app.route("/")
# So, instead of attaching to app, we attach the route definition to a blueprint object
def hello():
    return "Hello World!"

@home_routes.route("/about")
def about():
    return "About me"