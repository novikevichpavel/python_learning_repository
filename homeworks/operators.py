# 1. Создать две переменные и присвоить им им одинаковые последовательности типа set. При этом не копировать одну в другую
# 2. Вывести в терминал результат сравнения двух созданных объектов
# 3. Сравнить два объекта оператором is
# 4. Проверить, есть ли в наборе опредленные элементы используя, оператор in

set_one = {"abc", 123, True}
set_two = set_one.copy()

print(set_one == set_two)

print(set_one is set_two)

print("abc" in set_one)

print("abc" in set_two)

print("def" in set_one)

print("def" not in set_one)