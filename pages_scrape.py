import requests
import lxml.html as lh

def nyt_scrape(url, title):
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    text = title + '\n\n'
    text += doc.xpath("//div[@class='columnGroup first']")[0].text_content()
    return text

def bbc_scrape(url, title, date):
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    paragraphs = doc.xpath("//div[@class='story-body']/p")
    text = title + '\n' + date + '\n\n'
    for par in paragraphs:
        text += par.text_content() + '\n\n'
    return text

def reuters_scrape(url, title, date):
    text = title + '\n' + date + '\n\n'
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    text += doc.xpath('//span[@id="articleText"]')[0].text_content()
    #OR
    #first_par = doc.xpath('//span[@class="focusParagraph"]/p')[0].text_content()
    #paragraphs = doc.xpath('//span[@id="articleText"]/p')
    #text = first_par + '\n\n'
    #for par in paragraphs:
        #text += par.text_content() + '\n\n'
    return text

def ap_scrape(url, title, date):
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    paragraphs = doc.xpath('//div[@id="storyBodyDivd57851005a80479aaeeb90a12c70b9f6"]/p')
    text = title + '\n\n' + date + '\n\n'
    for par in paragraphs:
        text += par.text_content() + '\n\n'
    return text

def upi_scrape(url, title, date):
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    paragraphs = doc.xpath('//div[contains(@style, "font-size: 14px")]/p')
    text = title + '\n\n' + date + '\n\n'
    for par in paragraphs:
        text += par.text_content() + '\n\n'
    return text


