matrix_size = 5

matrix = [[char for char in input().split()] for row in range(matrix_size)]

dead_targets_pos, number_of_commands = [], int(input())
total_targets = [sum([matrix[row].count("x") for row in range(matrix_size)])]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def find_position():
    for row in range(matrix_size):
        if "A" in matrix[row]:
            col = matrix[row].index("A")
            matrix[row][col] = "."
            return row, col


player_row, player_col = find_position()


def shoot(row, col, direction):
    for shoot in range(matrix_size):

        shooting_row, shooting_col = row + directions[direction][0], col + directions[direction][1]

        if check_valid_index(shooting_row, shooting_col):

            if matrix[shooting_row][shooting_col] == "x":

                total_targets[0] -= 1
                dead_targets_pos.append([shooting_row, shooting_col])
                matrix[shooting_row][shooting_col] = "."

                break

            row, col = shooting_row, shooting_col

        else:

            break


def moving(row, col, direction, steps):

    total_step = [num * steps if num != 0 else 0 for num in directions[direction]]
    moving_row, moving_col = row + total_step[0], col + total_step[1]

    if check_valid_index(moving_row, moving_col) and matrix[moving_row][moving_col] == ".":

        matrix[row][col] = "."
        matrix[moving_row][moving_col] = "A"

        return moving_row, moving_col

    return row, col


def show_result():
    [print(x) for x in dead_targets_pos]


for num in range(number_of_commands):

    command = input().split()

    if "shoot" in command[0]:
        shoot(player_row, player_col, command[1])

    elif "move" in command[0]:
        player_row, player_col = moving(player_row, player_col, command[1], int(command[-1]))

    if total_targets[0] == 0:

        print(f"Training completed! All {len(dead_targets_pos)} targets hit.")
        show_result()
        break
else:
    print(f"Training not completed! {total_targets[0]} targets left.")
    show_result()