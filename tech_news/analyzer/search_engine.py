from datetime import datetime
from tech_news.database import search_news
import re


# Requisito 7
def search_by_title(title):
    news_list = search_news({"title": re.compile(rf"{title}", re.I)})

    return [(news['title'], news['url']) for news in news_list]


# Requisito 8
def search_by_date(date):
    try:
        string_to_date = datetime.strptime(date, '%Y-%m-%d')
        formated_date = datetime.strftime(string_to_date, '%d/%m/%Y')
        news_list = search_news({'timestamp': formated_date})
    except ValueError:
        raise ValueError("Data inválida")

    return [(news['title'], news['url']) for news in news_list]


# Requisito 9
def search_by_category(category):
    news_list = search_news({"category": re.compile(rf"{category}", re.I)})

    return [(news['title'], news['url']) for news in news_list]
