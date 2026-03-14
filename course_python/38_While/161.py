# цикл While

import random

random_num = random.randint(1, 10)

while True:
    user_input = int(input("Guess num form 1 to 10: "))
    if user_input != random_num:
        print("Try again")
        continue
    print(f"You won. The num is {random_num}")
    break