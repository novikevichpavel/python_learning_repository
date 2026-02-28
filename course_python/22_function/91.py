# Чтобы избежать измнения внешнего объекта внутри функции - можно создавать копию объекта

def increse_person_age(person):
    copy_person = person.copy()
    copy_person["age"] += 1
    return copy_person

person = {
    "name": "Pavel",
    "age": 26
}

copy_person = increse_person_age(person)
print(copy_person)
print(person)

print(increse_person_age(person))
print(person)