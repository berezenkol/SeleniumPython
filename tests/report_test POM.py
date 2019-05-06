import random
import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base import POMAdminLoginTestCase
from pages import login_page
from pages.login_page import LoginPage
from pages.new_report_page import NewReportPage
from pages.pim_page import PIMPage
from pages.report_run_page import ReportRunPage
from pages.reports_page import ReportsPage


class ReportTestCase(POMAdminLoginTestCase):

    def setUp(self):
        # after inheritance from POMAdminLoginTestCase I dont need 3 below lines as the super is created
        super(ReportTestCase, self).setUp()
        # self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        # self.driver.get('http://hrm-online.portnov.com')
        # self.wait = WebDriverWait(self.driver, 2)


        # creating an instance for step login_page
        #the same as we did with WebDriverWait: we created the variable instance(self.wait) and this variable we are using
        # o call all the functions. The same approach we use with all our pages: We create the instance variables to hold
        # the object (LoginPage - is an object)

        # self.login_page = LoginPage(self.driver)    - a part of super,setup()
        # we create the rest pages (just copy the login_page & paste with dedicated page name)
        self.pim = PIMPage(self.driver)
        self.reports = ReportsPage(self.driver)
        self.new_report = NewReportPage(self.driver)
        self.report_run = ReportRunPage(self.driver)

    def tearDown(self):
        # driver = self.driver
        # report_name = 'berezenkol_report # ' + str(random.randint(50, 200))
        # self.report_name = report_name
        # if self.report_name:
            # 2. Click on thePIM and the report tab
            # driver.find_element_by_id('menu_pim_viewPimModule').click()
            # driver.find_element_by_id('menu_core_viewDefinedPredefinedReports').click()
            # driver.find_element_by_id('search_search').send_keys(self.report_name)
            # driver.find_element_by_class_name('searchBtn').click()
            # driver.find_element_by_xpath('//td/input[@type="checkbox"]').click()
            # driver.find_element_by_id('btnDelete').click()
            # self.wait.until(ec.visibility_of_element_located((By.ID, 'dialogDeleteBtn'))).click()
            # ...by_css_selector ('td>input')

        # 11. tearDown: remove the report

        # self.driver.quit()
        super(ReportTestCase, self).tearDown()

    def test_create_report(self):
        report_name = 'berezenkol_report # ' + str(random.randint(50, 200))

        #Test Driven Development concept (no locators, just steps)

        # login is yellow, to avoid this we click on yellow bulb and choose Add method
        # login_page.login()        - a part of super,setup()
        # to make not red we need to add self. at the beginning
        self.pim.goto_reports()
        self.reports.add()
        # to make report_name not red we copy the report_name = ... from below test & paste above
        self.new_report.send_name(report_name)
        self.new_report.select_selection_criteria('Job Title')
        self.new_report.select_display_field_groups('Personal')
        self.new_report.enable_display_fields()
        self.new_report.save()
        self.reports.search(report_name)
        # assertions maybe
        self.reports.run(report_name)
        # get - it returns smt so we save it in a variable
        report_header = self.report_run.get_report_header()
        # assertion here



        # report_name = 'berezenkol_report # ' + str(random.randint(50, 200))
        #
        # # 1. Log in
        # driver = self.driver
        # login(driver)
        #
        # # 2. Click on thePIM and the report tab
        # driver.find_element_by_id('menu_pim_viewPimModule').click()
        # driver.find_element_by_id('menu_core_viewDefinedPredefinedReports').click()
        #
        # # 3. Click on the Add button
        # # 4. Enter the unique report name
        # driver.find_element_by_id('btnAdd').click()
        # self.wait.until(ec.presence_of_element_located((By.ID, 'report_report_name'))).send_keys(report_name)
        #
        # # 4. Enter the unique report name
        # # driver.find_element_by_id('report_report_name').send_keys(report_name) - combined below
        #
        # # 5. Select criteria = Job title & click Add
        # Select(driver.find_element_by_id('report_criteria_list')).select_by_visible_text('Job Title')
        # driver.find_element_by_id('btnAddConstraint').click()
        #
        # # 6. Select Display Field Group = Personal & click Add
        # Select(driver.find_element_by_id('report_display_groups')).select_by_visible_text('Personal ')
        # driver.find_element_by_id('btnAddDisplayGroup').click()
        #
        # # 7. make sure to check the checkbox and save
        # driver.find_element_by_id('display_group_1').click()
        # driver.find_element_by_id('btnSave').click()
        #
        # # 8. verify the report was created
        # #for this purpose we create a function
        # self.assertTrue(is_element_present(self.driver, By.XPATH, "//td[text()='{0}']".format(report_name)))
        #
        # # yes, a report was created and requires a cleanup
        # self.report_name = report_name
        #
        #
        # # 9. run the report
        # # driver.find_element_by_xpath("//td[text()='Ted']/../td[3]/a").click
        # driver.find_element_by_xpath("//td[text()='{0}']/../td[3]/a".format(report_name)).click()
        #
        # # 10. verify the report works
        # report_header = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#search-results > div.head > h1'))).text
        # self.assertEqual('Report Name : {0}'.format(report_name), report_header)


if __name__ == '__main__':
    unittest.main()
