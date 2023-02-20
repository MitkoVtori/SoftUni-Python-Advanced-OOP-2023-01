rows, columns = list(map(int, input().split()))

furniture_obstacles = "O"
empty = "-"
opponents = "P"
player = "B"
player_coordinates = [0, 0]
playground = []

for row in range(rows):
    cols = input().split()
    playground.append(cols)

    if player in cols:
        player_coordinates = [len(playground)-1, cols.index(player)]
        playground[player_coordinates[0]][player_coordinates[1]] = empty

opponents_count = 0
moves_count = 0

movement = input()
while movement != "Finish" and opponents_count < 3:

    if movement == "up":
        if 0 <= player_coordinates[0]-1 <= len(playground)-1:
            if playground[player_coordinates[0]-1][player_coordinates[1]] != furniture_obstacles:
                player_coordinates[0] -= 1
                moves_count += 1

    elif movement == "down":
        if 0 <= player_coordinates[0]+1 <= len(playground) - 1:
            if playground[player_coordinates[0] + 1][player_coordinates[1]] != furniture_obstacles:
                player_coordinates[0] += 1
                moves_count += 1

    elif movement == "left":
        if 0 <= player_coordinates[1]-1 <= len(playground[0]) - 1:
            if playground[player_coordinates[0]][player_coordinates[1]-1] != furniture_obstacles:
                player_coordinates[1] -= 1
                moves_count += 1

    elif movement == "right":
        if 0 <= player_coordinates[1] + 1 <= len(playground[0]) - 1:
            if playground[player_coordinates[0]][player_coordinates[1]+1] != furniture_obstacles:
                player_coordinates[1] += 1
                moves_count += 1

    if playground[player_coordinates[0]][player_coordinates[1]] == opponents:
        opponents_count += 1
        playground[player_coordinates[0]][player_coordinates[1]] = empty

    movement = input()

print("Game over!")
print(f"Touched opponents: {opponents_count} Moves made: {moves_count}")
