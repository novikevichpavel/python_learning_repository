from array import array
import sys

if len(sys.argv) < 2:
    raise IOError("Provide two args")

file_name = sys.argv[1]

imported_array = array("i")

with open(file_name, "rb") as file:
    imported_array.fromfile(file, 3)
    print(imported_array)