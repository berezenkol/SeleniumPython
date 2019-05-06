from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from external.handy_wrappers import HandyWrappers


class ElementPresenceCheck():
    def test(self):
        baseURL = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        textfield = hw.is_element_present('name',By.ID)
        print(str(textfield))

ff = ElementPresenceCheck()
ff.test()