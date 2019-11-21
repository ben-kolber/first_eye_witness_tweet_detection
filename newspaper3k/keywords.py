
# use to import some important stuff to get nlp to work
# import nltk
# nltk.download('punkt')
import re
import time
from collections import Counter

# newspaper3k
# https://github.com/codelucas/newspaper
from newspaper import Article

# rake algorithm
# https://github.com/csurfer/rake-nltk
from rake_nltk import Metric, Rake

# Text rank algorithm
# https://github.com/summanlp/textrank
from summa import keywords
from summa.summarizer import summarize


class KEYWORDS:

    # create article obejct + parse
    def __init__(self, url):
        self.url = url
        self.article = Article(url)
        self.article.download()
        try:
            self.article.parse()
            self.article.nlp()
        except:
            print("ERROR: 404 PAGE")
            exit()
        self.check_if_valid()

    # check if url is valid for Civid Extension
    def check_if_valid(self):
        print('--------------------------------------')
        print(self.article.source_url)
        print('--------------------------------------')

        article_meta_data = str(self.article.meta_data).replace(" ", "")
        article_validation = "'type':'article'"

        if article_validation in article_meta_data:
            print("URL: VALID")
        else:
            print("It appears you are not reading a news article, care to use our search engine?")

    # Get all keywords
    def get_keywords(self):
        total_keyword_list = self.all_newspaper_keywords()
        total_keyword_list += self.rake()
        total_keyword_list += self.text_rank()
        # clean all stopwords + return most common
        return Counter(self.remove_stopwords(total_keyword_list)).most_common(8)

    # all newspaper3k keywords
    def all_newspaper_keywords(self):
        # newspaper3k extracted keywords
        newspaper_list = self.article.keywords

        # newspaper3k extracting meta data
        meta_keywords = self.article.meta_keywords
        meta = []
        if not meta_keywords:
            pass
        else:
            for phrase in meta_keywords:
                tmp = phrase.split()
                for word in tmp:
                    if(word.isdigit() == False):
                        word = word.replace(":", "")
                        meta.append(word.replace("'s", "").lower())

        newspaper_list += meta_keywords
        # newspaper3k title keywords
        title = self.article.title
        title_keywords = []
        tmp = title.split()
        for word in tmp:
            if(word.isdigit() == False):
                word = word.replace(":", "")
                title_keywords.append(word.replace("'s", "").lower())
        newspaper_list += title_keywords

        # meta description
        meta_description = self.article.meta_description.split()
        newspaper_list += Counter(self.remove_stopwords(meta_description)).most_common(10)
        return newspaper_list

    # implementation of textrank
    def text_rank(self):
        try:
            summa_keywords = keywords.keywords(self.article.text, words=10, split=True)
            summa_summarize = "".join(summarize(self.article.text, split=True))
            [x.lower() for x in summa_keywords]
            return summa_keywords
        except:
            print("ERROR: INVALID URL")
            exit()

    # implementation of rake
    def rake(self):

        r_1 = Rake(ranking_metric=Metric.WORD_DEGREE)
        r_2 = Rake(ranking_metric=Metric.WORD_FREQUENCY)

        # Extraction given the text.
        r_1.extract_keywords_from_text(self.article.text)
        r_2.extract_keywords_from_text(self.article.text)

        # To get keyword phrases ranked highest to lowest.
        r_1.get_ranked_phrases()
        r_2.get_ranked_phrases()

        # To get keyword phrases ranked highest to lowest with scores.
        list_1 = r_1.get_ranked_phrases()[:10]
        list_2 = r_2.get_ranked_phrases()[:10]

        # make a list of duplicates
        dups = set(list_1) & set(list_2)
        r_3 = Rake(ranking_metric=Metric.WORD_DEGREE)
        r_4 = Rake(ranking_metric=Metric.WORD_FREQUENCY)
        r_3.extract_keywords_from_sentences(dups)
        r_4.extract_keywords_from_sentences(dups)
        list_3 = r_3.get_ranked_phrases()[:10]
        list_4 = r_4.get_ranked_phrases()[:10]

        rake_keywords = []
        tmp_keywords = list(set(list_3) & set(list_4))
        for i in range(len(tmp_keywords)):
            tmp = tmp_keywords[i].split()
            for word in tmp:
                if "-" not in word:
                    rake_keywords.append(word.lower())

        return rake_keywords

    # remove stopwords
    def remove_stopwords(self, list):
        with open('SmartStoplist.txt', 'r') as f:
            stopwords = [line.strip() for line in f]
        return [word for word in list if word not in stopwords]
