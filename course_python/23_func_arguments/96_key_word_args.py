# Аргументы с ключевыми словами позволяют передавать не в прямой последовательности
def get_posts_info(name, posts_qty):
    info = f"User {name} has {posts_qty} posts"
    return info

print(get_posts_info(posts_qty=25, name="Pavel"))