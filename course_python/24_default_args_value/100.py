# Значение параметров функции по умолчанию устанавливаются для того случая,что если какой-то из аргументов не будет передан на прямую - ему все равно будет присвоно дефолтно установленое значение

def mult_by_factor(value, multiplier=2):
    return value * multiplier

print(mult_by_factor(2, 5))
print(mult_by_factor(2))

# Значением по умолчнаю для параметра может быть и вызов функции

from datetime import date

def get_weekday():
    return date.today().strftime("%A")


def create_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy["created_on_weekday"] = weekday
    return post_copy


initial_post = {
    "id": 234,
    "author": "Pavel"
}


print(create_post(initial_post))

