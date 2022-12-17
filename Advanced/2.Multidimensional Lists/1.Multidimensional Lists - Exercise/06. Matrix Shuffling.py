rows, columns = [int(num) for num in input().split()]

matrix = []

for row in range(rows):
    cols = input().split()
    matrix.append(cols)

command = input().split()
while command[0] != "END":

    if command[0] == "swap":

        if not len(command) > 5:
            try:

                row1 = int(command[1])
                col1 = int(command[2])
                row2 = int(command[3])
                col2 = int(command[4])

            except ValueError:
                print("Invalid input!")
                continue

            if 0 <= row1 <= rows and 0 <= row2 <= rows and col1 <= columns and col2 <= columns:

                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

                for colons in matrix:
                    print(' '.join(colons))

            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input().split()