size = int(input())

battle_field = []
submarine = [0, 0]

for row in range(size):
    columns = [char for char in input()]
    battle_field.append(columns)

    if 'S' in columns:
        submarine = [len(battle_field)-1, columns.index('S')]
        battle_field[submarine[0]][submarine[1]] = '-'


naval_mines = 0
cruisers = 0

while True:
    movement = input()

    if movement == "up":
        submarine[0] -= 1

    elif movement == "down":
        submarine[0] += 1

    elif movement == "left":
        submarine[1] -= 1

    elif movement == "right":
        submarine[1] += 1

    if battle_field[submarine[0]][submarine[1]] == "*":
        naval_mines += 1
        battle_field[submarine[0]][submarine[1]] = '-'

        if naval_mines == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
            break

    elif battle_field[submarine[0]][submarine[1]] == "C":
        cruisers += 1
        battle_field[submarine[0]][submarine[1]] = '-'

        if cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

battle_field[submarine[0]][submarine[1]] = 'S'
[print(''.join(row)) for row in battle_field]