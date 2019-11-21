from keywords import KEYWORDS


urls = ['https://www.cnn.com/2019/05/08/us/denver-stem-shooting-heroes-run-hide-fight/index.html',
        'https://news.yahoo.com/nine-old-boy-charged-murder-074453202.html',
        'https://www.npr.org/2019/05/09/721893765/tense-u-s-china-trade-talks-underway-with-threat-of-tariffs-looming',
        'https://www.nytimes.com/2019/05/09/us/politics/trump-democrats-impeachment.html',
        'https://www.huffpost.com/entry/alabama-strict-abortion-law-felony_n_5cd44a1be4b054da4e857a4a?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuaHVmZnBvc3QuY29tLw&guce_referrer_sig=AQAAAKju1B-PF-hqdw_YS80hrmumVDdjcewTLcbmFMIRkDZzMxCa6Hz3A1Uy4zKvJ37d2ddIaUiuV42RV9dQ71WqyMVhIA88LzuklMlcf44jsPRC8vO_S7qT3GXDn4wqGHxRCLJ44oX0YfWnXutuPTb7FD2xve-adjS-AmN1M0izJmbs',
        'https://www.nbcnews.com/politics/congress/trump-impeachment-strategy-coming-together-pelosi-n1003981',
        'https://www.dailymail.co.uk/news/article-7010717/Fake-German-heiress-Anna-Sorokin-sentenced-four-12-years.html',
        'https://www.washingtonpost.com/technology/2019/05/09/food-delivery-freight-logistics-how-uber-aims-move-things-around-world/?utm_term=.0079ed751c9c',
        'https://www.theguardian.com/world/2019/may/09/north-korea-has-fired-second-projectile-in-five-days-says-south-korea',
        'https://www.wsj.com/articles/uber-prepares-for-ipo-at-midpoint-of-target-range-or-lower-11557422774?mod=hp_lead_pos1',
        'https://abcnews.go.com/US/guard-colorado-school-shooting-shot-deputies-wounded-student/story?id=62932261&cid=clicksource_4380645_null_hero_hed',
        'https://www.bbc.com/news/business-48217766',
        'https://www.usatoday.com/story/life/tv/2019/05/09/alex-trebek-pancreatic-cancer-cbs-sunday-morning-interview/1155575001/',
        'https://www.latimes.com/local/lanow/la-me-ln-saenz-arrest-gun-investigation-20190509-story.html',
        'https://www.foxnews.com/politics/two-years-after-getting-fired-by-trump-comeys-reign-at-fbi-remains-under-fire-amid-spygate',
        'https://www.aol.com/article/news/2019/05/09/two-students-arrested-in-school-shooting-appear-in-court/23723544/',
        'https://www.thedailybeast.com/stem-school-shooting-students-walk-out-of-vigil-organized-by-team-enough-and-moms-demand-action',
        'https://www.avclub.com/why-didn-t-daenerys-torch-euron-who-s-side-is-jaime-on-1834599395',
        'https://electrek.co/2019/05/09/tesla-saved-life-owner-crash-autopilot/',
        'https://io9.gizmodo.com/one-of-avengers-endgames-most-incredible-scenes-is-now-1834644122',
        'https://www.cbsnews.com/news/alabama-abortion-law-2019-chaos-on-senate-floor-today-while-state-lawmakers-debate-near-total-abortion-ban-2019-05-09/',
        'https://techcrunch.com/2019/05/09/blue-origin-unveils-its-lunar-lander-blue-moon/',
        'https://abc13.com/finance/walmart-managers-earn-$175000-a-year-on-average-report/5293048/',
        'https://www.theverge.com/2019/5/9/18563474/google-pixel-3a-xl-teardown-easy-repairs',
        'https://kotaku.com/the-final-fantasy-vii-remake-finally-re-emerges-1834654881',
        'https://www.polygon.com/2019/5/9/18543880/ghost-recon-breakpoint-release-date-announcement-livestream-pc-ps4-xbox-one']
# times = []
# for _ in range(10):
#start = time.time()
for url in urls:
    try:
        article = KEYWORDS(url)
    except:
        print('dumbass this is a bad url')

    k = article.get_keywords()
    for word in k:
        print(word)
