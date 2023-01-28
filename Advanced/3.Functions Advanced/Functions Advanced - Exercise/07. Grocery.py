def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return '\n'.join([f"{item[0]}: {item[1]}" for item in products])


""" ON ONE LINE!!! """
# def grocery_store(**kwargs): return '\n'.join([f"{item[0]}: {item[1]}" for item in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))])




''' TESTS '''
# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))

# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))





# def grocery_store(**kwargs):
#     '''
#
#         The groceries should be sorted by their quantity in descending order.
#         If there are two or more products with the same quantity,
#         the groceries should be sorted by their name's length in descending order.
#         If there are two or more products with the same name's length,
#         the groceries should be sorted by their name in ascending order (alphabetically).
#
#     '''
#
#     string = ''
#
#     for item, quantity in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
#         string += f'{item}: {quantity}\n'
#
#     return string
#
#
# ''' TESTS '''
# # print(grocery_store(
# #     bread=5,
# #     pasta=12,
# #     eggs=12,
# # ))
#
# # print(grocery_store(
# #     bread=2,
# #     pasta=2,
# #     eggs=20,
# #     carrot=1,
# # ))