from time import sleep

from selenium import webdriver


class IFrame():

    def test1(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        self.driver = webdriver.Chrome \
            (executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get(baseURL)
        self.driver.maximize_window()
        driver = self.driver

        # 1. We have to scroll down the page (we can do it using Java Script)
        driver.execute_script('window.scrollBy(0,1000);')

        # 2. Switch to the iframe using ID
        # driver.switch_to.frame('courses-iframe')   # 'id of the iframe'

        # 2a. Switch to the iframe using Name
        # driver.switch_to.frame('iframe-name')

        # 2b. Switch to the iframe using numbers
        driver.switch_to.frame(0)  # 0 because we have 1 iframe on the page, we know that indexing starts from 0

        sleep(2)

        # 3. Search course in iframe
        iframe_searchBox =  driver.find_element_by_id('search-courses')
        iframe_searchBox.send_keys('python')

        sleep(2)

        # 4. Switch back to the parent frame
        driver.switch_to.default_content()

        # 5. We have to scroll up the page (we can do it using Java Script)
        driver.execute_script('window.scrollBy(0,-1000);')
        sleep(2)

        # 6. Find element on the parent frame
        driver.find_element_by_id('name').send_keys('Success')
        sleep(2)
        driver.quit()


ff = IFrame()
ff.test1()