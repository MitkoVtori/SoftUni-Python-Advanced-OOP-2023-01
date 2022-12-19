rows = int(input())
matrix = [[char for char in input().split()] for row in range(rows)]
columns = len(matrix[0])

score, movement = [0], {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def check_movement(row, col):

    if 0 <= row < rows and 0 <= col < columns and matrix[row][col] != "R":
        return True

    print("Alice didn't make it to the tea party.")

    rabit_row, rabit_col = find_position("R", False)

    if rabit_row + rabit_col == row + col:
        matrix[row][col] = "*"

    show_result()
    exit()


def find_position(symbol, alice=True):

    for row in range(rows):

        if symbol in matrix[row]:

            col = matrix[row].index(symbol)

            if alice:

                matrix[row][col] = "*"

            return row, col


alice_row, alice_col = find_position("A")


def alice_movement(row, col, movement_pos):

    move_row, move_col = row + movement[movement_pos][0], col + movement[movement_pos][1]

    if check_movement(move_row, move_col):

        if matrix[move_row][move_col][-1].isdigit():

            score[0] += int(matrix[move_row][move_col])

        matrix[move_row][move_col] = "*"

    return move_row, move_col


def show_result():
    [print(*matrix[row]) for row in range(rows)]


while score[0] < 10:
    move = input()
    alice_row, alice_col = alice_movement(alice_row, alice_col, move)

print("She did it! She went to the party.")
show_result()