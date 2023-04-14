from tech_news.database import search_news


# Requisito 7
def search_by_title(title: str):
    news = search_news({
        "title": {"$regex": title, "$options": "i"},
    })

    return [
        (info["title"], info["url"])
        for info in news
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
