from selenium.webdriver.common.by import By

from pages.base_page import BasePage

locators = {

    "add_button": (By.ID, 'btnAdd'),
    "search_textfield": (By.ID, 'search_search'),
    "search_button": (By.CLASS_NAME, 'searchBtn'),
}

class ReportsPage(BasePage):
    # when we put driver in () within the class it gonna to be remembered & no need to put driver everywhere
    def __init__(self, driver):
        super(ReportsPage, self).__init__(driver)
        self.page_url = 'http://local.school.portnov.com:9595/symfony/web/index.php/core/viewDefinedPredefinedReports/reportGroup/3/reportType/PIM_DEFINED'


    def add(self):
        driver = self.driver
        # after locators are created we have to replace the locators in the code with the created one
        # driver.find_element_by_id('btnAdd').click() -code before locators created&below the code with created locators
        # to choose the locator - in [] press CTRL + space
        # [1] - index for second part of locator on dictionary ('btnAdd') [0]for first part (By.ID)
        driver.find_element_by_id(locators["add_button"][1]).click()

    def search(self, report_name):
        driver = self.driver
        driver.find_element_by_id(locators["search_textfield"][1]).send_keys(report_name)
        driver.find_element_by_class_name(locators["search_button"][1]).click()
    def run(self, report_name):
        self.driver.find_element_by_xpath("//td[text()='{0}']/../td[3]/a".format(report_name)).click()






