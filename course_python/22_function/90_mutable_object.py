def increase_person_age(person):
    person["age"] += 1
    return person

person_one = {
    "name": "Pavel",
    "age": 26
}

print(increase_person_age(person_one))