import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()  # Create an instance
        
    # Test addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    # Test subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    # Test multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
    # Test division
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    # Test division by zero
    def test_division_by_zero(self):
        self.assertEqual(self.calc.divide(10, 0), None)

if __name__ == "__main__":
    unittest.main()