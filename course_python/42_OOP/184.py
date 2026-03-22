class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class AdminUser(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
        self.is_admin = True

my_admin = AdminUser("Pavel", "novikevichp@eurotorg.by", "Admin")
print(my_admin)