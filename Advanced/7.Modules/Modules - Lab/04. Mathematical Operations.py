from custom_module.math_operations import *

first_number, sign, second_number = input().split()
first_number, second_number = float(first_number), int(second_number)

operations = {
    "/": divide,
    "*": multiply,
    "-": subtract,
    "+": add,
    "^": raise_numbers
}

print(operations[sign](first_number, second_number))