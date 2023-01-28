def even_odd(*args):
    args, even_or_odd = args[:-1], args[-1]

    if even_or_odd == "even":
        return [num for num in args if num % 2 == 0]

    elif even_or_odd == "odd":
        return [num for num in args if num % 2 != 0]


''' TESTS '''
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
