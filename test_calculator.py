#https://github.com/mpaquette1-svg/lab11-MP-MEG.git
#Partner 1: Matthew Paquette
#Partner 2: Miguel Gutierrez

import unittest
import calculator
import math


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):
        assert calculator.add(2,3) == 5
        assert calculator.add(-4,9) == 5
        assert calculator.add(0,0) == 0

    def test_subtract(self):
        assert calculator.subtract(10,4) == 6
        assert calculator.subtract(-2,-8) == 6
        assert calculator.subtract(-3,3) == -6
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(-3, 4), -12)
        self.assertEqual(calculator.mul(0, 10), 0)
        self.assertEqual(calculator.mul(2, 5), 10)

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(10,2),5)
        self.assertEqual(calculator.div(-9,3), -3)
        self.assertIsNone(calculator.div(10,0), 0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculator.div, 0, 7)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0)

        a, b = 3, 81
        expected = math.log(b) / math.log(a)
        self.assertAlmostEqual(calculator.logarithm(a, b), expected)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, calculator.logarithm, 1, 10)
        self.assertRaises(ValueError, calculator.logarithm, -2, 8)
        self.assertRaises(ValueError, calculator.logarithm, 2, 0)
        self.assertRaises(ValueError, calculator.logarithm, 2, -5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(0,5)
        with self.assertRaises(ValueError):
            calculator.logarithm(-10,10)
        self.assertAlmostEqual(calculator.logarithm(8,2),3)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(calculator.hypotenuse(3,4),5)
        self.assertEqual(calculator.hypotenuse(5,12), 13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            calculator.square_root(-9)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0),0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()