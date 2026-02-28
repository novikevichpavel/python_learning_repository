# 1. Создать функцию merge_list_to_dict
# 2. Функция должна имет два параметра
# 3. Функция должна обединять два списка, используя встроенную функцию zip
# 4. Конвертировать объект zip в словарь и вернуть его из функции 
# 5. Вызвать функцию, передав ей два списка в качестве аргументов
# 6. Вывести результат вызова в терминал

list_one = [1, 2, 3, 4]
list_two = [5, 6, 7, 8]

def merge_list_to_dict(list_one, list_two):
    union_lists = zip(list_one, list_two)
    return dict(union_lists)

print(merge_list_to_dict(list_one, list_two))