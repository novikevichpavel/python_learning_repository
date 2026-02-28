# Задача 1

# 1. Переписать вызов функции merge_list_to_dict так, чтобы в ней использовались аргументы с ключевыми словами
# 2. Добавить еще один вызов функции, в котором бдует один позиционный аргумент, а второй - аргумент с ключевым словом.


# Задача 2

# 1. Создать функцию updtae_car_info, в которой все именованые аргументы будут объединятьсяв словарь car
# 2. Добавить в словарь новый ключ is_available со значением True
# 3. Вернуть из функции измененный словарь
# 4. Вызвать функцию с именованными аргументами brand и price, их значения могут быть любыми
# 5. Вывести результат в терминал


# 1

list_one = [1, 2, 3]
list_two = [4, 5, 6]


def merge_list_to_dict(list_one, list_two):
    merged_list = zip(list_one, list_two)
    return dict(merged_list)


print(merge_list_to_dict(list_one=list_one, list_two=list_two))

print(merge_list_to_dict(list_one, list_two=list_two))


# 2

def update_car_info(**car):
    car["is_available"] = True
    return car

print(update_car_info(brand="BMW", price=25000))