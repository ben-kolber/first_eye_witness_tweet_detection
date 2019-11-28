import pandas as pd
import numpy as np
import re
from nltk.tag import pos_tag
from clean_tweets import Tweet

# Calculate Similarity score for each word in
# tweet1 and tweet2 where tweet1 is compared
# to entire database
# summation (TF * IDF * BOOST)
def similarity(tweet_1, tweet_2, all_tweets, propernouns, bigrams_1, bigrams_2):
    number_of_word_in_tweet = len(tweet_2)
    sim = 0.0
    occurence = 0.0
    boost = 1.0
    match = 0.0
    matches = []
    for word in tweet_1:

        # Calculate TF
        occurence_of_word_in_tweet_2 = tweet_2.count(word)
        if occurence_of_word_in_tweet_2:
            match += 1
            matches.append(word)
        TF = (occurence_of_word_in_tweet_2/len(tweet_2))

        # Calculate IDF and boost
        N = len(all_tweets)
        for tweet in all_tweets:
            if word in tweet.clean_text:
                occurence += 1

        # calculate the boost
        if word in propernouns:
            boost = 2
        else:
            boost = 1

            # IDF calculation
        IDF = (1 + np.log((N/occurence)))
        sim += (TF*IDF*boost)

    # compare bigrams
    bigrams = 1
    common = []
    for gram in bigrams_1:
        if gram in bigrams_2:
            common.append(gram)
            bigrams += 1.5

    if match == 2:
        return sim*2.0 * bigrams, match, matches, common

    elif match == 3:
        return sim*2.0*bigrams, match, matches, common

    elif match >= 4:
        return sim*3.0*bigrams, match, matches, common
    else:
        return sim*bigrams, match, matches, common


data = pd.read_excel('/Users/benjaminkolber/Desktop/test_data_for_comparisson.xlsx')
tmp = []
tweets = []
for index, row in data.iterrows():
    # create a tweet object
    # user, followers, text, creation, retweets , likes, hashtags, pronouns
    tweet = Tweet('1', '1', row[0], '1', '1', '1', '1', '1')
    tweets.append(tweet)

df = pd.DataFrame()
for i in range(len(tweets)):

    tweet = tweets[i].text    # actual tweet
    tmp_tweet = tweets[i].clean_text   # clean tweet

    tagged_sent = pos_tag(tweet.split())
    propernouns = [re.sub('[^A-Za-z0-9]+', '', word).lower()
                   for word, pos in tagged_sent if pos == 'NNP']

    for j in range(len(tweets)):  # test tweets[i] against all tweets in list
        comparator = tweets[j].text
        tester = tweets[j].clean_text
        sim, matches_len, matches, bigrams = similarity(
            tmp_tweet, tester, tweets, propernouns, tweets[i].bigrams, tweets[j].bigrams)

        # get sim of tweet with keywords of each group

        tmp.append([tweet, comparator, tmp_tweet, tester, sim,
                    matches_len, matches, bigrams, tweets[i].bigrams])
        print('basis tweet:')
        print(tweet)
        print('Being compared to:')
        print(tester)
        print('with a comparisson score of:')
        print(sim)
        print('----------------------------------------')

df = df.append(tmp, ignore_index=True)
df.columns = ['basis', 'comparator', 'basis keywords',
              'comparator keywords', 'similarity score', 'matches', 'matches', 'bigrams', 'bigrams']

df.to_csv('/Users/benjaminkolber/Desktop/output_TF_IDF_BOOST.csv')
