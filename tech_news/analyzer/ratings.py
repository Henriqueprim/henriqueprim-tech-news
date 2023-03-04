from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news_list = find_news()
    if news_list:
        category_list = Counter(sorted(
            news['category'] for news in news_list)).most_common(5)
        return [category[0] for category in category_list]
    return []
