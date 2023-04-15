from tech_news.database import find_news
from collections import defaultdict


def top_5_categories():
    news = find_news()
    ratings = defaultdict(lambda: 1)

    for info in news:
        ratings[info["category"]] += 1

    ratings_sorted = sorted(ratings.items(), key=lambda x: (-x[1], x[0]))

    return [category[0] for category in ratings_sorted][:5]
