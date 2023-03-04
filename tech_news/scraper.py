import requests
import time
import re
from requests.exceptions import HTTPError, ReadTimeout
from bs4 import BeautifulSoup


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
    soup = BeautifulSoup(html_content, "html.parser")
    cards = soup.find_all("h2", class_="entry-title")
    links = [link.find("a", href=True)['href'] for link in cards]
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    page_number = soup.find("a", class_="next page-numbers")
    if page_number:
        return page_number['href']
    return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    news_info = {
        "url": soup.find("link", {"rel": "canonical"})['href'],
        "title": soup.find("h1", class_="entry-title").text.strip(),
        "timestamp": soup.find("li", class_="meta-date").text,
        "writer": soup.find("a", class_="url fn n").text,
        "reading_time": int(re.findall(r"\d+",
                            soup.find("li",
                                       class_="meta-reading-time").text)[0]),
        "summary": soup.find("div",
                             class_="entry-content").find("p").text.strip(),
        "category": soup.find("span", class_="label").text,
    }
    return news_info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
