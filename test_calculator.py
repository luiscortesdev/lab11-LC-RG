import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertion#
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(8, 4), 12)
        self.assertEqual(add(-10, 20), 10)



    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6,3),3)
        self.assertEqual(subtract(5,4),1)
        self.assertEqual(subtract(-5,5),-10)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,0), 0)
        self.assertEqual(mul(10, 10), 100)
        self.assertEqual(mul(-12, 6), -72)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(6, 2), 1/3)
        self.assertEqual(div(50, 100), 2)
        self.assertEqual(div(-11, 77), -7)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(5,25),2)
        self.assertEqual(logarithm(3,27),3)
        self.assertEqual(logarithm(2,16),4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5,25)
    #     # use same technique from test_divide_by_zero
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        self.assertEqual(logarithm(2, 1), 0)
        self.assertAlmostEqual(logarithm(5, 125), 3)
        self.assertEqual(logarithm(4, 4), 1)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(7, 24), 25)
        self.assertEqual(hypotenuse(50, 120), 130)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            square_root(-12)
    #     # Test basic function
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(100), 10)
        self.assertEqual(square_root(25), 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()