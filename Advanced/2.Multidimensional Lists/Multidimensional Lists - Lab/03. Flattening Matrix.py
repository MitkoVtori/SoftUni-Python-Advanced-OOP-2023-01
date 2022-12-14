rows = int(input())

matrix = []

for row in range(rows):
    columns = input().split(", ")
    matrix.append(columns)

flattening_matrix = [int(num) for elements in matrix for num in elements]
print(flattening_matrix)