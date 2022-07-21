import requests
import uuid

# 이미지 추출
img_url = 'https://movie-phinf.pstatic.net/20220509_176/1652081912471yhg3N_JPEG/movie_image.jpg?type=m203_290_2'

saveName = str(uuid.uuid4())

img_response = requests.get(img_url)
#print(response.text)
print(saveName, type(saveName))
# 저장 위치 + 파일명
filePath = '/Users/jaykim0918/Downloads/BufferedWriter/'+saveName+'.jpg'
#print(filePath)

file = open(filePath, 'wb')
file.write(img_response.content)
file.close()

