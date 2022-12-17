rows, cols = [int(num) for num in input().split()]
matrix = [[char for char in input()] for _ in range(rows)]
commands = input()

winner, movement = False, {
    "U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]
}


def find_player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")


def player_alive(row, col):
    if matrix[row][col] == "B":
        show_result("dead")


def check_valid_index(row, col, player=False):
    global winner

    if 0 <= row < rows and 0 <= col < cols:
        return True

    if player:
        winner = True


def bunnies_position():
    position = []

    for row in range(rows):

        for col in range(cols):

            if matrix[row][col] == "B":

                position.append(row)
                position.append(col)

    return position


def bunnies_moves(bunnies_pos):
    for i in range(0, len(bunnies_pos), 2):

        row, col = bunnies_pos[i], bunnies_pos[i + 1]

        for bunnie_move in movement:

            new_row, new_col = row + movement[bunnie_move][0], col + movement[bunnie_move][1]

            if check_valid_index(new_row, new_col):

                matrix[new_row][new_col] = "B"


def show_result(status="won"):
    [print(*matrix[row], sep="") for row in range(rows)]
    print(f"{status}: {player_row} {player_col}")
    exit()


player_row, player_col = find_player_position()
matrix[player_row][player_col] = "."

for command in commands:

    player_movement_row, player_movement_col = player_row + movement[command][0], player_col + movement[command][1]

    if check_valid_index(player_movement_row, player_movement_col, True):

        player_row, player_col = player_movement_row, player_movement_col

    bunnies_moves(bunnies_position())

    if winner:

        show_result()

    if check_valid_index(player_movement_row, player_movement_col):

        player_alive(player_movement_row, player_movement_col)