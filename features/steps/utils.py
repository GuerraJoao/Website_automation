import time

import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def click_on_element(driver, element):
    action = ActionChains(driver)
    action.click(on_element=element)
    action.perform()


def insert_text(driver, element, text):
    # Leaving a field empty in the feature file is different from a empty string, so I decided to use the 'empty' string
    action = ActionChains(driver)
    action.click(on_element=element)
    # to represent an empty string, and thus no text is input
    if text != 'empty':
        action.send_keys(text)
    action.perform()


def wait_until_find_element_by_id(driver, element_id, delay=1, max_tries=5):
    for i in range(max_tries - 1):
        try:
            return driver.find_element(By.ID, element_id)
        except NoSuchElementException:
            time.sleep(delay)
    return driver.find_element(By.ID, element_id)

