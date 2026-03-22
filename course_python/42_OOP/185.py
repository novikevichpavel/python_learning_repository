class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Post:
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user
    
    def create_post(self, title, text, author):
        post = Post(title, text, author)
        self.posts.append(post)
        return post
    
    def find_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user
            
    def find_post_by_username(self, user):
        found_posts = []
        for post in self.posts:
            if post.author == user:
                found_posts.append(post)

        return found_posts
    

forum = Forum()

first_user = forum.register_user("Pavel", "pavel@gnail.com")
first_post = forum.create_post("First post", "Posts text about his life", first_user)

print(forum.posts[0].title, forum.posts[0].text)

find_user = forum.find_post_by_username(first_user)

print(first_user.name)


    