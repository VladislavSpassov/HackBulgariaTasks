import unittest
from ReversedPolishNotation import rpn_calculate


class TestReversedPolishNotation(unittest.TestCase):
    
    def test_when_single_digit_is_passed(self):
        number = 45
        self.assertEqual(rpn_calculate(number),number)
    def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
        expr = '4 8 +'
        expected_result = 12



if(__name__ == "__main__"):
    unittest.main()