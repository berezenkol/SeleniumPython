from time import sleep

from selenium import webdriver


class JavaScriptPopUp():
    def test1(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get(baseURL)
        driver = self.driver
        driver.maximize_window()

       # 1. Accept alert
        driver.find_element_by_id('name').send_keys('Liudmila')
        driver.find_element_by_id('alertbtn').click()
        sleep(2)

        alert1 = driver.switch_to.alert  # will switch to the existing alert
        alert1.accept()                  # to accept the alert

        # 2. Cancel the alert
        sleep(2)
        driver.find_element_by_id('name').send_keys('Liudmila')
        driver.find_element_by_id('confirmbtn').click()
        sleep(2)

        alert2 = driver.switch_to.alert
        alert2.dismiss()                 # to cancel the alert

        driver.quit()
ff = JavaScriptPopUp()
ff.test1()