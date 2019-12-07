"""Calculator using the reverse polish notation"""


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
            ".": self.print,
            "q": self.quit
        }

    def main(self):
        """Fonction principale"""

        print("Reverse polish notation calculator")

        try:
            while self.loop:
                data = input(">")

                for i in data.split():
                    for cast in (int, float):
                        try:
                            i = cast(i)
                            self.stack.append(i)
                            break
                        except ValueError:
                            pass

                    if isinstance(i, str):
                        if i in self.operation.keys():
                            self.operation[i]()
                        else:
                            print("Unknow command: {}".format(i))

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

    def print(self):
        """Take one number from the stack and print it"""
        if self.check_stack(1):
            print("{}".format(self.stack.pop()))

    def print_stack(self):
        """Print the stack"""
        if len(self.stack) > 0:
        for i in range(len(self.stack) - 1):
            print("{}, ".format(self.stack[i]), end="")
        print("{}".format(self.stack[-1]))

    def quit(self):
        """Quit the program"""
        self.loop = False


if __name__ == "__main__":
    CAL = Calculator()
    CAL.main()
