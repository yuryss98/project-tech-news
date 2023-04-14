import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news


def fetch(url):
    try:
        time.sleep(1)
        header = {"user-agent": "Fake user-agent"}
        page = requests.get(url, headers=header, timeout=3)
    except requests.ReadTimeout:
        return None

    if not page.status_code == 200:
        return None

    return page.text


def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    return [
        tag["href"] for tag in soup.find_all("a", {"class": "cs-overlay-link"})
    ]


def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        next_page = soup.find("a", {"class": "next page-numbers"})["href"]
    except TypeError:
        return None

    else:
        return next_page


def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    dict_news = {
        "url": soup.find("link", {"rel": "canonical"})["href"],
        "title": soup.find("h1", {"class": "entry-title"}).string.strip(),
        "timestamp": soup.find("li", {"class": "meta-date"}).string,
        "writer": soup.find("span", {"class": "author"}).string,
        "reading_time": int(
            soup.find("li", {"class": "meta-reading-time"}).text.split(" ")[0]
        ),
        "summary": soup.find("div", {"class": "entry-content"}).p.text.strip(),
        "category": soup.find("a", {"class": "category-style"})
        .find("span", {"class": "label"})
        .text
    }

    return dict_news


def get_tech_news(amount):
    html_content = fetch('https://blog.betrybe.com')
    links_news = scrape_updates(html_content)
    news = []
    count = 0

    while amount > count:
        try:
            current_news = fetch(links_news[count])
            news.append(scrape_news(current_news))
            count += 1
        except IndexError:
            next_page_link = scrape_next_page_link(html_content)
            html_content = fetch(next_page_link)
            links_news.extend(scrape_updates(html_content))

    create_news(news)

    return news
