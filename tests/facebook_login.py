import unittest
from time import sleep

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get("https://www.facebook.com/")

    def test_facebook_login(self):
        driver = self.driver
        driver.find_element_by_id('email').send_keys('malisha789@rambler.ru')
        driver.find_element_by_id('pass').send_keys('31Bestgirl31')
        driver.find_element_by_id('u_0_2').click()

        sleep(2)

        find_friends = driver.find_element_by_id('findFriendsNav').text

        # Expected value vs. Actual value

        self.assertEqual('Find Friends', find_friends)



if __name__ == '__main__':
    unittest.main()
