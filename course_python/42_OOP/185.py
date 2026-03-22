class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Post:
    def __init__(self, title: str, text: str, author: User):
        self.title = title
        self.text = text
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, name: str, email: str):
        user = User(name, email)
        self.users.append(user)
        return user
    
    def create_post(self, title: str, text: str, author: User):
        post = Post(title, text, author)
        self.posts.append(post)
        return post
    
    def find_user_by_name(self, name: str):
        for user in self.users:
            if user.name == name:
                return user
            
    def find_post_by_username(self, user: User):
        found_posts = []
        for post in self.posts:
            if post.author == user:
                found_posts.append(post)

        return found_posts
    
    def find_user_text_by_email(self, email: User):
        user_texts = []
        for post in self.posts:
            if post.author == email:
                user_texts.append(post.text)
        
        return user_texts
    

forum = Forum()

first_user = forum.register_user("Pavel", "pavel@gnail.com")
first_post = forum.create_post("First post", "Posts text about his life", first_user)

print(forum.posts[0].title, forum.posts[0].text)

find_user = forum.find_post_by_username(first_user)

found_text = forum.find_user_text_by_email(first_user)
print(found_text)

print(first_user.name)


    