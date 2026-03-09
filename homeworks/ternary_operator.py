# Перерписать пример используя классическую условную конструкцию. А так проверить длину строки, если строка длинее 79 символов, необходимо выводить - string is long, в противном случае выводить - string is short
# print(f"The size of image is {my_img[0]}x{my_img[1]}") if len(my_img) == 2 and type(my_img[0]) is str and type(my_img[1]) is str else print("Uncorrect format")


my_img = ("1920", "1080", "1920", "1080", "1920", "1080", "1920", "1080", "1920", "1080")

if len(my_img) == 2 and type(my_img[0]) is str and type(my_img[1]) is str:
    print(f"{my_img[0]}x{my_img[1]}")

if len(my_img[0] + my_img[1]) > 79:
    print("String is long")
else:
    print("String is short")