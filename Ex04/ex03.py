import requests
from bs4 import BeautifulSoup

# 댓글 추출
url = 'https://movie.daum.net/moviedb/grade?movieId=139606'

response = requests.get(url)

html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
tags = soup.select('.cmt_info')
print(tags)

#api 통신일 경우 selenium으로 크롤링해야함, bs4사용불가능