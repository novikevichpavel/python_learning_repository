# Сокращенный цикл используется для создания новых последовательснотей на основе существующих

# ВЫРАЖЕНИЕ for ЭЛЕМЕНТ in ПОСЛЕДОВТЕЛЬНОСТЬ if УСЛОВИЕ(опционально)



# 1

# all_nums = [3, -1, 5, -4, 11]

# absolute_nums = []

# new_abs_nums = [abs(num) for num in all_nums]
# print(new_abs_nums)

# for i in all_nums:
#     absolute_nums.append(abs(i))

# print(all_nums)
# print(absolute_nums)

# new_abs_nums = [abs(num) for num in all_nums]
# print(new_abs_nums)



# 2

# all_nums = [3, -1, 5, -4, 11]

# pos_nums = []

# for i in all_nums:
#     if i > 0:
#         pos_nums.append(i)

# print(pos_nums)

# new_pos_nums = [num for num in all_nums if num > 0]
# print(new_pos_nums)



# 3

# my_set = {1, 3, 11, 12}

# update_set = set()

# for i in my_set:
#     update_set.add(i * i)

# print(update_set)

# new_update_set = set(i * i for i in my_set)
# new_update_set_two = {i * i for i in my_set}
# print(new_update_set)
# print(new_update_set_two)



# 4

my_scores = {
    "a": 4, 
    "b": 10,
    "c": 15
}

scores = {}

for k, v in my_scores.items():
    scores[k] = v * 2 

print(scores)

new_score = {k: v * 2 for k, v in my_scores.items()}
print(new_score)