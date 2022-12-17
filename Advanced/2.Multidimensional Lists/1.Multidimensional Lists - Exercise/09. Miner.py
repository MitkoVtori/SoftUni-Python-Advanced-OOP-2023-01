field_numbers = int(input())
commands = input().split()
mine_field = [input().split() for _ in range(field_numbers)]


def find_starting_position():
    total_coal = 0
    for col in range(len(mine_field)):
        if "s" in mine_field[col]:
            colon = col
            row = mine_field[col].index("s")
        if "c" in mine_field[col]:
            total_coal += mine_field[col].count("c")
    return row, colon, total_coal


col, row, total_coal = find_starting_position()


def check_valid_index(col, row):
    if 0 <= row < len(mine_field) and 0 <= col < len(mine_field[row]):
        return True


def end_of_route(col, row):
    if mine_field[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        exit()


def coal_position(col, row, coal):
    if mine_field[row][col] == "c":
        mine_field[row][col] = "*"
        coal -= 1
    return coal


def up(col, row, total_coal):
    if check_valid_index(row - 1, col):
        row -= 1
        end_of_route(col, row)
        total_coal = coal_position(col, row, total_coal)
    return col, row, total_coal


def down(col, row, total_coal):
    if check_valid_index(row + 1, col):
        row += 1
        end_of_route(col, row)
        total_coal = coal_position(col, row, total_coal)
    return col, row, total_coal


def left(col, row, total_coal):
    if check_valid_index(row, col - 1):
        col -= 1
        end_of_route(col, row)
        total_coal = coal_position(col, row, total_coal)
    return col, row, total_coal


def right(col, row, total_coal):
    if check_valid_index(row, col + 1):
        col += 1
        end_of_route(col, row)
        total_coal = coal_position(col, row, total_coal)
    return col, row, total_coal


command_dic = {
    "up": up,
    "down": down,
    "left": left,
    "right": right

}
for command in commands:
    col, row, total_coal = command_dic[command](col, row, total_coal)
    if total_coal == 0:
        print(f"You collected all coal! ({row}, {col})")
        break
else:
    print(f"{total_coal} pieces of coal left. ({row}, {col})")