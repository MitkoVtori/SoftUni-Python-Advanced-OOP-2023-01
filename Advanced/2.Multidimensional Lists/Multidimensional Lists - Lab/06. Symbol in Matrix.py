rows = int(input())

matrix = [
    [
        char for char in input()
    ]
        for row in range(rows)
]

find_symbol = input()
found_symbol = False

for row in range(rows):
    columns = len(matrix[row])

    if found_symbol:
        break

    for column in range(columns):

        if matrix[row][column] == find_symbol:

            found_symbol = True
            print((row, column))
            break

if not found_symbol:
    print(f"{find_symbol} does not occur in the matrix")



# square_size = int(input()) # rows and columns
#
# matrix = []
#
# for row in range(square_size):
#     columns = [char for char in input()]
#     matrix.append(columns)
#
# search_symbol = input()
# found_symbol = False
#
# for row in range(square_size):
#
#     for col in range(square_size):
#         if matrix[row][col] == search_symbol:
#             print((row, col))
#             found_symbol = True
#             break
#     if found_symbol:
#         break
#
# if not found_symbol:
#     print(f"{search_symbol} does not occur in the matrix")