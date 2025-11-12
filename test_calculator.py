import unittest
import calculator
import math


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):
        assert calculator.add(2,3) == 0
        assert calculator.add(-4,9) == 5
        assert calculator.add(0,0) == 0

    def test_subtract(self):
        assert calculator.sub(10,4) == 6
        assert calculator.sub(-2,-8) == 6
        assert calculator.sub(-3,3) == -6
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculator.div, 0, 7)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)
        self.assertAlmostEqual(calculator.log(10, 1000), 3.0)

        a, b = 3, 81
        expected = math.log(b) / math.log(a)
        self.assertAlmostEqual(calculator.log(a, b), expected)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, calculator.log, 1, 10)
        self.assertRaises(ValueError, calculator.log, -2, 8)
        self.assertRaises(ValueError, calculator.log, 2, 0)
        self.assertRaises(ValueError, calculator.log, 2, -5)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()