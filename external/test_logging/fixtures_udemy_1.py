import unittest


class MyTestCase1(unittest.TestCase):

    @classmethod               # required for class method
    def setUpClass1(cls):       # this setUp class method is run ONCE before ALL tests
        print('*'*30)
        print('This method 1 will be called ONCE before all tests')
        print('*' * 30)

    def setUp(self):
        print('This method 1 will be called before each test')

    def test_a(self):
        print('It is a test a')
    def test_b(self):
        print('It is a test b')

    def tearDown(self):
        print('This method 1 will be called after each test')

    @classmethod
    def tearDownClass1(cls):
        print('*' * 30)
        print('This method 1 will be called ONCE after all tests')
        print('*' * 30)



if __name__ == '__main__':
    unittest.main()
