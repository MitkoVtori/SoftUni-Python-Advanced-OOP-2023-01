rows, columns = [int(num) for num in input().split(", ")]

matrix = []

for row in range(rows):
    cols = [int(num) for num in input().split()]
    matrix.append(cols)

sum_matrix = []

for column in range(columns):
    column_sum = 0

    for row in range(rows):
        column_sum += matrix[row][column]

    sum_matrix.append(column_sum)

[print(num) for num in sum_matrix]