from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor

import tweepy
import numpy as np
import pandas as pd

CONSUMER_KEY = "XXXX"
CONSUMER_SECRET = "XXXX"
ACCESS_TOKEN = "XXXX"
ACCESS_TOKEN_SECRET = "XXXX"

### TWITTER CLIENT ###

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

### TWITTER AUTHENTICATOR ###

class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        # handles authentication and connection the Twitter streaming API
        try:
            auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            return auth
        except:
            print('ERROR: authentication failed')


### MAIN ###
if __name__ == '__main__':
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()

    dictionary = {
        "realDonaldTrump": "Right",
        "elonmusk": "Left",
        "neiltyson": "Middle",


    ### STARTING DATAFRAME FOR LABELING ###
    df = pd.DataFrame()
    block_acct = []
    empty _acct = []

    for key in dictionary:
        try:
            aff = dictionary.get(key, "Unknown")
            ### LIST OF A USER'S TWEETS ###
            tweets = api.user_timeline(screen_name=key, count=4,
                                       tweet_mode="extended", include_rts=False)
            ## LIST WITH TEXT OF USER TWEETS ###
            tmp = []
            for tweet in tweets:
                tmp.append([key, aff, tweet.full_text])
            if tmp:
                print('appending ...')
                df = df.append(tmp, ignore_index=True)
            else:
                No_tweets.append([outlet])

        except tweepy.TweepError:
            blocked_acct.append([key])
            print("Failed to run the command on that user, adding to blocked and Skipping...")

    pd.set_option("display.max_columns", 0)
    print(df)
