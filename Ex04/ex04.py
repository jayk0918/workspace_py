from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome('/Users/jaykim0918/Dropbox/chromedriver')
url = 'https://movie.daum.net/moviedb/grade?movieId=139606'
wd.get(url)
wd.implicitly_wait(10) # 최대 10초 -> 로딩이 끝나면 그 전에 parsing 끝


cmt_tags = wd.find_elements(By.CSS_SELECTOR, '.cmt_info')
#print(cmt_tags)
'''
for cmt_tag in cmt_tags:
    rate = cmt_tag.find_element(By.CSS_SELECTOR, '.ratings').text
    cmt = cmt_tag.find.element(By.CSS_SELECTOR, 'li p').text
    date = cmt_tag.find.element(By.CSS_SELECTOR, '.txt_date').text

    print(rate, cmt, date, end="\n\n")
'''
# 더보기 클릭
while(True):
    try:
        wd.find_element(By.CSS_SELECTOR, '.alex_more').click()
        wd.implicitly_wait(2)
    except:
        print('마지막')
        break


for i, cmt_tag in enumerate(cmt_tags):
    rate = cmt_tag.find_element(By.CSS_SELECTOR, '.ratings').text
    try:
        cmt = cmt_tag.find.element(By.CSS_SELECTOR, '').text
    except:
        cmt = '****************'
    date = cmt_tag.find.element(By.CSS_SELECTOR, '.txt_date').text

    print(i+1, rate, cmt, date, end='\n\n')