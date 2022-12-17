rows, columns = list(map(int, input().split()))

matrix = []
squares = 0

for row in range(rows):
    columns = input().split()
    matrix.append(columns)

    try:

        for index, column in enumerate(columns):
            if columns[index + 1] == column:
                if 0 < row and matrix[row - 1][index] == column and matrix[row - 1][index + 1] == column:
                    squares += 1

    except IndexError:
        continue

print(squares)