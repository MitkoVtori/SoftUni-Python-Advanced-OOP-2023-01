matrix = [[int(num) for num in input().split()] for rows in range(int(input()))]

for row, col in [[int(num) for num in bomb.split(",")] for bomb in input().split(" ")]:
    if matrix[row][col] <= 0: continue
    bomb_damage, matrix[row][col] = matrix[row][col], 0
    for row_pos, col_pos in ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)):
        if 0 <= row + row_pos < len(matrix) and 0 <= col + col_pos < len(matrix[0]):
            if matrix[row + row_pos][col + col_pos] > 0: matrix[row + row_pos][col + col_pos] -= bomb_damage

alive_cells = [num for row in range(len(matrix)) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells)}")
[print(*matrix[row]) for row in range(len(matrix))]