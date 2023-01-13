import tweepy_test
import tweepy

def tweepy_auth(API_KEY,API_SECRET,ACCESS_TOKEN, ACCESS_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def retweet_favorites(api, username):
    for tweet in api.get_favorites(screen_name=username):
        try:
            api.retweet(tweet.id)
        except tweepy.errors.TweepyException as e:
            print(e)
    return print("done")