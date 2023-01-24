rows = int(input())

matrix = []

for row in range(rows):
    columns = list(map(int, input().split(", ")))
    matrix.append(columns)

flattening_matrix = []
[[flattening_matrix.append(num) for num in matrix[row]] for row in range(rows)]

print(flattening_matrix)



# rows = int(input())
#
# matrix = []
#
# for row in range(rows):
#     columns = input().split(", ")
#     matrix.append(columns)
#
# flattening_matrix = [int(num) for elements in matrix for num in elements]
# print(flattening_matrix)