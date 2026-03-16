class Divison:
    def __init__(self, num_one = None, num_two = None):
        self.num_one = num_one
        self.num_two = num_two

    def user_input(self):
        try:
            self.num_one = float(input("Введите первое число: "))
            self.num_two = float(input("Введите второе число: "))
        except ValueError as e:
            print("Введите корректное значение. Должно быть числом")

    def division_nums(self):
        try:
            if self.num_two == 0:
                raise ZeroDivisionError("Деление на ноль невозможно!")
            return self.num_one / self.num_two
        except ZeroDivisionError as e:
            return e
        
    def ask_continue(self):
        while True:
            print("Хотите продолжить? (да/нет)")
            message = input("Ответ: ")

            if message == "да":
                return True
            elif message == "нет":
                return False
            else:
                print("Некорректный ответ")

    def start_cycle(self):
        while True:
            self.user_input()
            result = self.division_nums()
            print(f"Result is {result}")

            if self.ask_continue() == False:
                break

        return "Выполнение программы завершено"


test_one = Divison()
result = test_one.start_cycle()
print(result)