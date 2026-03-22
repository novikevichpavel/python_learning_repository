class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")

custom_list = ExtendedList([2, 3, 4])
custom_list.print_list_info()