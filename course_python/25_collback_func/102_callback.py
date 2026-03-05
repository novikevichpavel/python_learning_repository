# Колбэк функция - функция, которая передается, как аргумент в другую функцию и там вызывается 

def other_fn():
    pass


def fn_with_callback(callback_fn):
    callback_fn()


fn_with_callback(other_fn)



# 2

def print_number_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def procces_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input("Enter number: "))

procces_number(entered_num, print_number_info)


# 3

def send_data():
    pass


def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    send_data_fn(updated_data)


process_data({"name":"Pavel"}, send_data)