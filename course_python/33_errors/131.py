class Calculator:
    def __init__(self, num_one=None, num_two=None):
        self.num_one = num_one
        self.num_two = num_two

    def get_num_one(self):
        while True:
            try:
                self.num_one = float(input("Enter num: "))
                break
            except ValueError:
                print("Must be int")

    def get_num_two(self):
        while True:
            try:
                self.num_two = float(input("Enter num: "))
                break
            except ValueError:
                print("Must be int")

    def get_operator(self):
        operators_list = ["+", "-", "*", "/"]
        while True:
            oper = input("Enter operator: ")
            if oper in operators_list:
                return oper
            print("Error. Unknown operator")

    def do_math(self):
        oper = self.get_operator()

        if oper == "+":
            return self.num_one + self.num_two
        elif oper == "-":
            return self.num_one - self.num_two
        elif oper == "*":
            return self.num_one * self.num_two
        elif oper == "/":
            if self.num_two == 0:
                return "Error: divison by Zero"
            return self.num_one / self.num_two

result = Calculator()
result.get_num_one()
result.get_num_two()
print(result.do_math())


