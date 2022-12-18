rows = int(input())

matrix = []

for row in range(rows):
    columns = [int(num) for num in input().split()]
    matrix.append(columns)

command = input().split()
while command[0] != "END":

    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):

        if command[0] == "Add":
            matrix[row][col] += value

        elif command[0] == "Subtract":
            matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    command = input().split()

[print(*row) for row in matrix]