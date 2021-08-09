import time

def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(10)
        new_height = driver.execute_script('return document.body.scrollHeight')

        if new_height == last_height:
            time.sleep(10)
            new_height = driver.execute_script('return document.body.scrollHeight')

            try:
                driver.find_element_by_class_name("mye4qd").click()
            except:

                if new_height == last_height:
                    break
    
    last_height = new_height