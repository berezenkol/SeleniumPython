import unittest

from fixtures.base import POMAdminLoginTestCase

from pages.pim_page import PIMPage


class MyTestCase(POMAdminLoginTestCase):
    def setUp(self):
        super(MyTestCase,self).setUp()
    def tearDown(self):
        super(MyTestCase,self).tearDown()

    def test_something(self):
        driver = self.driver
        pim_page = PIMPage(self.driver)
        pim_page.goto_reports()

        self.assertEqual('Employee Reports',driver.find_element_by_css_selector('.head h1').text)

    def test_performance_tab(self):
        driver = self.driver
        driver.find_element_by_id('menu_performance_viewPerformanceModule').click()
        self.assertEqual('Search Performance Reviews', driver.find_element_by_css_selector('.head h1').text)

    def test_pim_page(self):
        driver = self.driver
        pim_page_more = PIMPage(self.driver)
        pim_page_more.termination_reasons()

        self.assertEqual('Termination Reasons', driver.find_element_by_xpath('//h1[text()="Termination Reasons"]').text)

    def test_memberships(self):
        driver = self.driver
        pim_page_more = PIMPage(self.driver)
        pim_page_more.main_menu.selectMemberships()

        self.assertEqual('Memberships', driver.find_element_by_xpath('//h1[text()="Memberships"]').text)












if __name__ == '__main__':
    unittest.main()
