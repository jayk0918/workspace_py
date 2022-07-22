import requests
from bs4 import BeautifulSoup
import util

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

response = requests.get(url)

html = response.text
print(html)

soup = BeautifulSoup(html, 'html.parser')

tags = soup.select('.tit3>a')
print(tags[0])

for index, tag in enumerate(tags):
    #랭킹
    rank = index + 1

    #영화제목
    title = tag.text

    #포스터
    sub_page_url = tag['href']
    sub_url = 'https://movie.naver.com' + sub_page_url
    filePath = util.imgDownload(sub_url) #subpage에서 포스터 수집

    print(rank, title, filePath)