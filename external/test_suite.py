import unittest

from external.test_logging.fixtures_udemy_1 import MyTestCase1
from external.test_logging.fixtures_udemy_2 import MyTestCase2


# get all test from from fixtures_udemy_1 and fixtures_udemy_2
tc1 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase2)

# create a TestSuite combining fixtures_udemy_1 and fixtures_udemy_2
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(smoke_test)