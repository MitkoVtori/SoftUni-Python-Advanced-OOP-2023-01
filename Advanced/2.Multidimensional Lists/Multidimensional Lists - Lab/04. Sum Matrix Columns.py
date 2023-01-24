rows, columns = list(map(int, input().split(", ")))

matrix = []
sum_columns = [[] for _ in range(columns)]

for row in range(rows):
    cols = list(map(int, input().split()))
    matrix.append(cols)

    for col in range(columns):
        sum_columns[col].append(cols[col])

[print(sum(cols)) for cols in sum_columns]


# rows, columns = [int(num) for num in input().split(", ")]
#
# matrix = []
#
# for row in range(rows):
#     cols = [int(num) for num in input().split()]
#     matrix.append(cols)
#
# sum_matrix = []
#
# for column in range(columns):
#     column_sum = 0
#
#     for row in range(rows):
#         column_sum += matrix[row][column]
#
#     sum_matrix.append(column_sum)
#
# [print(num) for num in sum_matrix]