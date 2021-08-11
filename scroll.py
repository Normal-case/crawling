import time
from selenium import webdriver
import datetime
import pdb
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.common.keys import Keys
import dload

"""
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
"""

def scroll_down(driver, keyword):
    SCROLL_PAUSE_TIME = 2

    last_height = driver.execute_script("return document.body.scrollHeight")

    js_script = '''
    var scroll_height = document.body.scrollHeight
    return scroll_height
    '''

    while True:
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script(f"window.scrollTo(0, {last_height-2000});")
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    # ret = driver.page_source
    # soup = BeautifulSoup(ret, 'lxml')
    # images = soup.find_all('img', attrs={'class':'oCCRx'})

    # for img in images:
    #     src = img['src']
    #     dload.save(src, f'images/{keyword}/{img_num}.jpg')
    # print(len(images))

    images = driver.find_elements_by_class_name('oCCRx')
    print(images)
    for i, img in enumerate(images):
        src = img.get_property('srcset')
        src = src.split(',')[0]
        src = src.replace(' 100w', '')
        print(src)
        dload.save(src, f'images/{keyword}/{i}.jpg')
    print(len(images))


def get_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    return driver