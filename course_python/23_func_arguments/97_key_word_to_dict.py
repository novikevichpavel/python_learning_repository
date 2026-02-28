# Объединение аргументов в словарь

def get_posts_info(**person):
    info = f"{person["name"]} wrote {person["posts_qty"]} posts"
    return info

print(get_posts_info(name="Pavel", posts_qty=25))


# Резюме. В пайтон можно передавать, как позиционные аргументы, так и именованые аргументы. Позицонные можно объединять в кортежи, именованные в словарь