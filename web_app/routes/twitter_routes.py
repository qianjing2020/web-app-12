# web_app/routes/twitter_routes.py
from flask import Blueprint, render_template, jsonify
# from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import twitter_api_client
# from web_app.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    
    api = twitter_api_client()
    twitter_user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False) #rts: retweets
    
    return jsonify({"user": twitter_user._json, "tweets": [s._json for s in statuses]})
    