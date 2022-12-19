presents = [int(input())]
rows = int(input())
matrix = [[char for char in input().split()] for row in range(rows)]
cols, total_nice_kids = len(matrix[0]), [[sum([matrix[row].count("V") for row in range(rows)])] * 2]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


def find_position():
    for row in range(rows):
        if "S" in matrix[row]:
            col = matrix[row].index("S")
            matrix[row][col] = "-"
            return row, col


def check_where_he_steps(row, col, cookie=False):
    if matrix[row][col] == "V":
        total_nice_kids[0][0] -= 1
        presents[0] -= 1

    elif cookie and matrix[row][col] == "X":
        presents[0] -= 1

    elif matrix[row][col] == "C":
        cookie_time(row, col)

    matrix[row][col] = "-"


def cookie_time(row, col):
    for added_row, added_col in directions.values():

        moving_row, moving_col = row + added_row, col + added_col

        if check_valid_index(moving_row, moving_col):
            check_where_he_steps(moving_row, moving_col, True)


def santa_move(row, col, direction):
    santa_moving_row, santa_moving_col = row + directions[direction][0], col + directions[direction][1]

    if check_valid_index(santa_moving_row, santa_moving_col):
        check_where_he_steps(santa_moving_row, santa_moving_col)

    return santa_moving_row, santa_moving_col


def check_for_end():
    if total_nice_kids[0][0] == 0:

        show_result(santa_row, santa_col)
        print(f"Good job, Santa! {total_nice_kids[0][1]} happy nice kid/s.")
        exit()

    if presents[0] == 0 and total_nice_kids[0][0] > 0:

        print("Santa ran out of presents!")
        show_result(santa_row, santa_col)
        print(f"No presents for {total_nice_kids[0][0]} nice kid/s.")
        exit()
    if presents[0] == 0:

        show_result(santa_row, santa_col)
        print(f"No presents for {total_nice_kids[0][0]} nice kid/s.")
        exit()


def show_result(row, col):
    matrix[row][col] = "S"
    [print(*matrix[row]) for row in range(rows)]


santa_row, santa_col = find_position()
command = input()

while command != "Christmas morning":
    santa_row, santa_col = santa_move(santa_row, santa_col, command)
    check_for_end()
    command = input()

show_result(santa_row, santa_col)
print(f"No presents for {total_nice_kids[0][0]} nice kid/s.")