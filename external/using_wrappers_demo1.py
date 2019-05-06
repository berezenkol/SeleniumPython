from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from external.handy_wrappers import HandyWrappers


class UsingWrappers():
    def test(self):
        baseURL = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        textfield = hw.getElement('name',locatorType = 'id')
        textfield.send_keys('Test')
        sleep(2)


        # textfield = driver.find_element(By.ID, 'name') - we will use object from HandyWrappers
        # textfield.send_keys('Test')

ff = UsingWrappers()
ff.test()