import unittest
from time import sleep

from selenium import webdriver

from fixtures.base import AdminLoginTestCase
from steps.common import login


class MyTestCase(AdminLoginTestCase):
    def setUp(self):
        # after the inheritance happened I can delete the def tear down & webdriver.Chrome
        # and add the super class line code
        # self.driver = webdriver.Chrome(executable_path = r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        super(MyTestCase, self).setUp()
        #after in base the new class is created which is resp for url open and login, the below line is no more needed
        # self.driver.get('http://hrm-online.portnov.com')

    def tearDown(self):
        super(MyTestCase,self).tearDown()

    def test_something(self):

        # hrm login
        driver = self.driver

        # login(self.driver)  - this line is no more needed after inheritance from AdminLoginTestCase

        sleep(2)

        # check the size of logo

        logo = driver.find_element_by_xpath('//*[@id="branding"]/img')
        logo_size = logo.size

        self.assertTrue('56', logo_size.get('height'))

        # check the logo is on the top left

        window_size = driver.get_window_size()

        logo_location = logo.location

        top_right_corner_x_location = logo_size.get('width') + logo_location.get('x')

        # The entire logo (width) fits within the left half of the window

        self.assertTrue(top_right_corner_x_location < window_size.get('width')/2)



if __name__ == '__main__':
    unittest.main()
