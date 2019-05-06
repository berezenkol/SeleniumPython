from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class DragandDrop():
    def test1(self):
        baseURL = 'https://jqueryui.com/droppable/'
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get(baseURL)
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(3)

        #1. switch to iframe inside which we have our elements
        driver.switch_to.frame(0)

        #2. identify 2 elements we are planning to work with
        drag_element_from = driver.find_element_by_id('draggable')
        drop_element_to = driver.find_element_by_id('droppable')
        sleep(2)

        #3. Perform ActionChains
        # try:
        actions = ActionChains(driver)
        # actions.drag_and_drop(drag_element_from, drop_element_to).perform()
        actions.click_and_hold(drag_element_from).move_to_element(drop_element_to).release().perform()
        print('Drag and Drop element successfully')
        sleep(2)
        # except:
        #     print('Not success')

        driver.quit()


ff = DragandDrop()
ff.test1()