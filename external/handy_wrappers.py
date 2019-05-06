# it is a Framework approach
#we create this class to find elements

from selenium.webdriver.common.by import By


class HandyWrappers():
    def __init__(self,driver):   # - we need driver to perform actions; if we need smt from oitside - we need __init__ method
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()

        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        else:
            print('This locator type is not supported')
        return False

    def getElement(self,locator,locatorType = 'id'):

        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print('Element is found')
        except:
            print('Element is not found')
        return element

    def is_element_present(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print('Elemnet is found')
                return True
            else:
                return False

        except:
            print('Element is not found')
            return False

        #OR

    def elementPresenceCheck(self,locator, byType):
        try:
            elementlist = self.driver.find_elements(byType, locator)
            if len(elementlist) > 0:
                print('Elemnet is found')
                return True
            else:
                return False

        except:
            print('Element is not found')
            return False



# after we created this class we can use it in using_wrappers_demo1





