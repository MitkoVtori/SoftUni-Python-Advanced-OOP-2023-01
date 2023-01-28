def even_odd_filter(**kwargs):

    for key, values in kwargs.items():

        if key == "even":
            kwargs[key] = [num for num in values if num % 2 == 0]

        elif key == "odd":
            kwargs[key] = [num for num in values if num % 2 != 0]

    sorted_tuple = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    sorted_dict = {item[0]: item[1] for item in sorted_tuple}

    return sorted_dict


''' TESTS '''
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))



# def even_odd_filter(**kwargs):
#     for key, numbers in kwargs.items():
#         if key == 'even':
#             kwargs[key] = [num for num in numbers if num % 2 == 0]
#
#         elif key == 'odd':
#             kwargs[key] = [num for num in numbers if num % 2 != 0]
#
#     return {key: numbers for key, numbers in sorted(kwargs.items(), key=lambda x: -len(x[1]))}
#
#
# ''' TESTS '''
# # print(even_odd_filter(
# #     odd=[1, 2, 3, 4, 10, 5],
# #     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# # ))
# # print(even_odd_filter(
# #     odd=[2, 2, 30, 44, 10, 5],
# # ))