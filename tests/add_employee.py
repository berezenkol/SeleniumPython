import unittest
from random import randint

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import login, get_welcome_message, logout


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get('http://hrm-online.portnov.com')

        self.wait = WebDriverWait(self.driver, 10)
    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        empID = randint(100000, 999999)
        expected_Job_Title = 'QA Manager'
        expected_Employment_Status = 'Full Time'

        # after the Faker package is installed create a variable
        data = Faker()
        # expected_First_Name = 'Jamessss'
        # expected_Last_Name = 'Bondddd'

        expected_First_Name = data.first_name_female()
        expected_Last_Name = data.last_name_female()

        username = 'JBD' + str(empID)

        # login
        driver = self.driver

        login(self.driver)

        welcome_text = get_welcome_message(driver)
        # Expected value vs. Actual value
        self.assertEqual('Welcome Admin', welcome_text)

        # click the Add button
        driver.find_element_by_id('btnAdd').click()
        #todo  LB: may need to come back and do smt else

         # Enter First and Last names
        driver.find_element_by_id('firstName').send_keys(expected_First_Name)
        driver.find_element_by_id('lastName').send_keys(expected_Last_Name)

        # Enter and remember the empID
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys(empID)


        # Click Create Login Details checkbox
        driver.find_element_by_id('chkLogin').click()

        # wait for the fields to be available
        # fill them in
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID,'user_name'))).send_keys(username)
        driver.find_element_by_id('user_password').send_keys('password')
        driver.find_element_by_id('re_password').send_keys('password')

        # Save the employee
        driver.find_element_by_id('btnSave').click()

        driver.find_element_by_xpath('//*[@id="sidenav"]/li[6]/a').click()
        # todo LB: may need sleep
        driver.find_element_by_id('btnSave').click()
        locator = (By.CSS_SELECTOR, '.message.success')

        Select(driver.find_element_by_id('job_job_title')).select_by_visible_text(expected_Job_Title)
        Select(driver.find_element_by_id('job_emp_status')).select_by_visible_text(expected_Employment_Status)

        driver.find_element_by_id('btnSave').click()
        # todo LB: may need sleep

        # Go to PIM page
        driver.find_element_by_id('menu_pim_viewPimModule').click()
        # todo LB: may need to come back and do smt else

        # Search by empID
        driver.find_element_by_id('empsearch_id').send_keys(empID)
        driver.find_element_by_id('searchBtn').click()

        # Expected: 1 record back
        lst = driver.find_elements_by_xpath('//td[3]/a')
        self.assertTrue(len(lst) == 1)

        # Expected: correct Full Name
        firstName = driver.find_element_by_xpath('//td[3]/a').text
        lastName = driver.find_element_by_xpath('//td[4]/a').text
        Job_Title = driver.find_element_by_xpath('//td[5]').text
        Employment_Status = driver.find_element_by_xpath('//td[6]').text


        self.assertEqual(expected_First_Name, firstName)
        self.assertEqual(expected_Last_Name, lastName)
        self.assertEqual(Job_Title, expected_Job_Title)
        self.assertEqual(Employment_Status, expected_Employment_Status)

        # Log out
        # driver.find_element_by_id('welcome').click()
        # self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Logout'))).click()
        #driver.find_element_by_link_text('Logout').click() - instead of this line the whole code
        logout(self.wait, driver)

        # Log in
        login(driver,username)

        # Check Welcome message
        self.assertEqual('Welcome '+expected_First_Name,get_welcome_message(driver))

        # Log out
        logout(self.wait, driver)
        # driver.find_element_by_link_text('Logout').click() - instead of this line the whole code


if __name__ == '__main__':
    unittest.main()
