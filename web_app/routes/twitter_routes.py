# web_app/routes/twitter_routes.py
from flask import Blueprint, render_template, jsonify
from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import twitter_api_client
from web_app.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

def store_twitter_user_data(screen_name):    
    '''get twitter user information
    '''
    api = twitter_api_client()
    twitter_user = api.get_user(screen_name)    
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    #rts: retweets    
    #return jsonify({"user": twitter_user._json, "tweets": [s._json for s in statuses]})
    '''store twitter user meta info in database
    '''
    # Initialize a new user in the database: check if twitter_user.id already exists the User db, otherwise use the twitter_user.id
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()
    '''get embedding for each tweet
    '''
    print("STATUS COUNT:", len(statuses))
    basilica_api = basilica_api_client()
    all_tweet_texts = [status.full_text for status in statuses]
    embeddings = list(basilica_api.embed_sentences(all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(embeddings))
     #todo: explore using the zip() function maybe...
    '''store all tweets and embeddings into database
    '''
    counter = 0
    for status in statuses:
        print(status.full_text)
        print("------------")
        #print(dir(status))

        # Find or create database tweet:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text
        #embedding = basilica_client.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
        embedding = embeddings[counter]
        print(len(embedding))
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        counter+=1
    db.session.commit()
    return db_user, statuses
    #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets

@twitter_routes.route("/users")
@twitter_routes.route("/users.json")
def list_users():
    db_users = User.query.all()
    users = parse_records(db_users)
    return jsonify(users)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    db_user, statuses = store_twitter_user_data(screen_name)
    # return "OK"
    return render_template("user.html", user=db_user, tweets=statuses)