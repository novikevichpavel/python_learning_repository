# Присвоение значение из списка переменным

# 1

my_fruits = ["apple", "banana", "lime"]

my_apple = my_fruits[0]
my_banana = my_fruits[1]
my_lime = my_fruits[2]

print(my_apple, my_banana, my_lime)


# 2

my_apple_two, my_banana_two, my_lime_two = my_fruits

print(my_apple_two)
print(my_banana_two)
print(my_lime_two)


# 3

my_apple_third, *remaining_fruits = my_fruits
# присваивает переменной my_apple_third значение первого элемента списка, и создает новый список remaining_fruits присваивая ему оставшиеся элементы списка my_fruits

print(my_apple_third)
print(remaining_fruits)