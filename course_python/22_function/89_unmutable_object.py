# Передача неизменяемых объектов в фукнцию

def my(a, b):
    c = a + b
    return c

num_one = 5
num_two = 5

res = my(num_one, num_two)
print(res)