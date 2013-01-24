from apscheduler.scheduler import Scheduler
#from joblib import Parallel, delayed
from pymongo import MongoClient
import pattern.web 
import time
import pages_scrape
import mongo_connection
import logging

# In the scrape_func, if 'keep' will only have 1 word make it a list, else a
# tuple.

# If 'keep' is more than one word, change the 'all()' to 'any() and all()' since
# the desired behavior is to have any of the keep and none of the ignore.

def scrape_func(address, website, database):
    """
    Function to scrape various RSS feeds. Uses the 'keep' and 'ignore' iterables
    to define which words should be used in the text search.
    
    Inputs
    ------
    address : address for the RSS feed to scrape. String.

    website : name of the website to scrape to be used in the filepath for the
    output. String.

    database : name of the MongoDB database that contains the collections.
    String? pymongo connection object?
    """
    results = pattern.web.Newsfeed().search(address, count=100)
    keep = ('kill', 'bomb', 'die', 'attack', 'shoot', 'fight')
    ignore = ('crash', 'accident', 'funeral', 'flood', 'house fire', 
            'apartment fire', 'lightning', 'mine blast', 'lion', 'disease',
            'ebola', 'cholera', 'murder-suicide', 'hit-and-run', 
            'half-staff')
    for result in results:
        toWrite = (result.title + ' ' 
                + pattern.web.plaintext(result.description))
        if (any([term in toWrite.lower() for term in keep]) and 
                all([word not in toWrite.lower() for word in ignore])):
            if website == 'nyt':
                try:
                    temp = pages_scrape.nyt_scrape(result.url, result.title)
                    mongo_connection.add_entry(database, temp, result.url, result.date,
                        website)
                except IndexError:
                    pass
            if website == 'bbc':
                try:
                    temp = pages_scrape.bbc_scrape(result.url, result.title,
                        result.date)
                    mongo_connection.add_entry(database, temp, result.url, result.date,
                        website)
                except IndexError:
                    pass
            if website == 'reuters':
                try:
                    temp = pages_scrape.reuters_scrape(result.url, result.title,
                        result.date)
                    mongo_connection.add_entry(database, temp, result.url, result.date,
                        website)
                except IndexError:
                    pass
            if website == 'ap':
                try:
                    temp = pages_scrape.ap_scrape(result.url, result.title,
                        result.date)
                    mongo_connection.add_entry(database, temp, result.url, result.date,
                        website)
                except IndexError:
                    pass
            if website == 'upi':
                try:
                    temp = pages_scrape.upi_scrape(result.url, result.title,
                        result.date)
                    mongo_connection.add_entry(database, temp, result.url, result.date,
                        website)
                except IndexError:
                    pass
            if website == 'google':
                temp = (result.title + '\n' + result.date + '\n\n' +
                    pattern.web.plaintext(result.description))
                mongo_connection.add_entry(database, temp, result.url, result.date,
                    website)

#def parallel_func(siteList, database, n_cores = -1):
#    """
#    Takes the scrape_func defined above and runs it in parallel.
#
#    Inputs
#    ------
#
#    siteList : Dictionary of sites to be scraped with the website name as the
#    key and address as the value. Dict. 
#
#    n_cores : Number of cores to use. -1 indicates all available. Integer. 
#    """
#    Parallel(n_jobs=n_cores)(delayed(scrape_func)(siteList[website], website,
#        database) for website in siteList)

def call_scrape_func(siteList, database):
    for website in siteList:
        scrape_func(siteList[website], website, database)
    print 'Scraped once!'

if __name__ == '__main__':
    print 'Running...'
    to_scrape = {
            'google' : 'https://news.google.com/?output=rss', 
            'nyt' : 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
            'reuters' : 'http://feeds.reuters.com/Reuters/worldNews',
            'bbc' : 'http://feeds.bbci.co.uk/news/world/rss.xml',
            'ap' : 'http://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5',
            'upi' : 'http://rss.upi.com/news/emerging_threats.rss'
            }

    logging.basicConfig()
    
    connection = MongoClient()
    db = connection.atrocities_data

    sched = Scheduler()
    sched.add_interval_job(call_scrape_func, args = [to_scrape, db], hours=1)
    sched.start()
    while True:
        time.sleep(10)
    sched.shutdown()