from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def login(driver, username = 'admin', password = 'password'):
    driver.find_element_by_id('txtUsername').send_keys(username)
    driver.find_element_by_id('txtPassword').send_keys(password)
    driver.find_element_by_id('btnLogin').click()


def get_welcome_message(driver):
    # locator = (By.ID, 'welcome')
    # WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(locator))
    # welcome_text = driver.find_element_by_id('welcome').text
    # return welcome_text

    return WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.ID, 'welcome'))).text


def logout(wait, driver):
    driver.find_element_by_id('welcome').click()
    wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()


def is_element_present(driver, by, locator):
    try:
        driver.find_element(by, locator)
        return True
    except NoSuchElementException:
        return False