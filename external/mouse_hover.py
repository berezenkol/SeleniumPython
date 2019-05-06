from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class MouseHovere():
    def test1(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get(baseURL)
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(3)

        #1. We scroll down the page
        driver.execute_script('window.scrollBy(0,800);')
        sleep(2)
        #2. Find the button which has the list of items
        mouse_hover_button = driver.find_element_by_id('mousehover')

        itemtoclickLocator = '//div[@class = "mouse-hover-content"]//a[text() = "Top"]'


        try:
            actions = ActionChains(driver)
            actions.move_to_element(mouse_hover_button).perform()
            print('Mouse hovered on element')
            sleep(2)
            topLink = driver.find_element_by_xpath(itemtoclickLocator)
            actions.move_to_element(topLink).click().perform()
            print('Item clicked')
        except:
            print('Failed')

        driver.quit()

ff = MouseHovere()
ff.test1()