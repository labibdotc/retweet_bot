import tweepy
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# tweet_list = api.get_favorites(screen_name="aka_labib",count=5)
# user = api.get_user(screen_name="aka_labib")
# print(tweet_list)
# for tweet in tweet_list:
#     print(tweet.id)

# tweet_id = 1613232769823301632
# api.retweet(tweet_id)

for tweet in api.get_favorites(screen_name="aka_labib"):
    try:
        api.retweet(tweet.id)
    except tweepy.errors.TweepyException as e:
        print(e)