import time
from selenium import webdriver
import dload

def scroll_down(driver, keyword):
    SCROLL_PAUSE_TIME = 2

    last_height = driver.execute_script("return document.body.scrollHeight")

    # list for saving src
    links = []

    while True:

        xpath = '//img[@class="oCCRx"]'
        images = driver.find_elements_by_xpath(xpath)

        for img in images:
            src = img.get_attribute('src')
            links.append(src)

        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script(f"window.scrollTo(0, {last_height-2000});")
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height
    
    # remove duplicate
    links = list(dict.fromkeys(links))

    # save image
    for i, l in enumerate(links):
        dload.save(l, f'images/{keyword}/{i}.jpg')

def get_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    # options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    return driver