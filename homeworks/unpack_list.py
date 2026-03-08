dict_list = [
    {
        "user_name": "Pavel",
        "user_age": 27
    },
    {
        "user_name": "Polina",
        "user_age": 22
    },
    {
        "user_name": "Oksana",
        "user_age": 32
    }
]

dict_one, dict_two, dict_three = dict_list

def show_info(user_name=None, user_age=None):
    if not user_name or not user_age:
        return f"User not found"
    return f"User {user_name} is {user_age} years old"

print(show_info(**dict_one))
print(show_info(**dict_two))
print(show_info(**dict_three))
