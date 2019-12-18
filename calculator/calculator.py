"""Calculator using the reverse polish notation"""

import math


def get_number(num):
    """If possible return a number, else return num as a string"""
    for cast in (int, float):
        try:
            num = cast(num)
            return num
        except ValueError:
            pass

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

        self.loop_flag = True

        self.operation = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div,
            "**": self.pow,
            "and": self._and,
            "or": self._or,
            "xor": self.xor,
            "abs": self.absolute_value,
            "inv": self.inv,
            "switch": self.switch,
            "copy": self.copy,
            "pi": self.const_pi,
            "tau": self.const_tau,
            ".": self.print,
            "..": self.print_hex,
            "bin": self.print_bin,
            "s": self.print_stack,
            "clear": self.clear_stack,
            "q": self.quit
        }

    def loop(self):
        """Fonction principale"""

        print("Reverse polish notation calculator")

        try:
            while self.loop_flag:
                data = input(">")

                for i in data.split():
                    i = get_number(i)
                    if isinstance(i, (int, float)):
                        self.stack.append(i)

                    elif isinstance(i, str):
                        if i in self.operation.keys():
                            self.operation[i]()
                        else:
                            print("Unknow command: {}".format(i))

                    else:
                        raise "Should never happend"

        except KeyboardInterrupt:
            pass

    def check_stack(self, num):
        """Check if enough number are in the stack"""
        if len(self.stack) < num:
            print("Not enough number in the stack")
            return False

        return True

    def add(self):
        """Take 2 number from the stack, add them and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1 + value2)

    def sub(self):
        """Take 2 number from the stack, substracte them and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value2 - value1)

    def mul(self):
        """Take 2 number from the stack, mul them and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1 * value2)

    def div(self):
        """Take 2 number from the stack, divise them and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            if value1 == 0:
                print("Impossible to divise by 0")
                self.stack.append(value1)
                return
            value2 = self.stack.pop()
            self.stack.append(value2 / value1)

    def pow(self):
        """Take 2 number from the stack, apply power and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value2 ** value1)

    def _and(self):
        """Take 2 number from the stack, apply a bitwise "and" and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1 & value2)

    def _or(self):
        """Take 2 number from the stack, apply a bitwise "or" and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1 | value2)

    def xor(self):
        """Take 2 number from the stack, apply a bitwise "xor" and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1 ^ value2)

    def absolute_value(self):
        """Make absolute the last value of the stack"""
        if self.check_stack(1):
            self.stack.append(abs(self.stack.pop()))

    def inv(self):
        """Inverse the last number of the stack"""
        if self.check_stack(1):
            value = self.stack.pop()
            self.stack.append(1 / value)

    def switch(self):
        """Switch the last 2 numbers of the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1)
            self.stack.append(value2)

    def copy(self):
        """Copy the last number of the stack and add it to the stack"""
        if self.check_stack(1):
            self.stack.append(self.stack[-1])

    def const_pi(self):
        """Add pi to the stack"""
        self.stack.append(math.pi)

    def const_tau(self):
        """Add tau to the stack"""
        self.stack.append(math.tau)

    def print(self):
        """Take one number from the stack and print it"""
        if self.check_stack(1):
            print("{}".format(self.stack.pop()))

    def print_hex(self):
        """Take one number from the stack and print it in hex format"""
        if self.check_stack(1):
            i = self.stack.pop()
            if isinstance(i, int):
                print("0x{:X}".format(i))
            elif i.is_integer():
                i = int(i)
                print("0x{:X}".format(i))
            else:
                print(float.hex(i))

    def print_bin(self):
        """Take one number from the stack and print it in binary format"""
        if self.check_stack(1):
            i = self.stack.pop()
            if isinstance(i, int):
                print("0b{:b}".format(i))
            elif i.is_integer():
                i = int(i)
                print("0b{:b}".format(i))
            else:
                self.stack.append(i)
                print("Not possible to print a float in binary")

    def print_stack(self):
        """Print the stack"""
        if len(self.stack) > 0:
            for i in range(len(self.stack) - 1):
                print("{}, ".format(self.stack[i]), end="")
            print("{}".format(self.stack[-1]))
        else:
            print()

    def clear_stack(self):
        """Empty the stack"""
        self.stack = []

    def quit(self):
        """Quit the program"""
        self.loop_flag = False


def main():
    """Entry point of the program"""
    cal = Calculator()
    cal.loop()


if __name__ == "__main__":
    main()
