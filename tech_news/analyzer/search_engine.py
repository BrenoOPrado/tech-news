from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {'title': {'$regex': title, '$options': 'i'}}
    news_obj = search_news(query)
    news_tupla = [(item['title'], item['url']) for item in news_obj]
    return news_tupla


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""

    try:
        organized_date = datetime.strptime(date, '%Y-%m-%d'
                                           ).strftime('%d/%m/%Y')
        query = {'timestamp': organized_date}
        news_tupla = []
        news_obj = search_news(query)
        if len(news_obj) > 0:
            news_tupla = [(item['title'], item['url']) for item in news_obj]
        return news_tupla
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
