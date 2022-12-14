sum_elements_in_matrix = 0

rows, columns = list(map(int, input().split(", ")))

matrix = []
for row in range(rows):

    cols = list(map(int, input().split(", ")))
    sum_elements_in_matrix += sum(cols)
    matrix.append(cols)

print(sum_elements_in_matrix)
print(matrix)