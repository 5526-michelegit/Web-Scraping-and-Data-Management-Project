from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

def get_advs(url):
    items = []

    with webdriver.Firefox() as driver:
        driver.get(url)
        time.sleep(8)

        # Check cookie banner
        if len(driver.find_elements(By.ID, "didomi-notice-disagree-button")) != 0:
            print('Closing cookie banner..')
            cookie_banner_button = driver.find_element(By.ID, "didomi-notice-disagree-button")
            cookie_banner_button.click()
        
        page_index = 1
        last_page_visited = False
        next_button = driver.find_elements(By.CLASS_NAME, 'icon-arrow-right-after')
        while len(next_button) > 0 or last_page_visited == False :

            if len(next_button) == 0:
                last_page_visited = True

            articles = driver.find_elements(By.TAG_NAME, 'article')
            print(f'Trovati {len(articles)} elementi nella pagina {page_index}')

            for article in articles:
                if article.get_attribute('class') == 'adv noHover':
                    continue
                new_item = {}
                new_item['url'] = article.find_element(By.CLASS_NAME, 'item-link').get_attribute('href')
                new_item['title'] = article.find_element(By.CLASS_NAME, 'item-link').get_attribute('title')
                items.append(new_item)

            if last_page_visited == False:
                btn = driver.find_element(By.CLASS_NAME, 'icon-arrow-right-after')
                btn.click()
                time.sleep(8)
                next_button = driver.find_elements(By.CLASS_NAME, 'icon-arrow-right-after')

            page_index += 1

    return items