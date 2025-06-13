import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_simple_calculator(self):
        calculator = SimpleCalculator()  # Create an instance
        # Test addition
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)
        # Test subtraction
        result = calculator.subtract(5, 3)
        self.assertEqual(result, 2)
        # Test multiplication
        result = calculator.multiply(3, 4)
        self.assertEqual(result, 12)
        # Test division
        result = calculator.divide(10, 2)
        self.assertEqual(result, 5)
        # Test division by zero
        result = calculator.divide(10, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()