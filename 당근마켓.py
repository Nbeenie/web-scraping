import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.daangn.com/search/%EB%A7%88%ED%8F%AC")
html_info = response.text
soup = BeautifulSoup(html_info, 'html.parser')

lists = soup.find_all('a', class_="flea-market-article-link")


for list in lists:
    stuff = list.find('span', class_="article-title").text.replace('\n', "").strip()
    location = list.find('p', class_="article-region-name").text.replace('\n', "").strip()
    money = list.find('p', class_="article-price").text.replace('\n', "").strip()

    info = [stuff, location, money]
    print(info)
