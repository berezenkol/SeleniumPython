
import unittest
import random
from random import randint


from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base import BaseTestCase


class GmailTestCase(BaseTestCase):
    def setUp(self):
        super(GmailTestCase, self).setUp()
        # self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get('https://accounts.google.com')
        # self.wait = WebDriverWait(self.driver, 5)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        super(GmailTestCase, self).tearDown()
        # self.driver.quit()

    def test_gmail_login(self):
        # s = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
        # passlen = 10
        # password = ''.join(random.sample(s, passlen))

        password = '30Bestgirl30'

        driver = self.driver

        driver.find_element_by_id('identifierId').send_keys('berezenkol.87@gmail.com')
        driver.find_element_by_xpath('//span[@class = "RveJvd snByac"]').click()
        driver.find_element_by_xpath('//input[@name = "password"]').send_keys(password)

        # self.wait.until(ec.visibility_of_element_located((By.XPATH,'//input[@type = "password"]'))).send_keys(password)
        driver.find_element_by_id('passwordNext').click()

        # sleep(7)
        self.assertEqual('Welcome, Liudmila Berezenko', driver.find_element_by_xpath('//h1[@class = "x7WrMb"]').text)










if __name__ == '__main__':
    unittest.main()
