def sorting_cheeses(**kwargs):

    '''

        The function receives a dictionary with cheeses as keys and lists of pieces as values.
        We should return the cheeses and their pieces' as quantities sorted by the number of pieces
        of a cheese kind in descending order. If two or more cheeses have the same number of pieces,
        we should sort them by their names in ascending order (alphabetically).
        For each kind of cheese, we return their pieces quantities in descending order.

    '''

    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    cheeses = []

    for cheese, pieces_count in sorted_cheeses:
        cheeses.append(cheese)
        quantities = sorted(pieces_count, reverse=True)
        cheeses += quantities

    return '\n'.join([str(cheese) for cheese in cheeses])


# print('---- Documentation ----')
# print(sorting_cheeses.__doc__)
# print()
# print('---- Tests ----')
# print()
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
# print()
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )