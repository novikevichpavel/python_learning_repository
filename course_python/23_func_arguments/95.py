#  Функция может принимать неограниченое кол-во аргументов, если они объеденены в кортеж

def sum_nums(*args): # При объявлении такого аргумента, все параметры которые будет переданы в функции объединяться в кортеж
    return sum(args)

print(sum_nums(3, 3, 3, 3))


# Позиционные аргументы 
def get_posts_info(name, posts_qty):
    info = f"User {name} has {posts_qty} posts"
    return info

print(get_posts_info("Pavel", 25))