# Модуль array используется для сохранения однотипных данных

from array import array

my_int_array = array("i", [4, 5, 11, 15])

with open("my_array.bin", "wb") as my_array:
    my_int_array.tofile(my_array)

imported_array = array("i")

with open("my_array.bin", "rb") as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)