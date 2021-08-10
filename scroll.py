import time
from selenium import webdriver
import datetime
import pdb
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.common.keys import Keys
import dload

def scroll_down(driver, keyword):
    SCROLL_PAUSE_SEC = 3
    scroll_ = 0
    img_num = 0
    while True:
        
        js_script = '''\
        var jslist = []
        document.querySelectorAll('img.oCCRx').forEach(i => jslist.push(i.srcset));
        return jslist;
        '''
        python_list = driver.execute_script(js_script)
        tmp = python_list[0].split(',')[0]
        tmp = tmp.replace(' 100w', '')
        
        for img in python_list:
            
            img = img.split(',')[0]
            img = img.replace(' 100w', '')
            print(img)
            dload.save(img, f'images/{keyword}/{img_num}.jpg')

        # scroll down
        driver.execute_script(f'window.scrollTo({scroll_}, {scroll_} + 3000);')
        scroll_ += 3000
        time.sleep(SCROLL_PAUSE_SEC)
        new_height = driver.execute_script('return document.body.scrollHeight')
        img_num += 1
        if new_height < scroll_:
            break

def get_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    return driver