from tech_news.database import search_news
# from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    news_obj = search_news(query)
    news_tupla = [(item['title'], item['url']) for item in news_obj]
    return news_tupla


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
