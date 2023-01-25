def multiply(*args):
    '''
        This is a simple multiplication function that
        gets multiple elements and returns their multiplication sum
    '''

    result = 1 # result is set to one, because we do multiplication, and anything multiplied by 0 equals 0.

    for item in args:

        if type(item) is int:

            result *= item

    return result


''' No string tests '''

# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))

''' String tests '''

# print(multiply(1, "Henry", 45))
# print(multiply("First", "class"))
# print(multiply())



# def multiply(*args):
#     result = args[0]
#     for num in args[1:]:
#         result *= num
#     return result
#
#
# ''' TESTS '''
# # print(multiply(1, 4, 5))
# # print(multiply(4, 5, 6, 1, 3))
# # print(multiply(2, 0, 1000, 5000))
