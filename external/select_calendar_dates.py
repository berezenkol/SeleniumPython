from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Calendar():

    def test_select_calendar_dates(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.implicitly_wait(5)
        driver = self.driver
        driver.get('https://www.expedia.com/')
        driver.find_element_by_id('tab-flight-tab-hp').click()
        driver.find_element_by_id('flight-departing-hp-flight').click()
        driver.implicitly_wait(5)

        calMonth = driver.find_element_by_xpath('//div[@class = "datepicker-cal-month"][position()=1]')
        available_dates = calMonth.find_elements(By.XPATH,'//div[@class = "datepicker-cal-month"][position()=1]//button [@class ="datepicker-cal-date"]')
        print(len(available_dates))
        april25 = calMonth.find_element(By.XPATH,'//div[@class = "datepicker-cal-month"][position() = 1]//button[@data-day = "25"]')
        april25.click()

        driver.quit()

    def test_southwest(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.implicitly_wait(5)
        driver = self.driver
        driver.get('https://www.southwest.com/')
        driver.maximize_window()
        driver.find_element_by_id('LandingPageAirSearchForm_originationAirportCode').send_keys('NEW')
        sleep(2)
        itemToClick = None

        box = driver.find_element_by_xpath("//input[@id='LandingPageAirSearchForm_originationAirportCode']")

        box.clear()

        box.send_keys('New York')

        # this element contains a list of descendants generated after typing New York

        desc = driver.find_element_by_id('LandingPageAirSearchForm_originationAirportCode--menu')

        # You can't click the item as soon as you find it or the element gets destroyed during the for loop

        # and you get an exception even though it works. Store the element and click it after the loop

        # finishes

        for item in desc.find_elements_by_tag_name('li'):

            if str(item.text).endswith('EWR'):
                itemToClick = item

        itemToClick.click()

        driver.quit()
dd = Calendar()
# dd.test_select_calendar_dates()
dd.test_southwest()



