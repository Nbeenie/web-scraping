import requests
from bs4 import BeautifulSoup

header = {'User-agent': 'Mozila/2.0'}
response = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105', headers=header)
html_info = response.text
soup = BeautifulSoup(html_info, 'html.parser')
titles = soup.select('.cluster_text_headline')
for title in titles:
    print(title.text)