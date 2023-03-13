from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    return search_news(query)


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
