from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import os
import time
import urllib.request

driver = webdriver.Chrome(ChromeDriverManager().install())
keyword = '물티슈'
os.makedirs(f'images/google_resolution/{keyword}', exist_ok=True)

driver.get(f'https://www.google.com/search?q={keyword}&sxsrf=APq-WBuhA2ROxRsblsYs-CgplQrtBqJyCA:1647838771254&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0nOvktdb2AhXI6mEKHd7xCUYQ_AUoAXoECAEQAw&biw=1280&bih=1328&dpr=1')

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height != last_height:
        try:
            driver.find_element_by_css_selector('.wXeWr.islib.nfEiy').click()
        except:
            break
    else:
        break
    
    last_height = new_height

    # images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    print(len(images))
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(0.5)
            # imgUrl = driver.find_element_by_class_name('n3VNCb').get_attribute('src')
            imgUrl = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute('src')
            print(imgUrl)
            urllib.request.urlretrieve(imgUrl, f'images/google_resolution/{keyword}/{count}.jpg')
            count += 1
        except:
            pass

driver.close()
#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img
