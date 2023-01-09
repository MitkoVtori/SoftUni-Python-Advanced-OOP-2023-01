def func_executor(*args):
    function_results = []

    for function, elements in args:
        function_results.append(f"{function.__name__} - {function(*elements)}")

    return '\n'.join(function_results)


''' TESTS '''
# def sum_numbers(num1, num2):
#     return num1 + num2


# def multiply_numbers(num1, num2):
#     return num1 * num2


# print(func_executor(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
# ))


# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result


# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result


# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))
