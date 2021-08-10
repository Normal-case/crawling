import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from scroll import *
import os
import dload

keyword = input('검색할 태그를 입력하세요 : ')
crawling_num = int(input('원하는 이미지 개수를 입력하세요 : '))

# # google url
# url = 'https://www.google.com/search?q={}&sxsrf=ALeKk016mcgCxLZdfnAJPMJ7H3uGGFQg4g:1628485017590&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi_7Pq3k6PyAhUGG6YKHTSuAOcQ_AUoAXoECAIQAw&biw=2048&bih=1042'.format(keyword)

# driver = webdriver.Chrome()
# driver.get(url)

# time.sleep(5)

# ret = driver.page_source
# soup = BeautifulSoup(ret, 'html.parser')

# images = soup.find_all('img', attrs={'class': 'rg_i Q4LuWd'})

# for i, img in enumerate(images):
#     src = img['src']
#     urllib.request.urlretrieve(src, f'./images/{i}.jpg')


'''
pixabay crawling
'''

# url = f'https://pixabay.com/ko/images/search/{keyword}/'


# driver = webdriver.Chrome()
# driver.get(url)

# time.sleep(5)

# ret = driver.page_source
# soup = BeautifulSoup(ret, 'lxml')

# max_page = soup.select_one('.add_search_params > input')
# form = soup.select_one('.add_search_params')
# max_page = int(form.get_text().replace(' ', '').replace('/', ''))

# images = soup.find_all('img', attrs={'class': 'photo-result-image'})

# os.makedirs(f'./images/{keyword}', exist_ok=True)

# img_num = 0
# for page in range(1, max_page):

#     if page != 1:
#         url = f'https://pixabay.com/ko/images/search/{keyword}/?pagi={page}'
#         driver.get(url)

#         ret = driver.page_source
#         soup = BeautifulSoup(ret, 'html.parser')

#         images = soup.find_all('img', attrs={'class': 'photo-result-image'})

#         time.sleep(5)

#     for img in images:
#         src = img['src']
#         if src == '/static/img/blank.gif':
#             src = img['data-lazy-srcset'].split(',')[0]
#             src = src.replace(' 1x', '')

#         dload.save(src, f'images/{keyword}/{img_num}.jpg')

#         img_num += 1

#         if img_num == crawling_num:
#             break
#     else:
#         continue
#     break
    
# driver.quit()

'''
unsplash crawling
'''

url = f'https://unsplash.com/s/photos/{keyword}'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

scroll_down(driver)

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# images = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})

# print('number of img tags: ', len(images))

# n = 1

# for i in images:

#     try:
#         imgUrl = i['src']
#     except:
#         imgUrl = i['data-src']

#     with urllib.request.urlopen(imgUrl) as f:
#         with open('./img/' + keyword + str(n) + '.jpg', 'wb') as h:
#             img = f.read()
#             h.write(img)

#     n += 1