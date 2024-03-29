"""File containing the Calculator object and get_number function"""

import math
from fractions import Fraction
from decimal import Decimal
import yaml


def get_number(num):
    """If possible return a number, else return num as a string"""
    for cast in (int, float):
        try:
            num = cast(num)
            return num
        except ValueError:
            pass
    if num[0] == "0":
        for base in (2, 8, 16):
            try:
                num = int(num, base)
                return num
            except ValueError:
                pass

    return num


class Calculator:
    """Class Calculator"""

    def __init__(self):
        self.stack = []

        self.last = None

        self.loop_flag = True

        self.rounding_value = None

        self.operation = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div,
            "//": self.int_div,
            "%": self.modulo,
            "**": self.pow,
            "sqrt": self.sqrt,
            "exp": self.exp,
            "log10": self.log10,
            "log2": self.log2,
            "ln": self.loge,
            "and": self.and_,
            "or": self.or_,
            "xor": self.xor,
            "<<": self.shift_left,
            ">>": self.shift_right,
            "abs": self.absolute_value,
            "inv": self.inv,
            "neg": self.neg,
            "sin": self.sin,
            "cos": self.cos,
            "tan": self.tan,
            "asin": self.asin,
            "acos": self.acos,
            "atan": self.atan,
            "atan2": self.atan2,
            "sinh": self.sinh,
            "cosh": self.cosh,
            "tanh": self.tanh,
            "asinh": self.asinh,
            "acosh": self.acosh,
            "atanh": self.atanh,
            "torad": self.to_radian,
            "todeg": self.to_degree,
            "switch": self.switch,
            "del": self.del_,
            "copy": self.copy,
            "pi": self.const_pi,
            "tau": self.const_tau,
            "e": self.const_e,
            "sum": self.sum,
            "fact": self.factorial,
            "round": self.round,
            "ave": self.average,
            "dec": self.print_dec,
            "hex": self.print_hex,
            "bin": self.print_bin,
            "oct": self.print_oct,
            "ratio": self.ratio,
            "s": self.print_stack,
            "clear": self.clear_stack,
            "back": self.back,
            "help": self.help,
            "q": self.quit
        }

        self.custom_commands = {}

    def loop(self):
        """loop for getting input from user"""

        print("Reverse polish notation calculator")

        try:
            while self.loop_flag:
                data = input(">")
                self.evaluate(data)

        except (KeyboardInterrupt, EOFError):
            pass

    def evaluate(self, string):
        """Evaluate the string and calls adequate method"""
        for i in string.split():
            i = get_number(i)
            if isinstance(i, int):
                self.stack.append(i)
            elif isinstance(i, float):
                if i.is_integer():
                    self.stack.append(int(i))
                else:
                    self.stack.append(i)

            elif isinstance(i, str):
                if i in self.operation:
                    self.operation[i]()
                elif i in self.custom_commands:
                    self.evaluate(self.custom_commands[i])
                else:
                    print("Unknow command: {}".format(i))

            else:
                raise RuntimeError("Should never happend")

    def add_config(self, existing_path):
        """Add command from existing path
           Command must be on the format "{name_of_command} = {command}" """
        with open(existing_path, "r", encoding="UTF-8") as file:
            try:
                config = yaml.safe_load(file)
            except yaml.scanner.ScannerError as err:
                print("Error in config file : {}", err)
                return

            if self.rounding_value is None and "rounding" in config:
                self.rounding_value = config["rounding"]
            if "shortcut" in config:
                for i in config["shortcut"]:
                    try:
                        name, command = i.split("=")
                    except ValueError:
                        print("""Wrong command "{}" in file "{}" """.format(
                            i, existing_path))
                        print(
                            """Command must be of the format "{name_of_command = command}"\n""")
                    else:
                        name = name.strip()
                        self.custom_commands[name] = command

    def check_stack(self, num, command):
        """Check if enough number are in the stack"""
        if len(self.stack) < num:
            print("Not enough numbers in the stack for {} command".format(command))
            return False

        return True

    def add_stack(self, val):
        """Convert to int if possible and add to stack"""
        if isinstance(val, int):
            self.stack.append(val)
        elif isinstance(val, float):
            if val.is_integer():
                self.stack.append(int(val))
            else:
                self.stack.append(val)
        else:
            raise ValueError("Wrong data type")

    def add(self):
        """Take 2 numbers from the stack, add them and put the result in the stack"""
        if self.check_stack(2, "+"):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.add_stack(value1 + value2)

    def sub(self):
        """Take 2 numbers from the stack, substracte them and put the result in the stack"""
        if self.check_stack(2, "-"):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.add_stack(value2 - value1)

    def mul(self):
        """Take 2 numbers from the stack, mul them and put the result in the stack"""
        if self.check_stack(2, "*"):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.add_stack(value1 * value2)

    def div(self):
        """Take 2 numbers from the stack, divise them and put the result in the stack"""
        if self.check_stack(2, "/"):
            value1 = self.stack.pop()
            if value1 == 0:
                print("Impossible to divise by 0")
                self.stack.append(value1)
            else:
                value2 = self.stack.pop()
                d_res = Decimal(value2) / Decimal(value1)
                if d_res.to_integral_value() == d_res:
                    self.stack.append(int(d_res))
                else:
                    self.stack.append(float(d_res))

    def int_div(self):
        """Take 2 numbers from the stack, divise them and put the integer result in the stack"""
        if self.check_stack(2, "//"):
            value1 = self.stack.pop()
            if value1 == 0:
                print("Impossible to divise by 0")
                self.stack.append(value1)
            else:
                value2 = self.stack.pop()
                self.add_stack(value2 // value1)

    def modulo(self):
        """Take 2 numbers from the stack, divise them and put the remainder in the stack"""
        if self.check_stack(2, "%"):
            value1 = self.stack.pop()
            if value1 == 0:
                print("Impossible to divise by 0")
                self.stack.append(value1)
            else:
                value2 = self.stack.pop()
                self.add_stack(value2 % value1)

    def pow(self):
        """Take 2 numbers from the stack, apply power and put the result in the stack"""
        if self.check_stack(2, "**"):
            if self.stack[-2] == 0 and self.stack[-1] < 0:
                print("Impossible to divise by 0")
            else:
                value1 = self.stack.pop()
                value2 = self.stack.pop()
                self.add_stack(value2 ** value1)

    def sqrt(self):
        """Replace the last number in the stack with the square root of itself"""
        if self.check_stack(1, "sqrt"):
            value = self.stack.pop()
            if value < 0:
                print("Square root require non-negative value")
                self.stack.append(value)
            else:
                self.add_stack(math.sqrt(value))

    def exp(self):
        """Apply e**x to the last number of the stack"""
        if self.check_stack(1, "exp"):
            value = self.stack.pop()
            self.add_stack(math.exp(value))

    def log10(self):
        """Apply log10 to the last number of the stack"""
        if self.check_stack(1, "log10"):
            value = self.stack.pop()
            if value > 0:
                self.add_stack(math.log10(value))
            else:
                print("Number out of domain for logarithm")
                self.stack.append(value)

    def log2(self):
        """Apply log2 to the last number of the stack"""
        if self.check_stack(1, "log2"):
            value = self.stack.pop()
            if value > 0:
                self.add_stack(math.log2(value))
            else:
                print("Number out of domain for logarithm")
                self.stack.append(value)

    def loge(self):
        """Apply natural logarithm to the last number of the stack"""
        if self.check_stack(1, "loge"):
            value = self.stack.pop()
            if value > 0:
                self.add_stack(math.log(value))
            else:
                print("Number out of domain for logarithm")
                self.stack.append(value)

    def and_(self):
        """Take 2 numbers from the stack, apply a bitwise "and" and put the result in the stack"""
        if self.check_stack(2, "and"):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            if isinstance(value1, int) and isinstance(value2, int):
                self.stack.append(value1 & value2)
            else:
                print("This operation requires 2 int")
                self.stack.append(value2)
                self.stack.append(value1)

    def or_(self):
        """Take 2 numbers from the stack, apply a bitwise "or" and put the result in the stack"""
        if self.check_stack(2, "or"):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            if isinstance(value1, int) and isinstance(value2, int):
                self.stack.append(value1 | value2)
            else:
                print("This operation requires 2 int")
                self.stack.append(value2)
                self.stack.append(value1)

    def xor(self):
        """Take 2 numbers from the stack, apply a bitwise "xor" and put the result in the stack"""
        if self.check_stack(2, "xor"):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            if isinstance(value1, int) and isinstance(value2, int):
                self.stack.append(value1 ^ value2)
            else:
                print("This operation requires 2 int")
                self.stack.append(value2)
                self.stack.append(value1)

    def shift_left(self):
        """Take 2 numbers from the stack, apply a left shift and put the result in the stack"""
        if self.check_stack(2, "<<"):
            value2 = self.stack.pop()
            value1 = self.stack.pop()
            if isinstance(value1, int) and isinstance(value2, int):
                self.stack.append(value1 << value2)
            else:
                print("This operation requires 2 int")
                self.stack.append(value1)
                self.stack.append(value2)

    def shift_right(self):
        """Take 2 numbers from the stack, apply a right shift and put the result in the stack"""
        if self.check_stack(2, ">>"):
            value2 = self.stack.pop()
            value1 = self.stack.pop()
            if isinstance(value1, int) and isinstance(value2, int):
                self.stack.append(value1 >> value2)
            else:
                print("This operation requires 2 int")
                self.stack.append(value1)
                self.stack.append(value2)

    def absolute_value(self):
        """Make absolute the last value of the stack"""
        if self.check_stack(1, "abs"):
            self.stack.append(abs(self.stack.pop()))

    def inv(self):
        """Inverse the last number of the stack"""
        if self.check_stack(1, "inv"):
            value = self.stack.pop()
            self.add_stack(1 / value)

    def neg(self):
        """Change the sign of the last number in the stack"""
        if self.check_stack(1, "neg"):
            value = self.stack.pop()
            if value < 0:
                self.stack.append(abs(value))
            else:
                self.stack.append(0 - value)

    def sin(self):
        """Replace the last number in the stack with the sine of itself (measured in radians)"""
        if self.check_stack(1, "sin"):
            self.add_stack(math.sin(self.stack.pop()))

    def cos(self):
        """Replace the last number in the stack with the cosine of itself (measured in radians)"""
        if self.check_stack(1, "cos"):
            self.add_stack(math.cos(self.stack.pop()))

    def tan(self):
        """Replace the last number in the stack with the tangent of itself (measured in radians)"""
        if self.check_stack(1, "tan"):
            self.add_stack(math.tan(self.stack.pop()))

    def asin(self):
        """Replace the last number in the stack with the arc sine of itself (measured in radians)"""
        if self.check_stack(1, "asin"):
            value = self.stack.pop()
            if value < -1 or value > 1:
                print("Number out of domain for asin")
                self.stack.append(value)
            else:
                self.add_stack(math.asin(value))

    def acos(self):
        """Replace the last number in the stack with the arc cosine of itself
        (measured in radians)"""
        if self.check_stack(1, "acos"):
            value = self.stack.pop()
            if value < -1 or value > 1:
                print("Number out of domain for acos")
                self.stack.append(value)
            else:
                self.add_stack(math.acos(value))

    def atan(self):
        """Replace the last number in the stack with the arc tangent of itself
        (measured in radians)"""
        if self.check_stack(1, "atan"):
            value = self.stack.pop()
            self.add_stack(math.atan(value))

    def atan2(self):
        """Take 2 numbers from the stack, apply a atan2 function and put the result in the stack"""
        if self.check_stack(2, "atan2"):
            x_val = self.stack.pop()
            y_val = self.stack.pop()
            self.add_stack(math.atan2(y_val, x_val))

    def sinh(self):
        """Replace the last number in the stack with the hyperbolic sine of itself"""
        if self.check_stack(1, "sinh"):
            value = self.stack.pop()
            self.add_stack(math.sinh(value))

    def cosh(self):
        """Replace the last number in the stack with the hyperbolic cosine of itself"""
        if self.check_stack(1, "cosh"):
            value = self.stack.pop()
            self.add_stack(math.cosh(value))

    def tanh(self):
        """Replace the last number in the stack with the hyperbolic tangent of itself"""
        if self.check_stack(1, "tanh"):
            value = self.stack.pop()
            self.add_stack(math.tanh(value))

    def asinh(self):
        """Replace the last number in the stack with the asinh of itself"""
        if self.check_stack(1, "asinh"):
            value = self.stack.pop()
            self.add_stack(math.asinh(value))

    def acosh(self):
        """Replace the last number in the stack with the acosh of itself"""
        if self.check_stack(1, "acosh"):
            value = self.stack.pop()
            self.add_stack(math.acosh(value))

    def atanh(self):
        """Replace the last number in the stack with the atanh of itself"""
        if self.check_stack(1, "atanh"):
            value = self.stack.pop()
            self.add_stack(math.atanh(value))

    def to_radian(self):
        """Convert the last number from degree to radian"""
        if self.check_stack(1, "torad"):
            value = self.stack.pop()
            self.add_stack(value / 180 * math.pi)

    def to_degree(self):
        """Convert the last number from radian to degree"""
        if self.check_stack(1, "todeg"):
            value = self.stack.pop()
            self.add_stack(value * 180 / math.pi)

    def switch(self):
        """Switch the last 2 numbers of the stack"""
        if self.check_stack(2, "switch"):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1)
            self.stack.append(value2)

    def del_(self):
        """Delete the last number in the stack"""
        if self.check_stack(1, "del"):
            self.stack.pop()

    def copy(self):
        """Copy the last number of the stack and add it to the stack"""
        if self.check_stack(1, "copy"):
            self.stack.append(self.stack[-1])

    def const_pi(self):
        """Add pi to the stack"""
        self.stack.append(math.pi)

    def const_tau(self):
        """Add tau to the stack"""
        self.stack.append(math.tau)

    def const_e(self):
        """Add e to the stack"""
        self.stack.append(math.e)

    def sum(self):
        """Take all the number of the stack and add the sum"""
        if self.check_stack(1, "sum"):
            total = sum(self.stack)
            self.stack.clear()
            self.add_stack(total)

    def factorial(self):
        """Replace the last number in the stack with its factorial"""
        if self.check_stack(1, "fact"):
            value = self.stack.pop()
            if value < 0:
                print("Impossible to compute factorial for negative number")
                self.stack.append(value)
            elif isinstance(value, float):
                print("Impossible to compute factorial for float number")
                self.stack.append(value)
            else:
                self.stack.append(math.factorial(value))

    def round(self):
        """Round the last number in the stack"""
        if self.check_stack(1, "round"):
            value = self.stack.pop()
            self.stack.append(round(value, self.rounding_value))

    def average(self):
        """Take all the number of the stack and add the average"""
        if self.check_stack(1, "ave"):
            size = len(self.stack)
            total = sum(self.stack)
            self.stack.clear()

            self.add_stack(total / size)

    def print_dec(self):
        """Print the last number of the stack and remove it"""
        if self.check_stack(1, "dec"):
            val = self.stack.pop()
            self.last = val
            print("{}".format(val))

    def print_hex(self):
        """Print in hexadecimal format the last number of the stack and remove it"""
        if self.check_stack(1, "hex"):
            i = self.stack.pop()
            self.last = i
            if isinstance(i, int):
                print("0x{:X}".format(i))
            else:
                print(float.hex(i))

    def print_bin(self):
        """Print in binary format the last number of the stack and remove it"""
        if self.check_stack(1, "bin"):
            i = self.stack.pop()
            if isinstance(i, int):
                print("0b{:b}".format(i))
                self.last = i
            else:
                self.stack.append(i)
                print("Impossible to print a float in binary")

    def print_oct(self):
        """Print in octal format the last number of the stack and remove it"""
        if self.check_stack(1, "oct"):
            i = self.stack.pop()
            if isinstance(i, int):
                print("0o{:o}".format(i))
                self.last = i
            else:
                self.stack.append(i)
                print("Impossible to print a float in octal")

    def ratio(self):
        """Print in integer ratio format the last number of the stack and remove it"""
        if self.check_stack(1, "ratio"):
            value = self.stack.pop()
            self.last = value
            if isinstance(value, float):
                print(Fraction(value).limit_denominator())
            else:
                print("{}/1".format(value))

    def print_stack(self):
        """Print the stack"""
        if len(self.stack) > 0:
            for i in range(len(self.stack) - 1):
                print("{}, ".format(self.stack[i]), end="")
            print("{}".format(self.stack[-1]))
        else:
            print("Stack is empty")

    def clear_stack(self):
        """Empty the stack"""
        self.stack = []
        self.last = None

    def back(self):
        """Put back on the stack the last value that was printed"""
        if self.last is not None:
            self.stack.append(self.last)
            self.last = None
        else:
            print("No value was remove from the stack")

    def help(self):
        """Print help; Same as pol --list"""
        doc = ""
        for command, method in self.operation.items():
            doc += "`{}` : {}\n".format(command, method.__doc__)

        print(doc)

    def quit(self):
        """Quit the program"""
        self.loop_flag = False
