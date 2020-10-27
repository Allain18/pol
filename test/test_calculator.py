"""Test file for the calculator"""

import sys
import unittest
import math
from io import StringIO

from rpn_calc.calculator import Calculator, get_number


class TestCalculator(unittest.TestCase):
    """Test for the Calculator"""

    def setUp(self):
        self.stdout = StringIO()
        sys.stdout = self.stdout
        self.cal = Calculator()

    def test_get_number(self):
        """Test get_number function"""
        self.assertEqual(get_number("10"), 10)
        self.assertEqual(get_number("0b10"), 2)
        self.assertEqual(get_number("0x10"), 16)
        self.assertEqual(get_number("0o10"), 8)
        self.assertEqual(get_number("0.25"), 0.25)
        self.assertEqual(get_number("0xaaa"), 2730)
        self.assertEqual(get_number("alc"), "alc")

    def test_loop(self):
        """Test loop method"""
        stdin = StringIO("2 8 * q\n")
        sys.stdin = stdin
        self.cal.loop()

        self.assertEqual(self.cal.stack, [16])

    def test_add_config(self):
        """Test add_config method"""
        self.cal.add_config("test/custom_config.yml")
        self.assertEqual(self.stdout.getvalue(),
                         """Wrong command "false = 2 = /" in file "test/custom_config.yml" \n"""
                         """Command must be of the format "{name_of_command = command}"\n\n""")

        self.stdout.truncate(0)
        self.stdout.seek(0)
        self.cal.evaluate("2 double 2 10* wrong")

        self.assertEqual(self.cal.stack, [4, 100])
        self.assertEqual(len(self.cal.custom_commands), 3)
        self.assertEqual(self.stdout.getvalue(),
                         "Unknow command: not_a_command\n")

    def test_add_config_garbage(self):
        """Test add_config with a file with wrong yml syntax"""
        self.cal.add_config("test/config_garbage.yml")

    def test_check_stack(self):
        """Test check_stack method"""
        self.cal.stack.append(55)
        self.assertEqual(self.cal.check_stack(1, "test"), True)
        self.assertEqual(self.cal.check_stack(5, "test"), False)

        self.assertEqual(self.stdout.getvalue(),
                         "Not enough numbers in the stack for test command\n")

    def test_add(self):
        """Test add method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.add()
        self.assertEqual(self.cal.stack.pop(), 15)

    def test_sub(self):
        """Test sub method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.sub()
        self.assertEqual(self.cal.stack.pop(), -5)

        self.cal.stack.append(25.5)
        self.cal.stack.append(10)
        self.cal.sub()
        self.assertEqual(self.cal.stack.pop(), 15.5)

    def test_mul(self):
        """Test mul method"""
        self.cal.stack.append(5)
        self.cal.stack.append(-10)
        self.cal.mul()
        self.assertEqual(self.cal.stack.pop(), -50)

        self.cal.stack.append(0)
        self.cal.stack.append(-10)
        self.cal.mul()
        self.assertEqual(self.cal.stack.pop(), 0)

    def test_div(self):
        """Test div method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.div()
        self.assertEqual(self.cal.stack.pop(), 0.5)

        self.cal.stack.append(-10)
        self.cal.stack.append(5)
        self.cal.div()
        self.assertEqual(self.cal.stack.pop(), -2)

        # If div by 0, the stack remains the same
        self.cal.stack.append(5)
        self.cal.stack.append(0)
        self.cal.div()
        self.assertEqual(self.stdout.getvalue(), "Impossible to divise by 0\n")
        self.assertEqual(len(self.cal.stack), 2)

    def test_int_div(self):
        """Test int_div method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.int_div()
        self.assertEqual(self.cal.stack.pop(), 0)

        self.cal.stack.append(15)
        self.cal.stack.append(10)
        self.cal.int_div()
        self.assertEqual(self.cal.stack.pop(), 1)

        self.cal.stack.append(-15)
        self.cal.stack.append(5)
        self.cal.int_div()
        self.assertEqual(self.cal.stack.pop(), -3)

        # If div by 0, the stack remains the same
        self.cal.stack.append(5)
        self.cal.stack.append(0)
        self.cal.int_div()
        self.assertEqual(self.stdout.getvalue(), "Impossible to divise by 0\n")
        self.assertEqual(len(self.cal.stack), 2)

    def test_modulo(self):
        """Test modulo method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.modulo()
        self.assertEqual(self.cal.stack.pop(), 5)

        self.cal.stack.append(15)
        self.cal.stack.append(10)
        self.cal.modulo()
        self.assertEqual(self.cal.stack.pop(), 5)

        self.cal.stack.append(-15)
        self.cal.stack.append(5)
        self.cal.modulo()
        self.assertEqual(self.cal.stack.pop(), 0)

        # If div by 0, the stack remains the same
        self.cal.stack.append(5)
        self.cal.stack.append(0)
        self.cal.modulo()
        self.assertEqual(self.stdout.getvalue(), "Impossible to divise by 0\n")
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

    def test_sqrt(self):
        """Test sqrt method"""
        self.cal.stack.append(16)
        self.cal.sqrt()
        self.cal.stack.append(0)
        self.cal.sqrt()
        self.cal.stack.append(-5)
        self.cal.sqrt()
        self.assertEqual(self.stdout.getvalue(),
                         "Square root require non-negative value\n")
        self.assertEqual(self.cal.stack, [4, 0.0, -5])

    def test_exp(self):
        """Test exp method"""
        self.cal.stack.append(0)
        self.cal.exp()
        self.assertEqual(self.cal.stack, [1])

    def test_log10(self):
        """Test log10 method"""
        self.cal.stack.append(100)
        self.cal.log10()
        self.assertEqual(self.cal.stack.pop(), 2)

        self.cal.stack.append(-5)
        self.cal.log10()
        self.assertEqual(self.stdout.getvalue(),
                         "Number out of domain for logarithm\n")
        self.assertEqual(self.cal.stack, [-5])

    def test_log2(self):
        """Test log2 method"""
        self.cal.stack.append(256)
        self.cal.log2()
        self.assertEqual(self.cal.stack.pop(), 8)

        self.cal.stack.append(-5)
        self.cal.log2()
        self.assertEqual(self.stdout.getvalue(),
                         "Number out of domain for logarithm\n")
        self.assertEqual(self.cal.stack, [-5])

    def test_loge(self):
        """Test loge method"""
        self.cal.const_e()
        self.cal.loge()
        self.assertEqual(self.cal.stack.pop(), 1)

        self.cal.stack.append(-5)
        self.cal.loge()
        self.assertEqual(self.stdout.getvalue(),
                         "Number out of domain for logarithm\n")
        self.assertEqual(self.cal.stack, [-5])

    def test_and(self):
        """Test _and method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.and_()
        self.assertEqual(self.cal.stack.pop(), 0)

        self.cal.stack.append(7)
        self.cal.stack.append(15)
        self.cal.and_()
        self.assertEqual(self.cal.stack.pop(), 7)

    def test_or(self):
        """Test _or method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.or_()
        self.assertEqual(self.cal.stack.pop(), 15)

        self.cal.stack.append(7)
        self.cal.stack.append(15)
        self.cal.or_()
        self.assertEqual(self.cal.stack.pop(), 15)

    def test_xor(self):
        """Test xor method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.xor()
        self.assertEqual(self.cal.stack.pop(), 15)

        self.cal.stack.append(7)
        self.cal.stack.append(15)
        self.cal.xor()
        self.assertEqual(self.cal.stack.pop(), 8)

    def test_shift_left(self):
        """Test shift_left method"""
        self.cal.stack.append(55)
        self.cal.stack.append(2)
        self.cal.shift_left()
        self.assertEqual(self.cal.stack.pop(), 220)

        self.cal.stack.append(10)
        self.cal.stack.append(5.2)
        self.cal.shift_left()
        self.assertEqual(self.stdout.getvalue(),
                         "This operation requires 2 int\n")
        self.assertEqual(self.cal.stack, [10, 5.2])

    def test_shift_right(self):
        """Test shift_right method"""
        self.cal.stack.append(55)
        self.cal.stack.append(2)
        self.cal.shift_right()
        self.assertEqual(self.cal.stack.pop(), 13)

        self.cal.stack.append(2)
        self.cal.stack.append(5)
        self.cal.shift_right()
        self.assertEqual(self.cal.stack.pop(), 0)

        self.cal.stack.append(10)
        self.cal.stack.append(5.2)
        self.cal.shift_right()
        self.assertEqual(self.stdout.getvalue(),
                         "This operation requires 2 int\n")
        self.assertEqual(self.cal.stack, [10, 5.2])

    def test_absolute_value(self):
        """Test absolute_value method"""
        self.cal.stack.append(5)
        self.cal.absolute_value()
        self.assertEqual(self.cal.stack.pop(), 5)

        self.cal.stack.append(-12.3)
        self.cal.absolute_value()
        self.assertEqual(self.cal.stack.pop(), 12.3)

    def test_inv(self):
        """Test inv method"""
        self.cal.stack.append(4)
        self.cal.inv()
        self.assertEqual(self.cal.stack.pop(), 0.25)

        self.cal.stack.append(-0.1)
        self.cal.inv()
        self.assertEqual(self.cal.stack.pop(), -10)

    def test_neg(self):
        """Test neg method"""
        self.cal.stack.append(4)
        self.cal.neg()
        self.assertEqual(self.cal.stack.pop(), -4)

        self.cal.stack.append(-10.1)
        self.cal.neg()
        self.assertEqual(self.cal.stack.pop(), 10.1)

    def test_sin(self):
        """Test sin method"""
        self.cal.stack.append(0)
        self.cal.sin()
        self.assertEqual(self.cal.stack.pop(), 0.0)

        self.cal.stack.append(math.pi / 2)
        self.cal.sin()
        self.assertEqual(self.cal.stack.pop(), 1.0)

    def test_cos(self):
        """Test cos method"""
        self.cal.stack.append(0)
        self.cal.cos()
        self.assertEqual(self.cal.stack.pop(), 1.0)

        self.cal.stack.append(math.pi / 2)
        self.cal.cos()
        self.assertAlmostEqual(self.cal.stack.pop(), 0.0)

    def test_tan(self):
        """Test tan method"""
        self.cal.stack.append(0)
        self.cal.tan()
        self.assertEqual(self.cal.stack.pop(), 0.0)

        self.cal.stack.append(math.pi / 4)
        self.cal.tan()
        self.assertAlmostEqual(self.cal.stack.pop(), 1.0)

    def test_asin(self):
        """Test asin method"""
        self.cal.stack.append(0)
        self.cal.asin()
        self.assertEqual(self.cal.stack.pop(), 0.0)

        self.cal.stack.append(1)
        self.cal.asin()
        self.assertAlmostEqual(self.cal.stack.pop(), math.pi / 2)

        self.cal.stack.append(-2)
        self.cal.asin()
        self.assertAlmostEqual(self.cal.stack.pop(), -2)
        self.assertEqual(self.stdout.getvalue(),
                         "Number out of domain for asin\n")

    def test_acos(self):
        """Test acos method"""
        self.cal.stack.append(1)
        self.cal.acos()
        self.assertEqual(self.cal.stack.pop(), 0.0)

        self.cal.stack.append(0.0)
        self.cal.acos()
        self.assertAlmostEqual(self.cal.stack.pop(), math.pi / 2)

        self.cal.stack.append(-2)
        self.cal.acos()
        self.assertAlmostEqual(self.cal.stack.pop(), -2)
        self.assertEqual(self.stdout.getvalue(),
                         "Number out of domain for acos\n")

    def test_atan(self):
        """Test atan method"""
        self.cal.stack.append(1)
        self.cal.atan()
        self.assertAlmostEqual(self.cal.stack.pop(), math.pi/4)

        self.cal.stack.append(-1)
        self.cal.atan()
        self.assertAlmostEqual(self.cal.stack.pop(), - math.pi/4)

    def test_toreg(self):
        """Test to_radian method"""
        self.cal.stack.append(180)
        self.cal.to_radian()

        self.cal.stack.append(-90)
        self.cal.to_radian()

        self.cal.stack.append(45)
        self.cal.to_radian()

        self.assertListEqual(self.cal.stack, [math.pi, -math.pi/2, math.pi/4])

    def test_todeg(self):
        """Test to_degree method"""
        self.cal.stack.append(math.pi)
        self.cal.to_degree()

        self.cal.stack.append(-math.pi/2)
        self.cal.to_degree()

        self.cal.stack.append(math.pi/4)
        self.cal.to_degree()

        self.assertListEqual(self.cal.stack, [180, -90, 45])

    def test_switch(self):
        """Test switch method"""
        self.cal.stack.append(-25)
        self.cal.stack.append(32.2)
        self.cal.switch()
        self.assertEqual(self.cal.stack, [32.2, -25])

    def test_copy(self):
        """Test copy method"""
        self.cal.copy()
        self.assertEqual(self.cal.stack, [])

        self.cal.stack.append(10)
        self.cal.copy()
        self.assertEqual(self.cal.stack, [10, 10])

    def test_del(self):
        """Test _del method"""
        self.cal.const_pi()
        self.cal.const_tau()
        self.cal.del_()
        self.assertEqual(self.cal.stack, [math.pi])

    def test_sum(self):
        """Test sum method"""
        self.cal.stack.extend([5, 22, 33])
        self.cal.sum()
        self.assertEqual(self.cal.stack, [5+22+33])

    def test_fact(self):
        """Test fact method"""
        self.cal.factorial()
        self.assertEqual(self.stdout.getvalue(),
                         "Not enough numbers in the stack for fact command\n")

        self.cal.stack.append(5)
        self.cal.factorial()
        self.assertEqual(self.cal.stack.pop(), 120)

        self.stdout.truncate(0)
        self.stdout.seek(0)
        self.cal.stack.append(-5)
        self.cal.factorial()
        self.assertEqual(self.stdout.getvalue(),
                         "Impossible to compute factorial for negative number\n")
        self.assertEqual(self.cal.stack.pop(), -5)

        self.stdout.truncate(0)
        self.stdout.seek(0)
        self.cal.stack.append(3.2)
        self.cal.factorial()
        self.assertEqual(self.stdout.getvalue(),
                         "Impossible to compute factorial for float number\n")
        self.assertEqual(self.cal.stack.pop(), 3.2)

    def test_round(self):
        """Test round method"""
        self.cal.round()
        self.assertEqual(self.stdout.getvalue(),
                         "Not enough numbers in the stack for round command\n")

        self.cal.stack.append(5)
        self.cal.round()
        self.assertEqual(self.cal.stack.pop(), 5)

        self.cal.stack.append(5.6)
        self.cal.round()
        self.assertEqual(self.cal.stack.pop(), 6)

        self.cal.stack.append(-3566.33)
        self.cal.round()
        self.assertEqual(self.cal.stack.pop(), -3566)

    def test_average(self):
        """Test round method"""
        self.cal.average()
        self.assertEqual(self.stdout.getvalue(),
                         "Not enough numbers in the stack for ave command\n")

        self.cal.stack.append(5)
        self.cal.average()
        self.assertEqual(self.cal.stack.pop(), 5)

        self.cal.stack.extend([5, 5.6])
        self.cal.average()
        self.assertEqual(self.cal.stack.pop(), 5.3)

        self.cal.stack.extend([5.3, -3566.33])
        self.cal.average()
        self.assertAlmostEqual(self.cal.stack.pop(), -1780.515)

    def test_print_dec(self):
        """Test print method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10.2)

        self.cal.print_dec()
        self.cal.print_dec()

        self.assertEqual(self.stdout.getvalue(), "10.2\n5\n")

    def test_print_hex(self):
        """Test print_hex method"""
        self.cal.stack.append(500)
        self.cal.stack.append(10.0)
        self.cal.stack.append(12.2)

        self.cal.print_hex()
        self.cal.print_hex()
        self.cal.print_hex()

        self.assertEqual(self.stdout.getvalue(),
                         "0x1.8666666666666p+3\n0xA\n0x1F4\n")

    def test_print_bin(self):
        """Test print_bin method"""
        self.cal.stack.append(500)
        self.cal.stack.append(10.0)
        self.cal.stack.append(2.5)

        self.cal.print_bin()
        self.cal.stack.pop()
        self.cal.print_bin()
        self.cal.print_bin()

        self.assertEqual(self.stdout.getvalue(),
                         "Impossible to print a float in binary\n0b1010\n0b111110100\n")

    def test_print_oct(self):
        """Test print_oct method"""
        self.cal.stack.append(500)
        self.cal.stack.append(10.0)
        self.cal.stack.append(2.5)

        self.cal.print_oct()
        self.cal.stack.pop()
        self.cal.print_oct()
        self.cal.print_oct()

        self.assertEqual(self.stdout.getvalue(),
                         "Impossible to print a float in octal\n0o12\n0o764\n")

    def test_ratio(self):
        """Test ratio method"""
        self.cal.stack.append(10)
        self.cal.stack.append(-10)
        self.cal.stack.append(10.5)
        self.cal.stack.append(-10.25)
        self.cal.stack.append(0.75)
        self.cal.stack.append(10/6)

        self.cal.ratio()
        self.cal.ratio()
        self.cal.ratio()
        self.cal.ratio()
        self.cal.ratio()
        self.cal.ratio()

        self.assertEqual(self.stdout.getvalue(),
                         "5/3\n3/4\n-41/4\n21/2\n-10/1\n10/1\n")

    def test_print_stack(self):
        """Test print_stack"""
        self.cal.stack.append(500)
        self.cal.stack.append(10.0)
        self.cal.stack.append(123.123)

        self.cal.print_stack()

        self.cal.clear_stack()
        self.cal.print_stack()

        self.assertEqual(self.stdout.getvalue(),
                         "500, 10.0, 123.123\nStack is empty\n")

    def test_evaluate(self):
        """Test evaluate method"""
        self.cal.evaluate("5 10 * dec")
        self.assertEqual(self.stdout.getvalue(), "50\n")


if __name__ == "__main__":
    unittest.main()
