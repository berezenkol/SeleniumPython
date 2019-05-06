

from pages.base_page import BasePage



class PIMPage(BasePage):
    # when we put driver in () within the class it gonna to be remembered & no need to put driver everywhere
    def __init__(self, driver):
        super(PIMPage, self).__init__(driver)
        self.page_url = 'http://local.school.portnov.com:9595/symfony/web/index.php/pim/viewEmployeeList'

    def goto_reports(self):
        driver = self.driver
        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_id('menu_core_viewDefinedPredefinedReports').click()

    def termination_reasons(self):
        driver = self.driver
        driver.find_element_by_id('menu_pim_Configuration').click()
        driver.find_element_by_id('menu_pim_viewTerminationReasons').click()











