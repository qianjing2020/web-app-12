# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db
from web_app.routes.twitter_routes import store_twitter_user_data 

admin_routes = Blueprint("admin_routes", __name__)

#ideally be password protected
@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    # db.create_all() does all the flask db init, migrate, upgrade
    return jsonify({"message": "DB RESET OK"})

@admin_routes.route("/admin/db/seed")
def seed_db():
    print(type(db))
    # TODO: refactor the existing user and tweet storage logic from our twitter_routes into a re-usable function
    # ... so we can "seed" our database with some example users and tweets
    # ... to ensure that it is ready to make predictions later
    default_users = ["elonmusk", "justinbieber", "abcnews"]
    for screen_name in default_users:
        db_user, statuses = store_twitter_user_data(screen_name)
    
    return jsonify({"message": f"DB SEEDED OK (w/ {len(default_users)})"})