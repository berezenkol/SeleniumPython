from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class Sliders():
    def test1(self):
        baseURL = 'https://jqueryui.com/slider/'
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get(baseURL)
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(3)

        # 1. Switch to iframe where slider exist
        driver.switch_to.frame(0)

        #2. Find the slider locator
        slider_element = driver.find_element_by_xpath('//div[@id = "slider"]//span')
        sleep(2)

        try:
            actions= ActionChains(driver)
            actions.drag_and_drop_by_offset(slider_element,100,0).perform()
            print('Sliding Element Successfully')
            sleep(2)
        except:
            print('Not Success')

        driver.quit()

ff = Sliders()
ff.test1()