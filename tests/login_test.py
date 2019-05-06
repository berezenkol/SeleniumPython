import unittest
from time import sleep

from selenium import webdriver

from steps.common import get_welcome_message


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get("http://hrm-online.portnov.com")

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        sleep(3)
        driver.find_element_by_id('btnLogin').click()

        welcome_text = get_welcome_message(driver)

        # Expected value vs. Actual value

        self.assertEqual('Welcome Admin', welcome_text)

    def test_invalid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('administrator')
        driver.find_element_by_id('btnLogin').click()

        sleep(2)

        invalid_credentials = driver.find_element_by_id('spanMessage').text
        self.assertEqual('Invalid credentials', invalid_credentials)

    def test_empty_password(self):
        driver = self.driver

        # just practice of different types of selectors
        # 1. by id
        # driver.find_element_by_id('txtUsername').send_keys('admin')
        # 2. by xpath
        # driver.find_element_by_xpath('//input[@name = "txtUsername"]').send_keys('admin')
        # 3. by css
        driver.find_element_by_css_selector('input[name = "txtUsername"]').send_keys('admin')

        driver.find_element_by_id('txtPassword').send_keys('')
        driver.find_element_by_id('btnLogin').click()

        sleep(2)

        empty_password = driver.find_element_by_id('spanMessage').text
        self.assertEqual('Password cannot be empty', empty_password)


if __name__ == '__main__':
    unittest.main()
