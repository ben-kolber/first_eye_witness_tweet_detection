from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from itertools import product
import pandas as pd
import numpy
import re
from nltk.tag import pos_tag
from clean_tweets import Tweet


def similarity(str1, str2):
    
    #Defining stopwords for English Language
    stop_words = set(stopwords.words("english"))
    
    #Initialising Lists
    filtered_sentence1 = []
    filtered_sentence2 = []
    lemm_sentence1 = []
    lemm_sentence2 = []
    sims = []
    temp1 = []
    temp2 = []
    simi = []
    final = []
    same_sent1 = []
    same_sent2 = []
    #ps = PorterStemmer()

    #Defining WordNet Lematizer for English Language
    lemmatizer = WordNetLemmatizer()

    #myfile =  open('Text1.txt', 'r')
    #data=myfile.read().replace('\n', '')
    # print(sent_tokenize(example_text))
    ##
    # print(word_tokenize(example_text))

    #Tokenizing and removing the Stopwords
    for words1 in word_tokenize(str1):
        if words1 not in stop_words:
            if words1.isalnum():
                filtered_sentence1.append(words1)

    #Lemmatizing: Root Words
    for i in filtered_sentence1:
        lemm_sentence1.append(lemmatizer.lemmatize(i))

    # print(lemm_sentence1)

    # Tokenizing and removing the Stopwords
    for words2 in word_tokenize(str2):
        if words2 not in stop_words:
            if words2.isalnum():
                filtered_sentence2.append(words2)

    #Lemmatizing: Root Words
    for i in filtered_sentence2:
        lemm_sentence2.append(lemmatizer.lemmatize(i))

    # print(lemm_sentence2)

    ##---------------Removing the same words from the tokens----------------##
    # for word1 in lemm_sentence1:
    # for word2 in lemm_sentence2:
    # if word1 == word2:
    # same_sent1.append(word1)
    # same_sent2.append(word2)
    ##
    # if same_sent1 != []:
    # for word1 in same_sent1:
    # lemm_sentence1.remove(word1)
    # if same_sent2 != []:
    # for word2 in same_sent2:
    # lemm_sentence2.remove(word2)
    ##
    # print(lemm_sentence1)
    # print(lemm_sentence2)

    #Similarity index calculation for each word
    for word1 in lemm_sentence1:
        simi = []
        for word2 in lemm_sentence2:
            sims = []
           # print(word1)
            # print(word2)
            syns1 = wordnet.synsets(word1)
            # print(syns1)
            # print(wordFromList1[0])
            syns2 = wordnet.synsets(word2)
            # print(wordFromList2[0])
            for sense1, sense2 in product(syns1, syns2):
                d = wordnet.wup_similarity(sense1, sense2)
                if d != None:
                    sims.append(d)

            # print(sims)
            # print(max(sims))
            if sims != []:
                max_sim = max(sims)
                # print(max_sim)
                simi.append(max_sim)

        if simi != []:
            max_final = max(simi)
            final.append(max_final)

    # print(final)

    #        if max_sim >= 0.7:
    #           print(word1)
    #           print(word2)
    #           print('\n')

    #           if word1 not in temp1:
    #              temp1.append(word1)
    #           if word2 not in temp2:
    #              temp2.append(word2)
            # lemm_sentence1.remove(word1)
            # lemm_sentence2.remove(word2)
            # if wordFromList1 and wordFromList2: #Thanks to @alexis' note
            #  s = wordFromList1[0].wup_similarity(wordFromList2[0])
            # list.append(s)
    # for word1 in temp1:
    #    lemm_sentence1.remove(word1)

    # for word2 in temp2:
    #    lemm_sentence2.remove(word2)

    # print(lemm_sentence1)
    # print(lemm_sentence2)

    #Final Output

    similarity_index = numpy.mean(final)
    similarity_index = round(similarity_index, 2)
    print("Sentence 1: ", str1)
    print("Sentence 2: ", str2)
    print("Similarity index value : ", similarity_index)
    return similarity_index

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
        sim = similarity(tweet, comparator)

        # get sim of tweet with keywords of each group
        tmp.append([tweet, comparator, tmp_tweet, tester, sim])
        print('basis tweet:')
        print(tweet)
        print('Being compared to:')
        print(tester)
        print('with a comparisson score of:')
        print(sim)
        print('----------------------------------------')

df = df.append(tmp, ignore_index=True)
df.columns = ['basis', 'comparator', 'basis keywords',
              'comparator keywords', 'similarity score', 'matches', 'matches']

df.to_csv('/Users/benjaminkolber/Desktop/output_ML_NOT_CLEAN.csv')
