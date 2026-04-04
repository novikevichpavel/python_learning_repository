import re

my_str = "My name is Pavel."

print(re.search("Pavel", my_str))
print(re.search("P...l", my_str))

print(re.search("Pavel.$", my_str)) # $ - указывает, что слово в конце строки, . - указывает, что после слова може быть один символ

new_str = "Her name is Polina."

print(re.search("^M.*name", new_str)) # ^ - указывает, что поиск происхоидт в начале строки, .* - указыает, что между символами может быть что угодно


my_pattern = re.compile("^Her.*\.$")

print(my_pattern.search(new_str))
print(my_pattern.match(new_str))