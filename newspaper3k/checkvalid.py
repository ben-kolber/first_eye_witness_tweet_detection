from newspaper import Article

good_urls = ['https://www.cnn.com/2019/05/08/us/denver-stem-shooting-heroes-run-hide-fight/index.html',
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

bad_urls = ['https://stackoverflow.com/questions/38695194/search-for-word-in-text-file-in-python',
            'https://www.crummy.com/software/BeautifulSoup/bs4/doc/',
            'https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe',
            'https://www.quora.com/What-is-perfectly-legal-but-creepy-as-hell',
            'https://elemental.medium.com/why-exercisers-are-embracing-cannabis-96317907bb4c',
            'https://www.linkedin.com/in/joshuakaminetsky/',
            'https://www.debate.org/forums/debate.org/topic/4341085/',
            'https://www.debateart.com/participants/bsh1',
            'https://en.wikipedia.org/wiki/Death_Proof',
            'https://www.mako.co.il/',
            'https://techcrunch.com/',
            'https://www.cnn.com/',
            'https://www.coolmathgames.com/',
            'https://www.amazon.com/Limited-Thrones-Classic-Chocolate-Sandwich/dp/B07QGX1791?pf_rd_p=0fc3f2c4-3ed5-4d11-9995-8d7c82394713&pd_rd_wg=QHl4R&pf_rd_r=9KSW314DZ3B6CFH8XFXX&ref_=pd_gw_cr_simh&pd_rd_w=uOJhT&pd_rd_r=aed01cc8-878b-4135-b355-85b54db183e5',
            'https://trailers.apple.com/',
            'https://www.google.com/search?q=google&oq=google&aqs=chrome..69i57j69i60l3j69i65l2.1030j0j4&sourceid=chrome&ie=UTF-8',
            'https://www.cnn.com/specials/about-live-tv',
            'https://www.foxnews.com/',
            'https://nation.foxnews.com/personalities/bill-bennett/?cmpid=org=NAT::ag=owned::mc=FNC_display::src=FNC_web::cmp=video_driver::add=watch_platform_vd_creative',
            'https://www.youtube.com/watch?v=RrkL9e2w7gQ',
            'https://www.google.com/search?q=elon+musk&safe=active&source=lnms&tbm=nws&sa=X&ved=0ahUKEwifu_GClrDiAhWvwFkKHfHWDi8Q_AUIDigB&biw=1863&bih=1016',
            'https://www.tesla.com/elon-musk',
            'https://www.fiverr.com/?utm_source=40917&utm_medium=cx_affiliate&utm_campaign=&cxd_token=40917_1058601_webhost&show_join=true',
            'https://seekingalpha.com/article/4265387-micron-technology-chapter-3-parabellum',
            'https://www.bose.com/en_us/products/headphones/over_ear_headphones/quietcomfort-35-ii-wireless-custom.html?EarCap=tna-gloss']

def isValid(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
    except:
        print('ERROR WITH URL')

    article_meta_data = str(article.meta_data).replace(" ", "")
    article_validation = "'type':'article'"

    print('--------------------------------------')
    print(article.source_url)
    print('--------------------------------------')
    if article_validation in article_meta_data:
        return 'VALID ARTICLE!'
    else:
        return 'INVALID ARTICLE -> FuCk oFF'

for url in good_urls:
    print(isValid(url))

for url in bad_urls:
    print(isValid(url))
