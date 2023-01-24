import sys

rows, columns = list(map(int, input().split()))

matrix = [
    [int(num) for num in input().split()]
    for row in range(rows)
]

maximal_sum_matrix = []
maximal_sum = -sys.maxsize

end_of_matrix = False

for row in range(rows):

    for col in range(columns):
        if row+2 < rows and col+2 < columns:
            check_matrix = [
                [
                    matrix[row][col], matrix[row][col+1], matrix[row][col+2]
                ],
                [
                    matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]
                ],
                [
                    matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]
                ]
            ]
            sum_check_matrix = sum(check_matrix[0]) + sum(check_matrix[1]) + sum(check_matrix[2])
            if sum_check_matrix > maximal_sum:
                maximal_sum_matrix = check_matrix
                maximal_sum = sum_check_matrix

print(f"Sum = {maximal_sum}")
[print(' '.join([str(num) for num in row])) for row in maximal_sum_matrix]



# rows, columns = list(map(int, input().split()))
#
# matrix = [
#     [
#         int(col) for col in input().split()
#     ]
#             for row in range(rows)
# ]
#
# sum_square = -181
# square = []
#
# for row in range(rows):
#
#     try:
#
#         for column in range(columns):
#
#             new_square = []
#
#             ''' Getting the square numbers '''
#             first_line = matrix[row][column:column+3]
#             second_line = matrix[row+1][column:column+3]
#             third_line = matrix[row+2][column:column+3]
#
#             ''' Appending the square numbers to the new_square '''
#             [new_square.append(num) for num in first_line]
#             [new_square.append(num) for num in second_line]
#             [new_square.append(num) for num in third_line]
#
#             '''
#                 Checking if the new square sum is bigger
#                 Than the old one, and if so, changing the
#                 Old square and square sum with the new ones.
#             '''
#             if sum(new_square) > sum_square:
#                 sum_square = sum(new_square)
#                 square = new_square
#
#     except IndexError:
#         continue
#
# print(f"Sum = {sum_square}")
# [
#     print(' '.join(
#         [
#             str(col) for col in square[cols-3:cols]
#         ]
#     )
#   )
#         for cols in range(3, 9 + 1, 3)
# ]
#
# # [print(' '.join([str(col) for col in square[cols-3:cols]])) for cols in range(3, 9 + 1, 3)]
