import random

new_list = [
    1,
    "Oksana",
    "Pasha",
    True,
    False,
    "Poina",
    "Olga",
    "Ivan"
]

print(random.random())
print(random.randint(1, 10))
print(random.choice(new_list))
print(random.choices(new_list, k=2))
print(random.shuffle(new_list))
print(new_list)


print("".join(random.choices("0123456789", k=6)))