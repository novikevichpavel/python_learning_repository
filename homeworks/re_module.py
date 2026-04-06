import re 

class PasswordValidator:
    
    LOWER_CASE_PATTERN = r"[a-z]"
    UPPER_CASE_PATTERN = r"[A-Z]"
    SYMBOLS_PATTER = r"[!@#$%^&*]"
    NUMBERS_PATTERN = r"[0-9]"

    def __init__(self):
        self.pattern_lower = re.compile(self.LOWER_CASE_PATTERN)
        self.pattern_upper = re.compile(self.UPPER_CASE_PATTERN)
        self.pattern_symbols = re.compile(self.SYMBOLS_PATTER)
        self.pattern_numbers = re.compile(self.NUMBERS_PATTERN)
        self.password = None

    def get_pass(self):
        self.password = input("Enter your password: ")
        return self.password
    
    def check_valid_password(self):
        if self.pattern_lower.search(self.password) and self.pattern_numbers.search(self.password) and self.pattern_upper.search(self.password) and self.pattern_symbols.search(self.password):
            return True
        return False
    
    def __str__(self):
        if self.check_valid_password():
            return f"your password is valid"
        return f"Your password is not valid"
    
validator = PasswordValidator()
validator.get_pass()
# validator.check_valid_password()
print(validator)