import requests
from bs4 import BeautifulSoup

response = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
html_info = response.text
soup = BeautifulSoup(html_info, 'html.parser')

#영화 인기검색어
i = 1
for anchor in soup.select('div.tit3'):
    print(str(i)+"위" + anchor.get_text())
    i = i + 1
