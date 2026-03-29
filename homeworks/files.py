from pathlib import Path

if not "files":
    Path("Users") / "pavel" / "my_folder" / "python_learning_repository" / "files"

with open("first.txt", "w") as first:
    first.write("First line of the first file\n")
    first.write("Second line of the first file\n")
    first.write("Third line of the first file\n")

with open("second.txt", "w") as second:
    second.write("First line of the second file\n")
    second.write("Second line of the second file\n")
    second.write("Third line of the second file\n")
    
with open("first.txt") as first:
    for line in first:
        print(line)

with open("second.txt") as second:
    while True:
        line = second.readline()
        print(line)
        if not line:
            break



    