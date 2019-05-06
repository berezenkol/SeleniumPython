import unittest

from fixtures.base import POMAdminLoginTestCase
from pages.main_menu import MainMenu
from pages.pim_page import PIMPage


class MenuTestCase(POMAdminLoginTestCase):
    def test_localization_menu(self):
        # 1 way: use the main_menu through the page
        pim_page = PIMPage(self.driver)
        pim_page.main_menu.selectLocalizationmenuitem()
                           # OR
        # 2 way: use the main_menu directly from main_menu (if we don't have a page)
        main_menu = MainMenu(self.driver)
        main_menu.selectLocalizationmenuitem()




        # to check the place is correct or not we have to assert by header or url (True - expected, False - actual)
        # 1. checking the header (Localization)
        self.assertEqual('Localization', self.driver.find_element_by_id('localizationHeading').text)
        # 2. checking the URL
        # find looks for word 'localization' in the current_url. If this word is at the beginning of the url - it returns 0
        # but we know that this word is not at the beginning , so when it is found some positive number will be returned.
        # That is why we put >0
        self.assertTrue(self.driver.current_url.find('localization') > 0)

    def test_my_info_menu(self):
        my_info_page = MainMenu(self.driver)
        my_info_page.selectMyinfo()

        # The correct way would be to create a MyInfoPage instance & then call get_header() function from base_page
        # checking the header
        self.assertEqual('Personal Details', self.driver.find_element_by_css_selector('.head h1').text)

        # if we minimize the window and want to click on Job we will not be able to do that with regular driver.find_element_by....
        # instead we will use the execute_script command (see below)

        # 1. we set up the window size
        self.driver.set_window_size(200,300)

        #2. this should result in a WebDriverException "unknown error....element is not clackable"
        self.driver.find_element_by_link_text('Job').click()

        #3. Lets use command to 'fake' click it
        #A. this is about Java script (("document.querySelector('#sidenav > li:nth-child(6) > a').click()")
        # self.driver.execute_script("document.querySelector('#sidenav > li:nth-child(6) > a').click()")

                                    #OR
        #B. this is about webdriver
        # self.driver.execute_script("arguments[0].click()",self.driver.find_element_by_link_text('Job'))

        self.assertEqual('Job', self.driver.find_element_by_css_selector('.head h1').text)

if __name__ == '__main__':
    unittest.main()
