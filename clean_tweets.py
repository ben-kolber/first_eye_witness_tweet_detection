import pandas as pd
import numpy as np
import re
import nltk
from nltk.tag import pos_tag
from nltk import PorterStemmer
from nltk import LancasterStemmer
from nltk.util import ngrams

class Tweet:
    # initialize
    def __init__(self, user, followers, text, creation, retweets, likes, hashtags, propnouns):
        self.user = user
        self.followers = followers
        self.text = text
        self.clean_text = self.clean_tweets(self.text)
        self.creation = creation
        self.retweets = retweets
        self.likes = likes
        self.hashtags = hashtags
        self.propnouns = propnouns
        self.keywords = self.get_keywords()
        self.bigrams = self.bigrams(self.clean_text)

    # get bigrams 
    def bigrams(self, text):
        return list(nltk.bigrams(text))

    # get keywords
    def get_keywords(self):
        tmp = []
        self.text = ' '.join(word for word in self.text.split(' ') if not word.startswith('http'))

        # remove stop words for some main words
        with open('newspaper3k/SmartStoplist.txt', 'r') as f:
            stopwords = [line.strip() for line in f]
        keywords = [word for word in self.text.split() if word not in stopwords]
        return keywords

    # get the number of propernouns found
    def get_len_propers(self):
        if len(self.propnouns):
            return len(self.propnouns)
        else:
            return 1

    # Clean the tweets only for relevant words.
    def clean_tweets(self, text):
        st = LancasterStemmer()
        #st = PorterStemmer()
        with open('newspaper3k/SmartStoplist.txt', 'r') as f:
            stopwords = [line.strip() for line in f]

            # remove URL's
            text = re.sub(r'http\S+', '', text)
            tweet_tmp = text.split("\n")
            for k in tweet_tmp:
                tweet_tmp = re.sub(r"[^a-zA-Z0-9]+", ' ', k).lower()
                tweet_tmp = st.stem(tweet_tmp)
            tweet_tmp = ''.join([i for i in tweet_tmp if not i.isdigit()])
            tweet_tmp = tweet_tmp.split()
            result = [word for word in tweet_tmp if word not in stopwords]
            return result


'''
data = pd.read_excel('/Users/benjaminkolber/Desktop/test.xlsx')

for index, row in data.iterrows():
    # create a tweet object
    # user, followers, text, creation, retweets , likes, hashtags, pronouns
    tweet = Tweet(row[0], row[1], row[2], row[3],
                  row[4], row[5], row[6], row[13])
    print(tweet.clean_text)
'''
