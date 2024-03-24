from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.by import By
from custom_exceptions import DeactivateException, ScrapingDetectionException
import time

def import_data(url, proxy):

    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL", 
    }

    profile = webdriver.FirefoxProfile()
    profile.set_preference("javascript.enabled", True)
    with webdriver.Firefox(profile) as driver:
        driver.get(url)
        
        house = {}
        house['url'] = url
        
        # Check cookie banner
        if len(driver.find_elements(By.ID, "didomi-notice-disagree-button")) != 0:
            print('Closing cookie banner..')
            cookie_banner_button = driver.find_element(By.ID, "didomi-notice-disagree-button")
            cookie_banner_button.click()

        # Check if scraping has been detected
        if len(driver.find_elements(By.CLASS_NAME,'captcha__robot__container')) > 0:
            raise ScrapingDetectionException('Scraping detected')

        # Check if the property is still active
        if len(driver.find_elements(By.CLASS_NAME,'main-info__title-main')) == 0:
            if len(driver.find_elements(By.CLASS_NAME, 'deactivated-detail-with-suggestions')) > 0:
                raise DeactivateException('This property is deactivated')

        # Get the new url

        # Find the elemnt link with rel = canoncial
        canonical_url = driver.find_element(By.XPATH, '//link[@rel="canonical"]').get_attribute('href')
        house['url'] = canonical_url

        title = driver.find_element(By.CLASS_NAME,'main-info__title-main')
        house['title'] = title.text

        location = driver.find_element(By.CLASS_NAME,'main-info__title-minor')
        house['location'] = location.text

        price = driver.find_element(By.CLASS_NAME,'info-data-price').find_element(By.CLASS_NAME, 'txt-bold')
        house['price'] = price.text

        #Features
        features = driver.find_element(By.CLASS_NAME,'info-features')
        if len(features.find_elements(By.CLASS_NAME, "info-urgent")) != 0:
            house['occasione'] = True
        else:
            house['occasione'] = False

        features_details = features.find_elements(By.TAG_NAME,'span')
        features_len = len(features_details)

        if features_len >= 2:
            house['metratura'] = features_details[0].text

        if features_len >= 4:
            house['numero locali'] = features_details[2].text

        if features_len >= 5:
            house['posizione'] = features_details[4].text


        if len(driver.find_elements(By.CLASS_NAME, "adCommentsLanguage")) != 0:
            comments_container = driver.find_element(By.CLASS_NAME,'commentsContainer').find_element(By.CLASS_NAME, 'adCommentsLanguage')
            comment = comments_container.find_element(By.TAG_NAME, 'p')
            house['decriptions'] = comment.text

        # Caratteristiche specifice
        property_details = []
        constructions = []
        equipments = []

        details_block = driver.find_element(By.CLASS_NAME,'details-property')
        details_block_cols = details_block.find_elements(By.XPATH, "./*")

        for col in details_block_cols:
            col_blocks = col.find_elements(By.XPATH, "./*")
            for block in col_blocks:
                block_class = block.get_attribute("class")
                if block_class == 'details-property-h3':
                    block_index = col_blocks.index(block)
                    if block.text == 'Caratteristiche specifiche':
                        sub_block = col_blocks[block_index + 1]
                        items_list = sub_block.find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')
                        for item in items_list:
                            property_details.append(item.text)
                    elif block.text == 'Costruzione':
                        sub_block = col_blocks[block_index + 1]
                        items_list = sub_block.find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')
                        for item in items_list:
                            constructions.append(item.text)
                    elif block.text == 'Dotazione':
                        sub_block = col_blocks[block_index + 1]
                        items_list = sub_block.find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')
                        for item in items_list:
                            equipments.append(item.text)

        if len(property_details) > 0:
            house['propertyDetails'] = property_details

        if len(constructions) > 0:
            house['constructions'] = constructions

        if len(equipments) > 0:
            house['equipments'] = equipments

        # Dettagli Inserzionista
        advertiser = {}
        advertiser_block = driver.find_element(By.ID, 'module-contact-container')

        if len(advertiser_block.find_elements(By.CLASS_NAME, '_browserPhone')) > 0:
            phone = advertiser_block.find_element(By.CLASS_NAME, '_browserPhone')
            advertiser['phone'] = phone.text

        if len(advertiser_block.find_elements(By.CLASS_NAME, 'professional-name')) > 0:
            name_block = advertiser_block.find_element(By.CLASS_NAME, 'professional-name')
            advertiser_name = name_block.find_element(By.TAG_NAME, 'span')
            advertiser['name'] = advertiser_name.text

        if len(advertiser_block.find_elements(By.CLASS_NAME, 'ad-reference-container')) > 0:
            reference_block = advertiser_block.find_element(By.CLASS_NAME, 'ad-reference-container')
            reference_label = reference_block.find_element(By.TAG_NAME, 'p')
            advertiser['reference'] = reference_label.text

        if len(advertiser_block.find_elements(By.CLASS_NAME, 'advertiser-name-container')) > 0:
            advertiser_reference = advertiser_block.find_element(By.CLASS_NAME, 'advertiser-name-container')
            advertiser_reference_link = advertiser_reference.find_element(By.TAG_NAME, 'a')
            advertiser['fullname'] = advertiser_reference_link.text
            advertiser['link'] = advertiser_reference_link.get_attribute('href')

        house['advertiser'] = advertiser

        # Last Update
        stats_block = driver.find_element(By.ID, 'stats')
        stats_texts = stats_block.find_elements(By.CLASS_NAME,'stats-text')
        for item in stats_texts:
            item_text = item.text
            if 'Annuncio aggiornato' in item_text:
                house['lastUpdate'] = item_text 


        # Improve positions details
        position = {}
        print('Checking more details on the geo-position..')

        if len(driver.find_elements(By.ID, 'headerMap')) > 0:
            address = []
            position_block = driver.find_element(By.ID, 'headerMap')
            position_items = position_block.find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')
            for item in position_items:
                address.append(item.text)
            position['address'] = address
            house['fullAddress'] = position

        # Number of pics
        pictures_button = driver.find_element(By.CLASS_NAME,'icon-no-pics')
        # Look if there are some images
        if len(pictures_button.find_elements(By.TAG_NAME, 'span')) > 0:
            number_of_pictures = pictures_button.find_element(By.TAG_NAME, 'span').text
            house['numberOfPictures'] = number_of_pictures

        return house

