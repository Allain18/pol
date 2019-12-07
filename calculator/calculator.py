"""Calculator using the reverse polish notation"""


class Calculator:
    """Class Calculator"""

    def __init__(self):
        self.stack = []

        self.loop = True

        self.operation = {
            "+": self.plus,
            ".": self.print
        }

    def main(self):
        """Fonction principale"""

        print("Reverse polish notation calculator")

        try:
            while self.loop:
                data = input(">")

                for i in data.split():
                    try:
                        i = int(i)
                        self.stack.append(i)
                    except ValueError:
                        self.operation[i]()

        except KeyboardInterrupt:
            pass

    def check_stack(self, num):
        """Check if enough number are in the stack"""
        if len(self.stack) < num:
            return False

        return True

    def plus(self):
        """Take 2 number from the stack, add them and put the result in the stack"""
        if self.check_stack(2):
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append(value1 + value2)

    def print(self):
        """Take one number from the stack and print it"""
        if self.check_stack(1):
            print("{}".format(self.stack.pop()))


if __name__ == "__main__":
    CAL = Calculator()
    CAL.main()
