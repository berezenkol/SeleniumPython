import random
import unittest


from selenium import webdriver


class Calculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Liudmila\PycharmProjects\first\browser_drivers\chromedriver.exe')
        self.driver.get('http://www.math.com/students/calculators/source/basic.htm')

    def tearDown(self):
        self.driver.quit()

    def enter_random_numbers(self):
        num = random.randint(0, 999)
        #in order to split the number into pieces I have to convert it into a string
        list_of_numbers = list(str(num))

        for number in list_of_numbers:
            self.driver.find_element_by_css_selector('input[value="  {0}  "]'.format(number)).click()
        return num   # we dont know which num1 and num2 will be created, so we have to return the num

    def test_add_numbers(self):
        driver =self.driver

        # self.driver.find_element_by_name('one').click()
        # better to use css selector: input - is a tag, then specify attribute (it is a value)
        driver.find_element_by_css_selector('input[value="  1  "]').click()
        driver.find_element_by_css_selector('input[value="  +  "]').click()
        driver.find_element_by_css_selector('input[value="  2  "]').click()
        driver.find_element_by_name('DoIt').click()

        result = driver.find_element_by_name('Input').get_attribute('value')


        self.assertEqual(3, int(result))


    def test_random_numbers(self):
        driver = self.driver

        #for purpose of def enter_random_numbers I comment 2 lines below
        # num1 = random.randint(0,9)
        # num2 = random.randint(0,9)
        operator = random.choice(['+', ' -', '*', ' /'])

        # self.driver.find_element_by_name('one').click()
        # better to use css selector: input - is a tag, then specify attribute (it is a value)
        # driver.find_element_by_css_selector('input[value="  {0}  "]'.format(num1)).click()
        #instead of line below we can use the function to enter random 3-digit nymbers
        num1 = self.enter_random_numbers()       # it will be num1
        driver.find_element_by_css_selector('input[value="  {0}  "]'.format(operator)).click()
        # the same with num2 as above
        # driver.find_element_by_css_selector('input[value="  {0}  "]'.format(num2)).click()
        num2 = self.enter_random_numbers()       # it will be num2
        driver.find_element_by_name('DoIt').click()

        result = driver.find_element_by_name('Input').get_attribute('value')

        # after if/else statements are done, expected_result = None no more needed
        # expected_result = None
        if operator == '+':
            expected_result = num1+num2
        elif operator == ' -':
            expected_result = num1 - num2
        elif operator == '*':
            expected_result = num1 * num2
        else:
            if num2 is 0:
                expected_result = 'Infinity'
            else:
                expected_result = num1 / num2

        self.assertEqual(expected_result, int(result))

if __name__ == '__main__':
    unittest.main()
