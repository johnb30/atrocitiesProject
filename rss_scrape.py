from apscheduler.scheduler import Scheduler
#from joblib import Parallel, delayed
from pymongo import MongoClient
from corenlp import StanfordCoreNLP
import time
import logging
import datetime
import pattern.web
import nltk.data
import pages_scrape
import mongo_connection

# In the scrape_func, if 'keep' will only have 1 word make it a list, else a
# tuple.

# If 'keep' is more than one word, change the 'all()' to 'any() and all()'
#since the desired behavior is to have any of the keep and none of the ignore.


def scrape_func(address, website):
    """
    Function to scrape various RSS feeds. Uses the 'keep' and 'ignore'
    iterables to define which words should be used in the text search.

    Inputs
    ------
    address : address for the RSS feed to scrape. String.

    website : name of the website to scrape to be used in the filepath for the
    output. String.

    database : name of the MongoDB database that contains the collections.
    String? pymongo connection object?
    """
    connection = MongoClient()
    db = connection.atrocities_data
    collection = db[website]

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

    corenlp_dir = 'stanford-corenlp/'
    corenlp_parse = StanfordCoreNLP(corenlp_dir)

    log = open('log_file.txt', 'a')
    results = pattern.web.Newsfeed().search(address, count=100, cached=False)
    log1 = 'There are %d results from %s \n' % (len(results), website)
    log.write(log1)
    for result in results:
        if website == 'nyt':
            text = pages_scrape.scrape(result.url, result.title)
            head_sentences = sent_detector.tokenize(text.strip())[:4]
            joined_sentences = ' '.join(head_sentences)
            parsed = corenlp_parse.raw_parse(joined_sentences)
            entry_id = mongo_connection.add_entry(collection, text, parsed,
                                                    result.title, result.url,
                                                    result.date, website)
            if entry_id:
                log2 = 'Added entry from %s with id %s \n' % (result.url,
                                                                str(entry_id)
                                                                )
                log.write(log2)
            else:
                log2 = 'Result from %s already in database \n' % (result.url)
                log.write(log2)
        if website == 'bbc':
            text = pages_scrape.scrape(result.url, result.title)
            head_sentences = sent_detector.tokenize(text.strip())[:4]
            joined_sentences = ' '.join(head_sentences)
            parsed = corenlp_parse.raw_parse(joined_sentences)
            entry_id = mongo_connection.add_entry(collection, text, parsed,
                                                    result.title, result.url,
                                                    result.date, website)
            if entry_id:
                log2 = 'Added entry from %s with id %s \n' % (result.url,
                                                                str(entry_id)
                                                                )
                log.write(log2)
            else:
                log2 = 'Result from %s already in database \n' % (result.url)
                log.write(log2)
        if website == 'reuters':
            text = pages_scrape.scrape(result.url, result.title)
            head_sentences = sent_detector.tokenize(text.strip())[:4]
            joined_sentences = ' '.join(head_sentences)
            parsed = corenlp_parse.raw_parse(joined_sentences)
            entry_id = mongo_connection.add_entry(collection, text, parsed,
                                                    result.title, result.url,
                                                    result.date, website)
            if entry_id:
                log2 = 'Added entry from %s with id %s \n' % (result.url,
                                                                str(entry_id)
                                                                )
                log.write(log2)
            else:
                log2 = 'Result from %s already in database \n' % (result.url)
                log.write(log2)
        if website == 'ap':
            text = pages_scrape.scrape(result.url, result.title)
            head_sentences = sent_detector.tokenize(text.strip())[:4]
            joined_sentences = ' '.join(head_sentences)
            parsed = corenlp_parse.raw_parse(joined_sentences)
            entry_id = mongo_connection.add_entry(collection, text, parsed,
                                                    result.title, result.url,
                                                    result.date, website)
            if entry_id:
                log2 = 'Added entry from %s with id %s \n' % (result.url,
                                                                str(entry_id)
                                                                )
                log.write(log2)
            else:
                log2 = 'Result from %s already in database \n' % (result.url)
                log.write(log2)
        if website == 'upi':
            text = pages_scrape.scrape(result.url, result.title)
            head_sentences = sent_detector.tokenize(text.strip())[:4]
            joined_sentences = ' '.join(head_sentences)
            parsed = corenlp_parse.raw_parse(joined_sentences)
            entry_id = mongo_connection.add_entry(collection, text, parsed,
                                                    result.title, result.url,
                                                    result.date, website)
            if entry_id:
                log2 = 'Added entry from %s with id %s \n' % (result.url,
                                                                str(entry_id)
                                                                )
                log.write(log2)
            else:
                log2 = 'Result from %s already in database \n' % (result.url)
                log.write(log2)
        if website == 'xinhua':
            page_url = result.url.encode('ascii')
            page_url = page_url.replace('"', '')
            text = pages_scrape.scrape(page_url, result.title)
            head_sentences = sent_detector.tokenize(text.strip())[:4]
            joined_sentences = ' '.join(head_sentences)
            parsed = corenlp_parse.raw_parse(joined_sentences)
            entry_id = mongo_connection.add_entry(collection, text, parsed,
                                                    result.title, result.url,
                                                    result.date, website)
            if entry_id:
                log2 = 'Added entry from %s with id %s \n' % (result.url,
                                                                str(entry_id)
                                                                )
                log.write(log2)
            else:
                log2 = 'Result from %s already in database \n' % (result.url)
                log.write(log2)
        if website == 'google':
            text = pages_scrape.scrape(result.url, result.title)
            head_sentences = sent_detector.tokenize(text.strip())[:4]
            joined_sentences = ' '.join(head_sentences)
            parsed = corenlp_parse.raw_parse(joined_sentences)
            entry_id = mongo_connection.add_entry(collection, text, parsed,
                                                    result.title, result.url,
                                                    result.date, website)
            if entry_id:
                log2 = 'Added entry from %s with id %s \n' % (result.url,
                                                                str(entry_id)
                                                                )
                log.write(log2)
            else:
                log2 = 'Result from %s already in database \n' % (result.url)
                log.write(log2)
    interupt = '+' * 70
    log3 = '%s\nScrape %s once at %s!\n%s\n' % (interupt, website,
                                                datetime.datetime.now(),
                                                interupt)
    log.write(log3)
    log.close()


def call_scrape_func(siteList):
    for website in siteList:
        scrape_func(siteList[website], website)
    print 'Scraped at %s' % datetime.datetime.now()

if __name__ == '__main__':
    print 'Running...'
    to_scrape = {'google': 'https://news.google.com/?output=rss',
                 'nyt': 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                 'reuters': 'http://feeds.reuters.com/Reuters/worldNews',
                 'bbc': 'http://feeds.bbci.co.uk/news/world/rss.xml',
                 'ap': 'http://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5',
                 'upi': 'http://rss.upi.com/news/emerging_threats.rss',
                 'xinhua': 'http://www.xinhuanet.com/english/rss/worldrss.xml'
                 }
    #Line to aid in debugging
    call_scrape_func(to_scrape)

#    logging.basicConfig()
#
#    sched = Scheduler()
#    sched.add_interval_job(call_scrape_func, args=[to_scrape], hours=1)
#    sched.start()
#    while True:
#        time.sleep(10)
#    sched.shutdown()
