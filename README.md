
# Detecting First Eye Witness Tweets and Creating a Thread of Similar Tweets. 
The idea behind this project was detecting natural disasters before they hit the media from tweets all around the world. tweets were scraped from targeted active twitter users. Their tweets were preprocessed and then run through several ML algorithms. 

## Introduction 
  1. Scrape tweets from Twitter
  2. Detect first eye witness tweets for natural disasters
  3. Group together similar tweets i.e tweets relating to the same natural disaster
  4. Find related articles using newspaper3K
  
## Getting User Timeline Tweets using Tweepy
Get access tokens from Twitter to use their API for scraping data. Once all access tokens are received, simply list the twitter handles in the 'dictionary'. Running the program will retrieve real time tweets for the specified users timeline. 

simple_tweet_scraper.py : Tweet simple scraper
tweet_scraper_for_grouping.py : Scrapes additional data about each tweet (likes, followers, shares ...) and appends them to a data frame for further processing. 
clean_tweets.py : processes the tweet by extracting keywords, removing stopwords and stemming the tweet for further processing. 

## Grouping 
Different implementation to group together tweets given a similarity score. 
sim_1 : lammatization, wordnet and propernouns 
sim_2 : pos tagging, propernouns, TF-IDF, boosting
sim_3 : bigrams, trigrams, boosting, TF-IDF, common words, propernouns, 

# Aho Corasik Search 
Run an Aho-Corasik search on each tweet based on a list of keywords that would indicate the level of confidence in a first eye witness tweet for a natural disaster. 
The Aho-Corasik automaton is 'filled' with words in a trie structure, then run on each sentence. For each word matches, a count is kept for both the number of matches and the category in which the match occured. The resulting DF is pickled. 

aho_corasik_filter_words : word bank

# First Eye Witness Tweets : tweetClassifier.py
Given a DF of a bunch of features of a tweet (likes, aho-corasik results, grouping similarities... ) the following process takes place. 
  1. All contractions are extrapolated (ain't = am not / are not) ...
  2. Database of tweets is loaded, which are tagged as 'relevant tweet' and 'irelevant tweet', with features such as is_first_person, is_suffering, is_current ... data taken into account from the aho- corasik search. 
  3. The tweets are split into training and testing sets. 
  4. several ML models are trained on the tweets, such as Logistic regression, Support Vector Machine, K nearest neighbor ...
  5. The test tweets are run through the models and produce a list of accuracy of each trained model on the tested tweets.
  
  
## Newspaper3K
Using the newspaper3k package, the programs simply check validity of article URL's, can search through articles for given keywods and bigrams from tweets, and basically given a relevant tweet, and article will be found. 
  
## Acknowlegements 
Finding Eyewitness Tweets During Crises
Fred Morstatter, Nichola Lubold, Heather Pon-Barry, Ju ̈rgen Pfeffer, and Huan Liu

Understanding Eyewitness Reports on Twitter During Disasters
Kiran Zahra, Muhammad Imran, Frank O. Ostermann


