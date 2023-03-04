import requests
import time
from requests.exceptions import HTTPError, ReadTimeout


# Requisito 1
def fetch(url):
    time.sleep(1)
    HEADERS = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=HEADERS, timeout=3)
        response.raise_for_status()
    except (ReadTimeout, HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
