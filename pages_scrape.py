import requests
import justext


def scrape(url, title):
    text = str()
    try:
        page = requests.get(url)
        paragraphs = justext.justext(page.content,
                                     justext.get_stoplist('English'))
        for par in paragraphs:
            if par['class'] == 'good':
                text += par['text']
        return text
    #Generic error catching is bad
    #As are printed log statements....
    except Exception:
        print 'Something went wrong...'
