from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from nltk.tag import pos_tag
import re
import json
import unicodedata
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

    ### STARTING DATAFRAME FOR LABELING ###
    data = pd.read_excel('/Users/benjaminkolber/Desktop/grouping_media_users.xlsx')
    media = list(data['Media'])
    media += list(data['Journalists'])

    df = pd.DataFrame([['user', 'followers', 'text', 'created_at',
                        'retweets', 'likes', 'hashtags', 'URLs', 'user mentions',
                        '#breaking', '#breakingnews', '#news', 'propnouns_count', 'propnouns']])

    blocked_acct = []
    No_tweets = []
    for outlet in media[:5]:
        print('INIT Scraping : ')
        print(outlet)
        try:
            ### LIST OF A USER'S TWEETS ###
            tweets = api.user_timeline(screen_name=outlet, count=40,
                                       tweet_mode="extended", include_rts=False)
            ## LIST WITH TEXT OF USER TWEETS ###
            tmp = []
            for tweet in tweets:
                print('parsing tweet ... ')

                # check for proper nouns
                tagged_sent = pos_tag(tweet.full_text.split())

                with open('weirdchars.txt', 'r') as f:
                    weirdos = [line.strip() for line in f]

                for word in weirdos:
                    tweet.full_text = tweet.full_text.replace(word, '')
                propernouns = [re.sub('[^A-Za-z0-9]+', '', word).lower()
                               for word, pos in tagged_sent if pos == 'NNP']

                breakingnews = False
                breaking = False
                news = False
                # Check for hashtags

                if '#breakingnews' in tweet.full_text.lower():
                    breakingnews = True
                if '#breaking' in tweet.full_text.lower():
                    breaking = True
                if '#breakingnews' in tweet.full_text.lower():
                    news = True

                tweet.full_text = str(tweet.full_text.encode("utf-8"))
                unicodedata.normalize(
                    'NFKD', tweet.full_text).encode('ascii', 'ignore')

                # appending all data to df
                tmp.append([tweet.user.name, tweet.user.followers_count,
                            tweet.full_text, tweet.created_at, tweet.retweet_count, tweet.favorite_count,
                            tweet.entities['hashtags'], tweet.entities['urls'], tweet.entities['user_mentions'],
                            breaking, breakingnews, news, len(propernouns), propernouns])
            print('checking for non null ... ')
            if tmp:
                print('appending ...')
                df = df.append(tmp, ignore_index=True)
            else:
                No_tweets.append([outlet])

        except tweepy.TweepError:
            blocked_acct.append([outlet])
            print("Failed to run the command on that user, adding to blocked and Skipping...")

    pd.set_option("display.max_columns", 0)
    df.to_csv('/Users/benjaminkolber/Desktop/test.csv')

    print('DONE SCRAPING')
    print('Total Scraped:')
    print(df.size)
    print('------------------')
    print('Blocked accounts:')
    print(blocked_acct)
    print('------------------')
    print('Handlers with no tweets')
    print(No_tweets)
    print('------------------')
