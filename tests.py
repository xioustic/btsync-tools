import unittest
import verify

'''
The main methods that we make use of in unit testing for Python are:

assert: base assert allowing you to write your own assertions
assertEqual(a, b): check a and b are equal
assertNotEqual(a, b): check a and b are not equal
assertIn(a, b): check that a is in the item b
assertNotIn(a, b): check that a is not in the item b
assertFalse(a): check that the value of a is False
assertTrue(a): check the value of a is True
assertIsInstance(a, TYPE): check that a is of type "TYPE"
assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR
'''
 
class MainTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
 
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
 
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
 
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
 
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
 
class VerifyTests(unittest.TestCase):
    def setUp(self):
        tesdc

    def test_generate(self):
        verify.generateVerification('password',100000)

if __name__ == '__main__':
    unittest.main()