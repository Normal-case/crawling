import os
import time
import dload
from bs4 import BeautifulSoup
from selenium import webdriver

class CollectingSource():

    def __init__(self, keyword, crawling_num):
        self.driver = self.get_selenium()
        self.keyword = keyword
        self.crawling_num = crawling_num

    def get_selenium(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(chrome_options=options)
        return driver

    def scroll_down(self, xpath):
        SCROLL_PAUSH_TIME = 2

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        # list for saving src
        links = []

        while True:

            images = self.driver.find_elements_by_xpath(xpath)

            for img in images:
                src = img.get_attribute('src')
                links.append(src)
            
            self.driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight);')

            time.sleep(SCROLL_PAUSH_TIME)
            self.driver.execute_script(f'window.scrollTo(0, {last_height-2000});')
            time.sleep(SCROLL_PAUSH_TIME)

            new_height = self.driver.execute_script('return document.body.scrollHeight')

            if new_height == last_height:
                break

            last_height = new_height

            if 2 * self.crawling_num < len(links):
                break
        
        return list(dict.fromkeys(links))

    def pixabay(self):
        
        # open browser
        url = f'https://pixabay.com/ko/images/search/{self.keyword}/'
        self.driver.get(url)

        # wait loading
        time.sleep(3)

        # create save directory
        os.makedirs(f'./images/pixabay/{self.keyword}', exist_ok=True)

        # getting page source
        ret = self.driver.page_source

        # clearing page using soup
        soup = BeautifulSoup(ret, 'lxml')
        form  = soup.select_one('.add_search_params')
        
        # get max_page and images
        max_page = int(form.get_text().replace(' ', '').replace('/', ''))
        images = soup.find_all('img', attrs={'class':'photo-result-image'})

        img_num = 0
        for page in range(1, max_page):

            # when page is not first page
            if page != 1:
                url = f'https://pixabay.com/ko/images/search/{self.keyword}/?pagi={page}'
                self.driver.get(url)

                ret = self.driver.page_source
                soup = BeautifulSoup(ret, 'lxml')

                images = soup.find_all('img', attrs={'class':'photo-result-image'})

                time.sleep(3)

            for img in images:
                src = img['src']

                # when image is loading
                if src == '/static/img/blank.gif':
                    src = img['data-lazy-srcset'].split(',')[0]
                    src = src.replace(' 1x', '')

                dload.save(src, f'images/pixabay/{self.keyword}/{img_num}.jpg')

                img_num += 1

                if img_num == self.crawling_num:
                    break
            else:
                continue
                
            break

        self.driver.close()

    
    def unsplash(self):
        
        url = f'https://unsplash.com/s/photos/{self.keyword}'
        self.driver.get(url)

        time.sleep(3)

        os.makedirs(f'./images/unsplash/{self.keyword}', exist_ok=True)

        xpath = '//img[@class="oCCRx"]'
        links = self.scroll_down(xpath)

        if self.crawling_num > len(links):

            for i, l in enumerate(links):
                dload.save(l, f'images/unsplash/{self.keyword}/{i}.jpg')
        
        else:
            
            for i in range(self.crawling_num):
                dload.save(links[i], f'images/unsplash/{self.keyword}/{i}.jpg')

        self.driver.close()