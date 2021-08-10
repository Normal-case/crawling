import time
import datetime
import pdb
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

def scroll_down(driver):
    SCROLL_PAUSE_SEC = 3
    scroll_ = 0

    while True:
        
        ret = driver.page_source
        soup = BeautifulSoup(ret, 'lxml')
        images = soup.find_all('img', attrs={'class': 'oCCRx'})
        print(len(images))

        for img in images:
            try:
                print(img['alt'])
            except:
                print('no alt')

        print('='*100)
        # scroll down
        driver.execute_script(f'window.scrollTo({scroll_}, {scroll_} + 3000);')
        scroll_ += 3000
        time.sleep(SCROLL_PAUSE_SEC)
        new_height = driver.execute_script('return document.body.scrollHeight')

        if new_height < scroll_:
            break