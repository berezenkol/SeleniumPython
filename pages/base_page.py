from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import EXPLICIT_TIMEOUT
from pages.main_menu import MainMenu


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)
        # we will create instance of main_menu here. after that all other pages will inherit from it
        self.main_menu = MainMenu(self.driver)
        self.page_url = None

    def goto_page(self):
        self.driver.get(self.page_url)

    def get_header(self):
        return self.driver.find_element_by_css_selector('.head h1').text

