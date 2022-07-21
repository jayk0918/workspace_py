import requests
from bs4 import BeautifulSoup

#1. 사이트에 요청 & 응답받기 - requests
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

# 요청
response = requests.get(url)

# 응답확인
print(response.status_code) #상태코드 : 200 -> 정상반응, 404 -> 잘아는 숫자지?
html = response.text #html코드
#print(html)


#2. 필요한 태그 추출 - beautifulsoup (랭킹 추출)
soup = BeautifulSoup(html, 'html.parser')
tags = soup.select('.tit3>a')
tag2 = soup.select_one('.tit3>a')
print(tags)
print(tags[0])
print(tags[1])
print(tag2)
print(tags[22].text)
print(tag2.text)
#print(tag[50]) - out of range

print('===' * 40)

'''
for tag in tags:
    title = tag.text
    print(title)
'''

for index, tag in enumerate(tags):
    rank = index + 1
    title = tag.text
    print(rank, title)