import pandas as pd
import nltk
from nltk.tag import pos_tag
import re
import numpy as np
from collections import Counter


class GROUP:

    # list of tweets and list of keywords that describes the group

    def __init__(self, tweet):
        self.tweets = []
        self.tweets.append(tweet)
        self.keywords = Counter(tweet.keywords).most_common(12)

    # add a tweet to the group
    def append_tweet(self, tweet):
        self.tweets = tweets.append(tweet)
        self.keywords = self.update_keywords(tweet)

    # update the group keywords based on the newest tweet
    def update_keywords(self, tweet):
        self.keywords += tweet.keywords
        return Counter(self.keywords).most_common(12)

    def get_total_tweets(self):
        return len(self.tweets)


class Tweet:
    # initialize
    def __init__(self, user, followers, text, creation, retweets, likes, hashtags, propnouns):
        self.user = user
        self.followers = followers
        self.text = text
        self.creation = creation
        self.retweets = retweets
        self.likes = likes
        self.hashtags = hashtags
        self.propnouns = propnouns
        self.keywords = self.get_keywords()

    # get keywords
    def get_keywords(self):
        tmp = []
        self.text = ' '.join(word for word in self.text.split(' ') if not word.startswith('http'))

        # remove stop words for some main words
        with open('newspaper3k/SmartStoplist.txt', 'r') as f:
            stopwords = [line.strip() for line in f]
        keywords = [word for word in self.text.split() if word not in stopwords]
        return keywords

    def get_propers(self):
        if len(self.propnouns):
            return (len(self.propnouns)*1.5)
        else:
            return 1

# proper noun boosts


def Boost():
    if len(self.propnouns):
        return (len(self.propnouns)*1.5)
    else:
        return 1


class GROUP_MASTER:
    def __init__(self, CSV_FILE):
        #self.data = pd.read_csv(CSV_FILE)
        self.all_groups = []
        self.start_grouping()

    def similarity(self, tweet_1, tweet_2):

        # Calculate Similarity score for each word in
        # tweet1 and tweet2 where tweet1 is compared
        # to entire database
        # summation (TF * IDF * BOOST)
        number_of_word_in_tweet = len(tweet2.split())
        for word in tweet_1.split():

            # Calculate TF
            occurence_of_word_in_tweet = sum(1 for _ in re.finditer(
                r'\b%s\b' % re.escape(word), tweet_2.lower()))
            TF = (occurence_of_word_in_tweet/number_of_word_in_tweet)

            # Calculate IDF
            count = 0
            total_tweets = self.total_tweets()
            for tweet in self.get_all_tweets_available():
                if word in tweet:
                    count += 1
            IDF = 1 + np.log((total_tweets / count))

            # Calculate Boost
            if word in tweet_1.propnouns:
                boost = 1.5
            else:
                boost = 1

            # multiply all and add to summation
            sim += (TF * IDF * boost)
        return sim

    # return total amount of tweets in all groups
    def total_tweets(self):
        for group in self.all_groups:
            total += group.get_total_tweets()
        return total

    # get a list of all tweets in all groups
    def get_all_tweets_available(self):
        tweets = []
        for group in self.all_groups:
            tweets = tweets.append(group.tweets)
            return tweets

    def assign_group(self, tweet):

        # if this is the first call to the function with first tweet and first group
        if not self.all_groups:
            group = GROUP(tweet)
            self.all_groups.append(group)

        # A group of some form exists
        else:

            # parsing over all the created groups
            for i in range(len(self.all_groups)):

                # get sim of tweet with first tweet of each group
                sim_1 = self.similarity(tweet, self.all_groups[i].tweets[0])
                # get sim of tweet with keywords of each group
                keywords = ' '.join(word[0] for word in self.all_groups[i].keywords)
                sim_2 = self.similarity(tweet, keywords)
                # get average similarity
                similarity = (sim_1 + sim_2) / 2
                print('tweet_1')
                print(tweet_1.text)
                print('tweet_2:')
                print(tweet_2.text)
                print('similarity:')
                print(similarity)


data = pd.read_csv('/Users/benjaminkolber/Desktop/test.csv')

for index, row in data.iterrows():
    # create a tweet object
    # user, followers, text, creation, retweets , likes, hashtags, pronouns
    tweet = Tweet(row['0'], row['1'], row['2'], row['3'],
                  row['4'], row['5'], row['6'], row['13'])
    print(tweet.hashtags)
