from fixtures.params import DOMAIN
from pages.base_page import BasePage


class LoginPage(BasePage):
    # when we put driver in () within the class it gonna to be remembered & no need to put driver everywhere
    def __init__(self, driver):
        super(LoginPage,self).__init__(driver)
        self.page_url = DOMAIN + '/symfony/web/index.php/auth/login'


# copy login from common and paste the entire code below then delete the created def login
# we remove driver from def login () and pass in self, below we write the driver = self.driver
    # because we created an instance using set up we passed in driver immediately
    def login(self, username = 'admin', password = 'password'):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id('btnLogin').click()
