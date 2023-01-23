from math import floor


def multiply():
    global sentence

    manual_check = " * ".join([str(num) for num in sentence])
    result = 1

    for item in sentence:
        result *= int(item)

    manual_check += f" = {result}"
    return manual_check, result


def add():
    global sentence

    manual_check = " + ".join([str(num) for num in sentence])
    result = sum([int(num) for num in sentence])

    manual_check += f" = {result}"
    return manual_check, result


def divide():
    global sentence

    manual_check = " / ".join([str(num) for num in sentence])
    result = int(sentence[0])

    try:

        for index in range(len(sentence)):
            result /= int(sentence[index + 1])

    except IndexError:
        manual_check += f" = {result}"
        return manual_check, result


def subtract():
    global sentence

    manual_check = " - ".join([str(num) for num in sentence])
    result = int(sentence[0])

    try:

        for index in range(len(sentence)):
            result -= int(sentence[index + 1])

    except IndexError:
        manual_check += f" = {result}"
        return manual_check, result


sentence = []

operations = {
    "*": multiply,
    "+": add,
    "/": divide,
    "-": subtract
}

expression = input().split()
result = 0

for item in expression.copy():

    index = expression.index(item)

    if item in operations.keys():
        sentence = expression[0:index]
        result = operations[item]()
        # print(result[0])
        expression = expression[index + 1:]
        expression.insert(0, result[1])

print(floor(result[1]))








# from math import floor
# from collections import deque
#
# '''
#     Note:
#         We need only the result at the end of an operation.
#         In the returns you may see not just the result, but the formula also.
#         This is made just for debugging. In case something's wrong,
#         we can easily see what the current function does.
# '''
#
#
# def multiply(numbers: deque):
#     global result
#     result = 1 # The result is set to one, because any number multiplied by 0 will equal 0
#
#     for num in numbers:
#         result *= num
#
#     return f"{' * '.join([str(num) for num in numbers])} = {result}"
#
#
# def divide(numbers: deque):
#     global result
#
#     formula = ' / '.join([str(num) for num in numbers]) # This is made here, because after the for loop below the numbers will be different
#
#     for index in range(len(numbers) - 1):
#         numbers[index + 1] = numbers[index] / numbers[index + 1] # Here, we make the second index(divisor) become the result of the division
#
#     result = floor(numbers[-1]) # After the for loop, we made the last number result of the whole division, so the result is just the last number.
#
#     return f"{formula} = {result}"
#
#
# def add(numbers: deque):
#     global result
#     result = sum(numbers)
#
#     return f"{' + '.join([str(num) for num in numbers])} = {result}"
#
#
# def subtract(numbers: deque):
#     global result
#
#     formula = ' - '.join([str(num) for num in numbers]) # This is made here, because after the for loop below the numbers will be different
#
#     for index in range(len(numbers) - 1):
#         numbers[index + 1] = numbers[index] - numbers[index + 1] # Here, we make the second index(divisor) become the result of the subtraction
#
#     result = numbers[-1] # After the for loop, we made the last number result of the whole subtraction, so the result is just the last number.
#
#     return f"{formula} = {result}"
#
#
# valid_operations = ["*", "+", "-", "/"]
#
# expression = input().split()
# expression_copy = expression.copy() # We made copy, so I can do whatever I want with it, without affecting the for loop or changing the expression.
# operation_numbers = deque()
#
# last_operator_index = 0 # This is used to see, what the last operation result was, so we work directly with the new number.
# last_operator = 0 # This is used to print the last result of the operations.
#
# for index, char in enumerate(expression):
#
#     if char in valid_operations:
#
#         [operation_numbers.append(int(num)) for num in expression_copy[last_operator_index:index]] # We get all numbers, from the last result to the operation.
#
#         if char == "*":
#
#             operation = multiply(operation_numbers)
#
#             expression_copy[index] = f'{result}' # Here we save the result on the place of the operation
#             last_operator_index = index
#
#             last_operator = operation.split()[-1] # We need to print only the result at the end.
#
#         elif char == "/":
#
#             operation = divide(operation_numbers)
#
#             expression_copy[index] = f'{result}' # Here we save the result on the place of the operation
#             last_operator_index = index
#
#             last_operator = operation.split()[-1] # We need to print only the result at the end.
#
#         elif char == "+":
#
#             operation = add(operation_numbers)
#
#             expression_copy[index] = f'{result}' # Here we save the result on the place of the operation
#             last_operator_index = index
#
#             last_operator = operation.split()[-1] # We need to print only the result at the end.
#
#         elif char == "-":
#
#             operation = subtract(operation_numbers)
#
#             expression_copy[index] = f'{result}' # Here we save the result on the place of the operation
#             last_operator_index = index
#
#             last_operator = operation.split()[-1] # We need to print only the result at the end.
#
#         operation_numbers = deque()
#
# print(last_operator)
