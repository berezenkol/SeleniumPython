from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

# to inherit from BasePage we put (BasePage) & import

class ReportRunPage (BasePage):

    # when we put driver in () within the class it gonna to be remembered & no need to put driver everywhere
    def __init__(self, driver):
        super(ReportRunPage, self).__init__(driver)
        self.wait = WebDriverWait(self.driver,2)
        # below 2 lines are no more needed, instead of it super. init
        # self.driver = driver
        # self.wait = WebDriverWait(self.driver, 2)

        self.page_url = ('http://local.school.portnov.com:9595/symfony/web/index.php/core/displayPredefinedReport?reportId=7')
        # super  - refers to parent page

    # we want to go directly to the certain page
    # def goto_page(self):
    #     self.driver.get(self.page_url)
    # after added (BasePage) we can remove this code because now it inheriting from the parent


    def get_report_header(self):
        return self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#search-results > div.head > h1'))).text


