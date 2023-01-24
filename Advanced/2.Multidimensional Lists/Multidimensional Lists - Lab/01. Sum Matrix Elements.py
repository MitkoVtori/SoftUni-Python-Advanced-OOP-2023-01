rows, columns = list(map(int, input().split(", ")))

matrix = []

sum_matrix = 0

for row in range(rows):
    cols = list(map(int, input().split(", ")))
    matrix.append(cols)
    sum_matrix += sum(cols)

print(sum_matrix)
print(matrix)