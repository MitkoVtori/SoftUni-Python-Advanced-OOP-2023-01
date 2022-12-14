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