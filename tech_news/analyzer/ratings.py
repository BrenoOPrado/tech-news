from tech_news.database import search_news


# Requisito 10
def top_5_categories():
    """Seu código deve vir aqui"""
    result = {}
    for item in search_news({}):
        if item['category'] in result:
            result[item['category']] += 1
        else:
            result[item['category']] = 1

    result = sorted(result.items(), key=lambda item: (-item[1], item[0]))

    five_first_results = []
    for item in result:
        if len(five_first_results) <= 5:
            five_first_results.append(item[0])

    return five_first_results
