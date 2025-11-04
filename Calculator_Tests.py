import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    """Standard arithmetic operations"""
    def test_addition(self):
        calc = Calculator(5, 3, "+")
        self.assertEqual(calc.calculate(), 8)

    def test_subtraction(self):
        calc = Calculator(10, 4, "-")
        self.assertEqual(calc.calculate(), 6)

    def test_multiplication(self):
        calc = Calculator(7, 6, "*")
        self.assertEqual(calc.calculate(), 42)

    def test_division(self):
        calc = Calculator(8, 2, "/")
        self.assertEqual(calc.calculate(), 4)

    """Exceptional scenarios"""
    def test_division_by_zero(self):
        calc = Calculator(5, 0, "/")
        with self.assertRaises(ZeroDivisionError):
            calc.calculate()

    def test_invalid_operation(self):
        calc = Calculator(5, 5, "%")  # unsupported operation
        with self.assertRaises(Exception):
            calc.calculate()

    """Boundary cases"""
    def test_zero_addition(self):
        calc = Calculator(0, 0, "+")
        self.assertEqual(calc.calculate(), 0)

    def test_negative_numbers(self):
        calc = Calculator(-5, -3, "+")
        self.assertEqual(calc.calculate(), -8)

    def test_large_numbers(self):
        calc = Calculator(1e6, 1e6, "+")
        self.assertEqual(calc.calculate(), 2e6)

    """Type errors"""
    def test_non_numeric_input_a(self):
        with self.assertRaises(TypeError):
            Calculator("5", 5, "+")

    def test_non_numeric_input_b(self):
        with self.assertRaises(TypeError):
            Calculator(5, "3", "-")

    def test_invalid_operation_type(self):
        with self.assertRaises(TypeError):
            Calculator(5, 5, 10)

if __name__ == "__main__":
    unittest.main()