rows, columns = list(map(int, input().split()))

matrix = [input().split() for row in range(rows)]

squares = 0

for row in range(rows):

    for col in range(columns):
        if row+1 < rows and col+1 < columns:
            symbol = matrix[row][col]
            if matrix[row][col+1] == symbol and matrix[row+1][col] == symbol and matrix[row+1][col+1] == symbol:
                squares += 1

print(squares)


# rows, columns = list(map(int, input().split()))
#
# matrix = []
# squares = 0
#
# for row in range(rows):
#     columns = input().split()
#     matrix.append(columns)
#
#     try:
#
#         for index, column in enumerate(columns):
#             if columns[index + 1] == column:
#                 if 0 < row and matrix[row - 1][index] == column and matrix[row - 1][index + 1] == column:
#                     squares += 1
#
#     except IndexError:
#         continue
#
# print(squares)