import time
import unittest
from random import randint

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get('https://learn.letskodeit.com/p/practice')
        # self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    # def tearDown(self):
    #     self.driver.quit()

    def test_screenshot(self):
        driver = self.driver
        windowsize = driver.get_window_size()
        print(windowsize)

        driver.find_element_by_link_text('Login').click()
        driver.find_element_by_id('user_email').send_keys('abc@email.com')
        driver.find_element_by_id('user_password').send_keys('abc123')
        driver.find_element_by_name('commit').click()

        # take a screenshot and save to the desired location
        self.generic_method_screenshot(driver)
        # driver.get_screenshot_as_file('C:\\Users\\Liudmila\\Desktop\\screenshot.png')
        # print('Screenshot is saved on users folder')
        driver.set_window_size(800, 200)
        windowsize1 = driver.get_window_size()
        print(windowsize1)

    def generic_method_screenshot(self, driver):
        """
        It is a good pracice to keep generic codes in one place and then call it in our tests
        Takes screenshot of the current open page
        param: driver
        return:
        """

        # filename = str(randint(1,60)) + '.png'
        #OR
        filename = str(round(time.time()* 1000)) + '.png'
        screenshotDirectory = 'C:\\Users\\Liudmila\\Desktop\\'
        destinationFile = screenshotDirectory + filename
        driver.get_screenshot_as_file(destinationFile)
        print('Screenshot is saved on users folder')










if __name__ == '__main__':
    unittest.main()
