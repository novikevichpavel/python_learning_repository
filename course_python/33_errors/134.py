# 1

try:
    print(10 / 2)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else: # Выполняется в случае, если ошибок не возникло
    print("Succes")
finally: # Выполняется в любом случае. К примеру в этом блоке происходит отключение соединения с БД
    ("Continue...")


# 2 Вариант с автоматическим подбором ошибки

try:
    print(10 / 0)
except Exception as e:
    print(e)



