import sys

rows, columns = list(map(int, input().split(", ")))

matrix = []
submatrix = []
sum_submatrix = -sys.maxsize

for row in range(rows):
    cols = list(map(int, input().split(", ")))
    matrix.append(cols)

for row in range(rows):

    for col in range(columns):
        if row+1 < rows and col+1 < columns:
            square = [matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]
            if sum(square) > sum_submatrix:
                submatrix = [[square[0], square[1]], [square[2], square[3]]]
                sum_submatrix = sum(square)

[print(' '.join([str(col) for col in row])) for row in submatrix]
print(sum_submatrix)




# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [7, 1, 3, 3, 2, 1],
#             [1, 3, 9, 8, 5, 6],
#             [4, 6, 7, 9, 1, 0],
#         ]
#
#     else:
#
#         (rows_count, columns_count) = map(int, input().split(', '))
#
#         matrix = []
#
#         for row_index in range(rows_count):
#             row = [int(x) for x in input().split(', ')]
#             matrix.append(row)
#
#         return matrix
#
#
# def get_sum_of_submatrix(matrix, row_index, column_index, size):
#
#     the_sum = 0
#
#     for r in range(row_index, row_index + size):
#         for c in range(column_index, column_index + size):
#             the_sum += matrix[r][c]
#
#     return the_sum
#
#
# def get_best_submatrix_sum_coordinates(matrix, submatrix_size):
#
#     best_row_index = 0
#     best_column_index = 0
#     best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)
#
#     for row_index in range(len(matrix) - submatrix_size + 1):
#
#         for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
#
#             current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
#
#             if best_sum < current_sum:
#                 best_sum = current_sum
#                 best_row_index = row_index
#                 best_column_index = col_index
#
#     return (best_row_index, best_column_index)
#
#
# def print_result(coordinates, size):
#
#     (row_index, col_index) = coordinates
#
#     for r in range(row_index, row_index + size):
#
#         row = []
#
#         for c in range(col_index, col_index + size):
#
#             row.append(matrix[r][c])
#
#         print(' '.join(str(x) for x in row))
#
#     print(get_sum_of_submatrix(matrix, row_index, col_index, size))
#
#
# SUBMATRIX_SIZE = 2
#
# matrix = read_matrix()
# coordinates = get_best_submatrix_sum_coordinates(matrix, SUBMATRIX_SIZE)
# print_result(coordinates, SUBMATRIX_SIZE)