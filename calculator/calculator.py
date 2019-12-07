"""Calculator using the reverse polish notation"""


def get_number(num):
    """if possible return a number, else return num as a string"""
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

        self.loop = True

        self.operation = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div,
            "**": self.pow,
            "and": self._and,
            ".": self.print,
            "..": self.print_hex,
            "b": self.print_bin,
            "s": self.print_stack,
            "clear": self.clear_stack,
            "q": self.quit
        }

    def main(self):
        """Fonction principale"""

        print("Reverse polish notation calculator")

        try:
            while self.loop:
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
            value2 = self.stack.pop()
            self.stack.append(value2 / value1)

    def pow(self):
        """Take 2 number from the stack, divise them and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value2 ** value1)

    def _and(self):
        """Take 2 number from the stack, divise them and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1 & value2)

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
            else:
                print(float.hex(i))

    def print_bin(self):
        """Take one number from the stack and print it in binary format"""
        if self.check_stack(1):
            i = self.stack.pop()
            if isinstance(i, int):
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

    def clear_stack(self):
        """Empty the stack"""
        self.stack = []

    def quit(self):
        """Quit the program"""
        self.loop = False


if __name__ == "__main__":
    CAL = Calculator()
    CAL.main()
