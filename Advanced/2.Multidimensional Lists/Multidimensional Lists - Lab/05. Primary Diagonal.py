square_size = int(input()) # rows and columns

matrix = []
primary_diagonal_sum = 0

for row in range(square_size):
    columns = list(map(int, input().split()))
    matrix.append(columns)
    primary_diagonal_sum += columns[row]

print(primary_diagonal_sum)


# rows = int(input())
#
# matrix = [
#     [
#         int(num)
#             for num in input().split()
#      ]
#             for row in range(rows)
# ]
#
# sum_diagonal = 0
#
# for column in range(rows):
#     row = column
#     sum_diagonal += matrix[row][column]
#
# print(sum_diagonal)