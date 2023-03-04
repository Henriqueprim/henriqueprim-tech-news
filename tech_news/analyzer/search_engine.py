from tech_news.database import search_news
import re


# Requisito 7
def search_by_title(title):
    news_list = search_news({"title": re.compile(rf"{title}", re.I)})

    return [(news['title'], news['url']) for news in news_list]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
