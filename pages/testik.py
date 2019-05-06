import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.new_report_page import NewReportPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 2)

        self.login_page = LoginPage(self.driver)
        self.new_report_page = NewReportPage(self.driver)

        self.login_page.goto_page()
        # self.driver.get('http://local.school.portnov.com:9595/symfony/web/index.php/auth/login')

    def tearDown(self):
        self.driver.quit()

    def test_create_report(self):

        self.login_page.login()
        self.new_report_page.goto_page()

        self.driver.current_url

if __name__ == '__main__':
    unittest.main()


