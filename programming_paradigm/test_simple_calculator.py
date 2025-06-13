import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_simple_calculator(self):
        calc = SimpleCalculator()  # Create an instance
        
        # Test addition
        test_addition = calc.add(2, 3)
        self.assertEqual(test_addition, 5)
        # Test subtraction
        test_subtraction = calc.subtract(5, 3)
        self.assertEqual(test_subtraction, 2)
        # Test multiplication
        test_multiplication = calc.multiply(3, 4)
        self.assertEqual(test_multiplication, 12)
        # Test division
        test_division = calc.divide(10, 2)
        self.assertEqual(test_division, 5)
        # Test division by zero
        result = calc.divide(10, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()