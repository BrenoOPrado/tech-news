from parsel import Selector
from tech_news.database import create_news
import re
import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    url_list = []
    if html_content != '':
        selector = Selector(html_content)

        for article in selector.css('div.archive-wrap')[0].css('article'):
            url_list.append(article
                            .css('h2.entry-title > a::attr(href)').get())

    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_url = selector.css('a.next.page-numbers::attr(href)').get()
    return next_url


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    result = {}
    count = 0

    for rel in selector.css('link::attr(rel)').getall():
        if rel == 'canonical':
            result['url'] = selector.css('link::attr(href)').getall()[count]
        count += 1
    result['title'] = selector.css('h1.entry-title::text').get().strip('\xa0')
    result['timestamp'] = selector.css('li.meta-date::text').get()
    result['writer'] = selector.css('span.author > a.url.fn.n::text').get()
    reading_time = ''
    for letter in selector.css('li.meta-reading-time::text').get():
        if letter.isdigit():
            reading_time += letter
    result['reading_time'] = int(reading_time)
    result['category'] = selector.css('span.label::text').get()
    result['summary'] = selector.css('div.entry-content > p,p::text').get()
    result['summary'] = re.sub('<.*?>', '', result['summary']).strip()
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    count = 0
    news_content = []
    url = 'https://blog.betrybe.com/'

    while count < amount:
        page = fetch(url)
        url_list = scrape_updates(page)
        for url in url_list:
            if count < amount:
                news_content.append(scrape_news(fetch(url)))
                count += 1
        url = scrape_next_page_link(page)

    create_news(news_content)

    return news_content
