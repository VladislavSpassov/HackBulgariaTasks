import unittest

from RPN import rpn_calculate
class TestReversedPolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed(self):
        number = '45'
        self.assertEqual(rpn_calculate(number),int(number))
    def test_add_two(self):
        expr = "4 4 +"
        self.assertEqual(int(rpn_calculate(expr)),8)

    def test_sub_two(self):
        expr = "4 4 -"
        self.assertEqual(int(rpn_calculate(expr)),0)
    def test_mult_two(self):
        expr = "4 4 *"
        self.assertEqual(int(rpn_calculate(expr)),16)
    def test_div_two(self):
        expr = "4 4 /"
        self.assertEqual(int(rpn_calculate(expr)),1)
    
    def test_long_add(self):
        expr = "4 8 4 8 + + + "
        self.assertEqual(int(rpn_calculate(expr)),24)
    def test_long_mult(self):
        expr = "4 7 * 42 2 * * "
        self.assertEqual(int(rpn_calculate(expr)),2352)

    def test_long_substraction(self):
        expr = "18 123 - 12 2 4 - - -"

        self.assertEqual(int(rpn_calculate(expr)),-119)       
    '''def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
        expr = '4 8 +'
        expected_result = 12
        self.assertEqual(rpn_calculate(expr),expected_result)
    '''

if(__name__ == "__main__"):
    unittest.main()