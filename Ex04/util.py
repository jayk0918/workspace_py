import requests
from bs4 import BeautifulSoup
import uuid

def imgDownload(sub_page_url):
    #sub_page_url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=81888'
    response = requests.get(sub_page_url)
    html = response.text
    #print(html)

    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.select_one('.poster>a>img')
    #print(tag)
    poster_url = tag['src']
    #print(poster_url)

    saveName = str(uuid.uuid4())

    filePath = '/Users/jaykim0918/Downloads/BufferedWriter/'+saveName+'.jpg'

    img_response = requests.get(poster_url)

    file = open(filePath, 'wb')
    file.write(img_response.content)
    file.close()

    return filePath