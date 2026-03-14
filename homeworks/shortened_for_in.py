# 1

dict_one = {
    "a": "Pavel",
    "b": "Polina",
    "c": "Oksana"
}

dict_two = {k: v.upper() for k, v in dict_one.items()}

print(dict_two)



# 2

list = ["ad", "asffss", "s", "hfdutdf"]

new_list = [i for i in list if len(i) > 3]

print(new_list)