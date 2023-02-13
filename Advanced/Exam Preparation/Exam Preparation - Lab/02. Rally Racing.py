def get_field(size):
    racer_number = input()
    up_tunnel_entry, down_tunnel_entry = [], []
    matrix = []

    for row in range(size):
        columns = input().split()
        matrix.append(columns)

        if columns.count("T") == 2:
            t_number = 0
            for index, col in enumerate(columns):
                if col == "T" and t_number == 0:
                    t_number += 1
                    up_tunnel_entry = (len(matrix)-1, index)

                elif col == "T" and t_number == 1:
                    down_tunnel_entry = (len(matrix)-1, index)

        elif columns.count("T") == 1:

            if not up_tunnel_entry:
                up_tunnel_entry = (len(matrix)-1, columns.index("T"))

            else:
                down_tunnel_entry = (len(matrix)-1, columns.index("T"))

    return racer_number, up_tunnel_entry, down_tunnel_entry, matrix


def race(matrix, top_tunnel_entry, bottom_tunnel_entry):
    racer_coordinates = [0, 0]
    kilometers = 0

    movement = input()
    while movement != "End":

        if movement == "up":
            racer_coordinates[0] -= 1

        elif movement == "down":
            racer_coordinates[0] += 1

        elif movement == "left":
            racer_coordinates[1] -= 1

        elif movement == "right":
            racer_coordinates[1] += 1

        if matrix[racer_coordinates[0]][racer_coordinates[1]] == "T":
            kilometers += 20

            if tuple(racer_coordinates) == top_tunnel_entry:
                racer_coordinates = list(bottom_tunnel_entry)

            elif tuple(racer_coordinates) == bottom_tunnel_entry:
                racer_coordinates = list(top_tunnel_entry)

            matrix[top_tunnel_entry[0]][top_tunnel_entry[1]] = "."
            matrix[bottom_tunnel_entry[0]][bottom_tunnel_entry[1]] = "."

        kilometers += 10

        if matrix[racer_coordinates[0]][racer_coordinates[1]] == "F":
            matrix[racer_coordinates[0]][racer_coordinates[1]] = "C"
            return [True, kilometers]

        movement = input()

    matrix[racer_coordinates[0]][racer_coordinates[1]] = "C"
    return [False, kilometers]


matrix_size = int(input())
racer, top_tunnel, bottom_tunnel, matrix = get_field(matrix_size)

finished, kilometers = race(matrix, top_tunnel, bottom_tunnel)

if finished:
    print(f"Racing car {racer} finished the stage!")

else:
    print(f"Racing car {racer} DNF.")


print(f"Distance covered {kilometers} km.")
[print(''.join(column)) for column in matrix]
