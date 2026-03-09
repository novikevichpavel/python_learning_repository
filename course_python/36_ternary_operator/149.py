# Тернарный оператор заменяет условнное выржаени if-else(условное выражение). У тернарного оператора 3 опренда: выражние 1 if условие else выражение 2

num = int(input("Enter a value: "))
print("Your num is even" if num % 2 == 0 else "your num is odd")


my_img = ("1920", "1080")

print(f"The size of image is {my_img[0]}x{my_img[1]}") if len(my_img) == 2 and type(my_img[0]) is str and type(my_img[1]) is str else print("Uncorrect format")

