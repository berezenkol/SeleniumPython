from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import EXPLICIT_TIMEOUT


class MainMenu(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)
        #for Action Chains Object we need to create a variable
        self.action = ActionChains(self.driver)

    def selectLocalizationmenuitem(self):
      driver = self.driver

        # we can create a variable and then pass in this var OR can pass in the entire code
      admin_menu = driver.find_element_by_id('menu_admin_viewAdminModule')
      # the below 3 codes are to be grabed and passed into move_to_element(here)
      # driver.find_element_by_id('menu_admin_UserManagement')
      # driver.find_element_by_id('menu_admin_Configuration')
      # driver.find_element_by_id('menu_admin_localization')

    # 1 way to call self.action line at a time (as below)
    #   self.action.move_to_element(admin_menu)
    #   self.action.move_to_element(driver.find_element_by_id('menu_admin_UserManagement'))
    #   self.action.move_to_element(driver.find_element_by_id('menu_admin_Configuration'))
    #   self.action.move_to_element(driver.find_element_by_id('menu_admin_localization')))

    # 2 way BEST!!! we can call the multiple commands in one line of code (as below)
      self.action.move_to_element(admin_menu).move_to_element(
          driver.find_element_by_id('menu_admin_UserManagement')).move_to_element(
          driver.find_element_by_id('menu_admin_Configuration')).click(
          driver.find_element_by_id('menu_admin_localization')).perform()
        # ActionsChain will not work until we call the .perorm()

    def selectMemberships(self):
        driver = self.driver
        admin_menu = driver.find_element_by_id('menu_admin_viewAdminModule')
        self.action.move_to_element(admin_menu).move_to_element(
            driver.find_element_by_id('menu_admin_UserManagement')).move_to_element(
            driver.find_element_by_id('menu_admin_Qualifications')).click(
            driver.find_element_by_id('menu_admin_membership')).perform()

    def selectMyinfo(self):
        driver = self.driver

        driver.find_element_by_id('menu_pim_viewMyDetails').click()



