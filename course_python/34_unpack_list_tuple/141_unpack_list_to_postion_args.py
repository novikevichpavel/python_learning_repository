user_data = ["Pavel", 27]

def user_info(name, commnets_qty):
    if not commnets_qty:
        return f"User {name} has no commnets"
    return f"User {name} has {commnets_qty} comments"

print(user_info(*user_data))