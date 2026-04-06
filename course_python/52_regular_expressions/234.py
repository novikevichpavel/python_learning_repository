import re

class EmailValidator:

    EMAIL_PATTERN = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"

    def __init__(self):
        self.email_pattern = re.compile(self.EMAIL_PATTERN)
        self.email = None

    def get_email(self):
        self.email = input("Enter an email: ")
        return self.email

    def validation_email(self):
        if not self.email_pattern.fullmatch(self.email):
            return False 
        return bool(self.email_pattern.fullmatch(self.email))
    
    def __str__(self):
        if self.validation_email():
            return f"Your email {self.email} is valid"
        return f"Your email is not valid"
    

user_input = EmailValidator()
user_input.get_email()
user_input.validation_email()
print(user_input)
