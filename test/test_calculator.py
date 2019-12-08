"""Test file for the calculator"""
import unittest
from calculator.calculator import Calculator, get_number


class TestCalculator(unittest.TestCase):
    """Test for the Calculator"""

    def setUp(self):
        self.cal = Calculator()

    def test_get_number(self):
        """Test get_number function"""
        self.assertEqual(get_number("10"), 10)
        self.assertEqual(get_number("0b10"), 2)
        self.assertEqual(get_number("0x10"), 16)
        self.assertEqual(get_number("0o10"), 8)
        self.assertEqual(get_number("0.25"), 0.25)

    def test_add(self):
        """Test add method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.add()
        self.assertEqual(self.cal.stack.pop(), 15)

    def test_div(self):
        """Test div method"""
        self.cal.stack.clear()

        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.div()
        self.assertEqual(self.cal.stack.pop(), 0.5)

        # If div by 0, the stack remains the same
        self.cal.stack.append(5)
        self.cal.stack.append(0)
        self.cal.div()
        self.assertEqual(len(self.cal.stack), 2)

    def test_pow(self):
        """Test pow method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.pow()
        self.assertEqual(self.cal.stack.pop(), 5**10)

        self.cal.stack.append(5)
        self.cal.stack.append(0)
        self.cal.pow()
        self.assertEqual(self.cal.stack.pop(), 1)
