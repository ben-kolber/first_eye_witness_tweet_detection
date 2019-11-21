# from aho_corasick import KeywordTree
from ahocorapy.keywordtree import KeywordTree
from nltk.tag import pos_tag
from collections import Counter
import re

from keywords import KEYWORDS
import time
import pandas as pd
import numpy as np

## GET SOME KEYWORDS ##
start = time.time()
url = 'https://www.cnn.com/2019/05/15/success/wealth-coach-china-stocks/index.html'
article = KEYWORDS(url)
keywords = article.get_keywords()
for word in keywords:
    print(word)
end = time.time()
t = end - start
print(t)

tweets = ['Trumps trade wars are threatening to push the economy into a recession. His feud with China is driving up the prices of consumer goods and increasing the cost of inputs for the manufacturing sector. Its a dangerous combination.',
          'Walmart says higher China tariffs will increase prices for U.S. shoppers',
          'U.S. to begin testing sick, dead pigs for fatal hog virus ravaging China',
          'Every minute a garbage truck of plastic is dumped into the seas. We catch seafood equivalent to the weight of China every year. We need to change course.',
          '#China will never surrender to external pressure, a Foreign Ministry spokesperson said on Tuesday. "China doesnt want a trade war, but we are not afraid of fighting one. If someone brings the war to our doorstep, we will fight to the end.',
          'Farmer who voted for Trump says hes off the Trump train because of the trade war with China',
          'According to CCTV, soybean planting area has expanded in Heilongjiang, Chinas main grain producing province, this year. This farmer from Heilongjiang said now he has all his 100 hectares of land planting soybeans. Trade war becomes opportunity for Chinese soybean farmers.',
          'Trump has no clue how to negotiate trade with China or any other country. He has no idea how tariffs really work. He refuses to see how his ridiculous trade war will hurt average Americans.',
          'China has 51 female billionaires, South Korea has 1, Japan has none. And the answer might well be down to something Chairman Mao unintentionally set in motion',
          'President Trump today called his trade war with China a “little squabble.” It’s not a squabble, it’s a disaster with huge costs for California consumers, farmers and businesses. It’s time to stop holding American consumers and producers hostage as trade talks continue.',
          'All that President Trump has to do to win the Great Trade War with China is to give American farmers some tariff money to compensate them. Meanwhile, he can sit back & watch the tech industry get hammered - which they richly deserve. Thats called a win-win.',
          'The Trump admin has made $8,520,000,000 in direct payments to farmers through a 2018 aid program designed to counter losses stemming from Trumps trade war with China, Axios reports. ',
          'Farmer who voted for Trump says he’ll "never vote for him again" as family set to lose $150,000 in China trade war ',
          'Republicans borrowing another 20 billion dollars from China to pay farmers who cannot sell their products to China because of the trade war shows their loyalty to free market principals wait a second I don’t get it.',
          'Trump lost 5 points on Rasmussen in the past 3 days.  Im guessing delayed reaction to people not understanding the trade war with China and the one day stock selloff.',
          'BREAKING NEWS: Chinese people rush to buy $3 Donald Trump toilet brushes amid trade war with the U.S. & joke Trump can be so useful. People in China are cheering for Beijing in a trade war with Washington by cleaning their toilets with brushes that look like the U.S. President. ',
          'Most Chinese agree that the US is more powerful than China and Washington holds initiative in the trade war. But we just dont want to cave in and we believe there is no way the US can crush China. We are willing to bear some pain to give the US a lesson.',
          'China will fight to the end if President Trumps trade war continues says Beijings ambassador to the UK as he calls Americans troublemakers who are fixated on us first',
          'My discussion with soybean farmer and Wisconsin Soybean Association president Tony Mellenthin @MellenthinFarms about how the trade war with China is currently affecting farmers, and what happens once it is over. ']


# AHO - CORASICK #
kwtree = KeywordTree(case_insensitive=True)

df = pd.DataFrame()
matches = []
tmp = []
clean_keywords = []
# Add keywords to the trie
for word in keywords:
    kwtree.add(word[0])
    clean_keywords.append(word[0])
kwtree.finalize()


# Run a search on every tweet and add to dataframe

for i in range(len(tweets)):
    matches = []
    tmp = []

    # remove all special charactets
    for k in tweets[i].split("\n"):
        tweet = re.sub(r"[^a-zA-Z0-9]+", ' ', k).lower()
    results = kwtree.search_all(tweet)

    # match results
    for result in results:
        matches.append(result)

    # grab proper nouns from tweet to raise relevance score
    tagged_sent = pos_tag(tweets[i].split())
    propernouns = [re.sub('[^A-Za-z0-9]+', '', word).lower()
                   for word, pos in tagged_sent if pos == 'NNP']

    propers = list(set(propernouns) & set(clean_keywords))

    # relevance score : matches(+1) + propernoun mathches(+1.5) / 20 (max 8 + 12)
    relevance = (float(len(matches)) + float(len(propers)) * 1.5)

    # all data on search result per tweet
    tmp.append(["{} {}".format("Twt #", i), "{} {}".format(
        "Hts:", len(matches)), "{} {}".format("NNP #", len(propers)),
        "{} {}".format("RLV #", relevance), matches])

    # add to data frame tweet, number of matches and words that matched.
    df = df.append(tmp, ignore_index=True)

print(df.to_string(index=False))
