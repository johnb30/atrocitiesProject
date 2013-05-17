import requests
import justext
#import lxml.html as lh


def scrape(url, title):
    text = str()
    page = requests.get(url)
    paragraphs = justext.justext(page.content, justext.get_stoplist('English'))
    for par in paragraphs:
        if par['class'] == 'good':
            text += par['text']
    return text


#def nyt_scrape(url, title):
#    try:
#        page = requests.get(url)
#        doc = lh.fromstring(page.content)
#        text = title + '\n\n'
#        content = doc.xpath("//div[@class='columnGroup first']//p[@itemprop='articleBody']")
#        for paragraph in content:
#            text += paragraph.text_content() + '\n\n'
#        return text
#    except IndexError:
#        pass
#
#
#def bbc_scrape(url, title, date):
#    try:
#        page = requests.get(url)
#        doc = lh.fromstring(page.content)
#        paragraphs = doc.xpath("//div[@class='story-body']/p")
#        text = title + '\n' + date + '\n\n'
#        for par in paragraphs:
#            text += par.text_content() + '\n\n'
#        return text
#    except IndexError:
#        pass
#
#
#def reuters_scrape(url, title, date):
#    try:
#        text = title + '\n' + date + '\n\n'
#        page = requests.get(url)
#        doc = lh.fromstring(page.content)
#        text += doc.xpath('//span[@id="articleText"]')[0].text_content()
#        #OR
#        #first_par = doc.xpath('//span[@class="focusParagraph"]/p')[0].text_content()
#        #paragraphs = doc.xpath('//span[@id="articleText"]/p')
#        #text = first_par + '\n\n'
#        #for par in paragraphs:
#            #text += par.text_content() + '\n\n'
#        return text
#    except IndexError:
#        pass
#
#
#def ap_scrape(url, title, date):
#    try:
#        page = requests.get(url)
#        doc = lh.fromstring(page.content)
#        paragraphs = doc.xpath('//div[@id="storyBodyDivd57851005a80479aaeeb90a12c70b9f6"]/p')
#        text = title + '\n\n' + date + '\n\n'
#        for par in paragraphs:
#            text += par.text_content() + '\n\n'
#        return text
#    except IndexError:
#        pass
#
#
#def upi_scrape(url, title, date):
#    try:
#        page = requests.get(url)
#        doc = lh.fromstring(page.content)
#        paragraphs = doc.xpath('//div[contains(@style, "font-size: 14px")]/p')
#        text = title + '\n\n' + date + '\n\n'
#        for par in paragraphs:
#            text += par.text_content() + '\n\n'
#        return text
#    except IndexError:
#        pass
#
#
#def xinhua_scrape(url, title, date):
#    try:
#        text = title + '\n' + date + '\n'
#        page = requests.get(url)
#        doc = lh.fromstring(page.content)
#        content = doc.xpath('//div[@id="Content"]//p')
#        for paragraph in content:
#            text += paragraph.text_content()
#        text = text.replace('\n\n', '\n')
#        return text
#    except IndexError:
#        pass
