my_set = {"1920x1080", "800x600"}

my_set.add("1024x768") # Добавление жлемента в набор

new_set = {"111x111", "222x222", "1920x1080"}

union_set = new_set.union(my_set) # Объединение наборов

intersection_set = my_set.intersection(new_set) # Находит пересение двух наборов
diff_set = my_set.difference(new_set) # Покажет все значения, по которым наборы различаются

# Метод .discard("element") удаляет элемент из набора / .remove()
# Метод .copy() копирует набор




set_one = {1, 2, 4}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two)) # Проверяет входит ли один из наборов в другой