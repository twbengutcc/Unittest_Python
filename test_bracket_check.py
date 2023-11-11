import unittest
from bracket_check import bracket_check


class MyTestCase(unittest.TestCase):
    def test_no_error(self):
        test_string = '[{(Hello)}]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, False)  # add assertion here

    def test_error_1(self):
        test_string = '[{(Hello})]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)

    def test_error_2(self):
        test_string = '[{(Hello'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)

    def test_error_3(self):
        test_string = 'Hello)('
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)

    def test_error_4(self):
        test_string = '{}{'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        self.assertEqual(location, [2])


if __name__ == '__main__':
    unittest.main()
