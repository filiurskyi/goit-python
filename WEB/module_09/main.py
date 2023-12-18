import requests
import bs4 as bs
from urllib.parse import urljoin



import http.client
base_url = "index.minfin.com.ua"
url_path = "/ua/russian-invading/casualties/3/"
full_url = "https://index.minfin.com.ua/ua/russian-invading/casualties/3/"


def http_get():
    conn = http.client.HTTPSConnection(base_url, port=443)
    conn.request("GET", url_path)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    conn.close()
    return data


def get_url(url):
    response = requests.get(url)
    return response


if __name__ == '__main__':
    print(http_get() == get_url(full_url).text)
