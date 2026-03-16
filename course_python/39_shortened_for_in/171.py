from sys import getsizeof

squares_gen = (i * i for i in range(10))
print(getsizeof(squares_gen))
print(type(squares_gen))

squares_list = [i * i for i in range(10)]
print(getsizeof(squares_list))
print(type(squares_list))