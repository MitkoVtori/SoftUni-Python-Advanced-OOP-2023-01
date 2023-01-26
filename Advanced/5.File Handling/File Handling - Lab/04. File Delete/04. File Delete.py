import os

try:
    os.remove("my_first_file.txt")
except FileNotFoundError:
    print("File already deleted!")