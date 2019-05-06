import unittest


class MyTestCase2(unittest.TestCase):

    @classmethod               # required for class method
    def setUpClass2(cls):       # this setUp class method is run ONCE before ALL tests
        print('*'*30)
        print('This method 2 will be called ONCE before all tests')
        print('*' * 30)

    def setUp(self):
        print('This method 2 will be called before each test')

    def test_a(self):
        print('It is a test c')
    def test_b(self):
        print('It is a test d')

    def tearDown(self):
        print('This method 2 will be called after each test')

    @classmethod
    def tearDownClass2(cls):
        print('*' * 30)
        print('This method 2 will be called ONCE after all tests')
        print('*' * 30)



if __name__ == '__main__':
    unittest.main()
