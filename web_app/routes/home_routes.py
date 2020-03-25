# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
# replaced @app.route("/")
# So, instead of attaching to app, we attach the route definition to a blueprint object
def index():
    return "Hello World!"

@home_routes.route("/about")
def about():
    return "About me"