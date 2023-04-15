from tech_news.database import search_news
from datetime import datetime


def search_by_title(title: str):
    news = search_news({
        "title": {"$regex": title, "$options": "i"},
    })

    return [
        (info["title"], info["url"])
        for info in news
    ]


def search_by_date(date):
    try:
        get_date = datetime.strptime(date, "%Y-%m-%d")
        date_format = datetime.strftime(get_date, "%d/%m/%Y")

        news = search_news({"timestamp": date_format})

        return [
            (info["title"], info["url"])
            for info in news
        ]

    except ValueError:
        raise ValueError('Data inválida')


def search_by_category(category):
    news = search_news({
        "category": {"$regex": category, "$options": "i"},
    })

    return [
        (info["title"], info["url"])
        for info in news
    ]
