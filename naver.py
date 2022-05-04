from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from webdriver_manager.chrome import ChromeDriverManager

import os
import time
import urllib.request

driver = webdriver.Chrome(ChromeDriverManager().install())
keyword = '물티슈'
os.makedirs(f'images/naver/{keyword}', exist_ok=True)

driver.get(f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}')

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(SCROLL_PAUSE_TIME)

    # driver.execute_script(f'window.scrollTo(0, {last_height-2000})')
    # time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script('return document.body.scrollHeight')
    print(f'last_height: {last_height} || new_height: {new_height}')
    if new_height == last_height:
        break
    #     try:
    #         driver.find_element_by_css_selector('.link_thumb._imageBox._infoBox').click()
    #     except:
    #         break
    # else:
    #     break
    
    last_height = new_height

    images = driver.find_elements_by_css_selector('._image._listImage')
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(0.2)
            imgUrl = driver.find_element_by_xpath('//*[@id="main_pack"]/section[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[1]/img').get_attribute('src')
            urllib.request.urlretrieve(imgUrl, f'images/naver/{keyword}/{count}.jpg')
            count += 1
        except:
            pass

driver.close()