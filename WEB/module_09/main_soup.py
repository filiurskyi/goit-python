import json
from typing import Union

import requests
from bs4 import BeautifulSoup

from con_redis import redis_get, redis_set


# from urllib.parse import urljoin, urlparse


class QuoteCard:
    def __init__(self):
        self.quote = ""
        self.author = ""
        self.tags = []

    def to_dict(self):
        return {
            "tags": self.tags,
            "author": self.author,
            "quote": self.quote,
        }

    def add_tag(self, tag):
        self.tags.append(tag)


class AuthorCard:
    def __init__(self):
        self.name = ""
        self.born_date = ""
        self.born_location = ""
        self.description = ""

    def to_dict(self):
        return {
            "fullname": self.name,
            "born_date": self.born_date,
            "born_location": self.born_location,
            "description": self.description
        }


def response_caching(url):
    cached_response = redis_get(url)
    if cached_response is not None:
        print("cached")
        return cached_response
    else:
        print("uncached")
        response = requests.get(url)
        redis_set(url, response)
        return response


def append_to_json(obj: Union[QuoteCard, AuthorCard], filename):
    new_data = obj.to_dict()
    with open(filename, "r", encoding="utf-8") as f:
        data_list = json.load(f)
    with open(filename, "w", encoding="utf-8") as f:
        if new_data not in data_list:
            data_list.append(new_data)
        json.dump(data_list, f, indent=2)


def get_quotes(url: str):
    soup = BeautifulSoup(response_caching(url).text, "lxml")
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    tags = soup.find_all("div", class_="tags")

    for i in range(0, len(quotes)):
        quote_card = QuoteCard()
        tagsforquote = tags[i].find_all("a", class_="tag")
        quote_card.quote = quotes[i].text[1:-1]  # trim quote mark
        quote_card.author = authors[i].text
        for tagforquote in tagsforquote:
            quote_card.add_tag(tagforquote.text)
        append_to_json(quote_card, "quotes.json")


def get_authors(url: str):
    soup = BeautifulSoup(response_caching(url).text, "lxml")
    fullname = soup.find_all("h3", class_="author-title")
    born_date = soup.find_all("span", class_="author-born-date")
    born_loc = soup.find_all("span", class_="author-born-location")
    description = soup.find_all("div", class_="author-description")

    author_card = AuthorCard()
    for i in range(0, len(fullname)):
        author_card.name = fullname[i].text.strip()
        author_card.born_date = born_date[i].text.strip()
        author_card.born_location = born_loc[i].text.strip()
        author_card.description = description[i].text.strip()
    append_to_json(author_card, "authors.json")


def get_authors_urls(base, url_list=["/"]):
    for url in url_list:
        soup = BeautifulSoup(response_caching(base + url).text, "lxml")
        url_list = soup.select("div[class=quote] a")

        result = []
        for a in url_list:
            if a["href"].startswith("/author"):
                result.append(a["href"])
        if result:
            return [*result, *get_authors_urls(base, url_list=result)]
        else:
            return []


def get_quote_urls(base, url_list=["/"]):
    result = [*url_list]
    for url in url_list:
        soup = BeautifulSoup(response_caching(base + url).text, "lxml")
        url_list = soup.select("li[class=next] a[href]")
        if url_list:
            for a in url_list:
                link = a["href"]
                result.append(link)
                return [*result, *get_quote_urls(base, url_list=[link])]
        else:
            return result




if __name__ == "__main__":
    base_url = "https://quotes.toscrape.com/"
    pages_urls = get_quote_urls(base_url)
    print(pages_urls)
    for q_url in pages_urls:
        print("processing url ", q_url)
        get_quotes(base_url + q_url)

        author_urls = get_authors_urls(base_url + q_url)

        for a_url in author_urls:
            get_authors(base_url + a_url)
