from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NewReportPage (BasePage):
    # when we put driver in () within the class it gonna to be remembered & no need to put driver everywhere
    def __init__(self, driver):
        super(NewReportPage,self).__init__(driver)
        self.page_url = 'http://local.school.portnov.com:9595/symfony/web/index.php/core/definePredefinedReport'
        self.wait = WebDriverWait(self.driver, 2)

    def send_name(self, report_name):
        self.wait.until(ec.presence_of_element_located((By.ID, 'report_report_name'))).send_keys(report_name)

    def select_selection_criteria(self, param):
        Select(self.driver.find_element_by_id('report_criteria_list')).select_by_visible_text('Job Title')
        self.driver.find_element_by_id('btnAddConstraint').click()

    def select_display_field_groups(self, param):
        Select(self.driver.find_element_by_id('report_display_groups')).select_by_visible_text('Personal ')
        self.driver.find_element_by_id('btnAddDisplayGroup').click()

    def enable_display_fields(self):
        self.driver.find_element_by_id('display_group_1').click()

    def save(self):
        self.driver.find_element_by_id('btnSave').click()

