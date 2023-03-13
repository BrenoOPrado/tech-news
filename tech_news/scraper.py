from parsel import Selector
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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
