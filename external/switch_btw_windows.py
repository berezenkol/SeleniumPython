from time import sleep

from selenium import webdriver


class SwitchWindows():

    def test1(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get(baseURL)
        driver = self.driver


        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print('Parent handle: ' + parentHandle)

        # Find Open Window button and click it
        driver.find_element_by_id('openwindow').click()
        sleep(2)

        #Find all handles: there should be 2 handles after clicking open window button
        handles = driver.window_handles

        #Swith to window and search for course
        for handle in handles:
            print('2 open handles: ' + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)         # this is the method to switch btw windows
                print('Switched to new window' + handle)
                searchBox = driver.find_element_by_id('search-courses')
                searchBox.send_keys('python')
                sleep(2)
                driver.close()
                break

        #Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element_by_id('name').send_keys('Hello')


ff = SwitchWindows()
ff.test1()

