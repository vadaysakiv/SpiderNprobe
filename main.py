import requests
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()


def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        pass
    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag= soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        #print(url)
        for link in urls:
            if link not in visited_urls:
                visited_urls.add(link)
                url_join=urljoin(url,link) 
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join,keyword)
            else:
                pass



url=input("enter the url you want to input:\n")

keyword = input("keyword to search:")


spider_urls(url,keyword)
