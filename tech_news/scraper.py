import requests
import time
from bs4 import BeautifulSoup


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


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    return [
        tag["href"] for tag in soup.find_all("a", {"class": "cs-overlay-link"})
    ]


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        next_page = soup.find("a", {"class": "next page-numbers"})['href']
    except TypeError:
        return None

    else:
        return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
