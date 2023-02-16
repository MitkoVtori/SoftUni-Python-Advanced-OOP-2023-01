size = int(input())

food = '*'
lair = "B"
snake = "S"
trail = '.'
top_lair, bottom_lair = [], []
snake_coordinates = [0, 0]

food_eaten = 0

snake_territory = []

for row in range(size):
    columns = [char for char in input()]
    snake_territory.append(columns)

    if snake in columns:
        snake_coordinates = [len(snake_territory)-1, columns.index(snake)]
        snake_territory[snake_coordinates[0]][snake_coordinates[1]] = trail

    if columns.count(lair) == 2:
        turn = 0
        for index in range(len(columns)):
            if turn == 0:
                if columns[index] == lair:
                    top_lair = [len(snake_territory)-1, index]
                    turn += 1

            elif columns[index] == lair and turn == 1:
                bottom_lair = [len(snake_territory)-1, index]
                break

    elif lair in columns:
        if top_lair:
            bottom_lair = [len(snake_territory)-1, columns.index(lair)]
            continue
        top_lair = [len(snake_territory)-1, columns.index(lair)]

snake_out_of_territory = False

while food_eaten < 10:
    movement = input()

    try:

        if movement == "up":
            snake_coordinates[0] -= 1

        elif movement == "down":
            snake_coordinates[0] += 1

        elif movement == "left":
            snake_coordinates[1] -= 1

        elif movement == "right":
            snake_coordinates[1] += 1

        if snake_territory[snake_coordinates[0]][snake_coordinates[1]] == food:
            food_eaten += 1

        elif snake_territory[snake_coordinates[0]][snake_coordinates[1]] == lair:
            snake_territory[snake_coordinates[0]][snake_coordinates[1]] = trail

            if snake_coordinates == top_lair:
                snake_coordinates = bottom_lair

            else:
                snake_coordinates = top_lair

        snake_territory[snake_coordinates[0]][snake_coordinates[1]] = trail

    except IndexError:
        print("Game over!")
        snake_out_of_territory = True
        break

if food_eaten >= 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_eaten}")

if not snake_out_of_territory:
    snake_territory[snake_coordinates[0]][snake_coordinates[1]] = snake

[print(''.join(row)) for row in snake_territory]
