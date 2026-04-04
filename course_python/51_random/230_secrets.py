# Для генерации паролей используется модуль secrets

import secrets, string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

all_chars = string.ascii_letters + string.digits + string.punctuation

print("".join(secrets.choice(all_chars) for i in range(9)))