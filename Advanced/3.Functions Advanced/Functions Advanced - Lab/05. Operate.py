def operate(operation, *args):
    result = args[0]

    if operation == "+":
        result = sum(args)

    elif operation == "-":
        for num in args[1:]:
            result -= num

    elif operation == "/":
        for num in args[1:]:
            result /= num

    elif operation == "*":
        for num in args[1:]:
            result *= num

    return result


''' ---- Tests ---- '''
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("-", 17, 12, 3))
# print(operate("/", 20, 5, 2))




# from collections import deque
#
#
# class Operate:
#
#     def __init__(self, operation, *args):
#         self.operation = operation
#         self.numbers = deque(args)
#
#     def multiply(self):
#         result = 1
#
#         length = len(self.numbers)
#
#         for num in range(length):
#             result *= self.numbers.popleft()
#
#         return result
#
#     def add(self):
#         result = 0
#
#         length = len(self.numbers)
#
#         for num in range(length):
#             result += self.numbers.popleft()
#
#         return result
#
#     def divide(self):
#
#         try:
#
#             length = len(self.numbers)
#
#             for num in range(length):
#                 result = self.numbers.popleft()
#                 result /= self.numbers.popleft()
#                 self.numbers.appendleft(result)
#
#         except IndexError:
#             return result
#
#     def subtract(self):
#
#         try:
#
#             length = len(self.numbers)
#
#             for num in range(length):
#                 result = self.numbers.popleft()
#                 result -= self.numbers.popleft()
#                 self.numbers.appendleft(result)
#
#         except IndexError:
#             return result
#
#     def check_operation(self):
#
#         if self.operation == "*":
#             return self.multiply()
#
#         elif self.operation == "+":
#             return self.add()
#
#         elif self.operation == "/":
#             return self.divide()
#
#         elif self.operation == "-":
#             return self.subtract()
#
#     def __repr__(self):
#         return str(self.check_operation())


# operate = Operate

# ''' ---- Tests ---- '''
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("-", 17, 12, 3))
# print(operate("/", 20, 5, 2))