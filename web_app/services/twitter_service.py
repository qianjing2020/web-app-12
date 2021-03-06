# web_app/services/twitter_service.py
import tweepy
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY", default="OOPS")
consumer_secret = os.getenv("TWITTER_API_SECRET", default="OOPS")
access_token = os.getenv("TWITTER_ACCESS_TOKEN", default="OOPS")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", default="OOPS")


def twitter_api_client():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print("AUTH", type(auth))

    api = tweepy.API(auth)
    return api

api = twitter_api_client()
pprint(dir(api))
#breakpoint()

""" # get a collection of public tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
   print(tweet.text)
 """
 
# get one user's twit information
screen_name = "elonmusk"
print("--------------")
print("USER...")
user = api.get_user(screen_name)
print(type(user))  # > <class 'tweepy.models.User'>
print(user.screen_name)
print(user.followers_count)
pprint(user._json)
print("--------------")
print("STATUSES...")
# get that user's tweets:
# see: http://docs.tweepy.org/en/latest/api.html#API.user_timeline
statuses = api.user_timeline(
    screen_name,
    tweet_mode="extended",
    count = 150, exclude_replies = True, include_rts = False)
    
for status in statuses:
    print(type(status))  # > <class 'tweepy.models.Status'>
    # pprint(status._json)
    # breakpoint()
    print(status.full_text)
 