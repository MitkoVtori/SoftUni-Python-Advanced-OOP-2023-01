rows = int(input())

matrix = []
even_matrix = []

for row in range(rows):
    columns = list(map(int, input().split(", ")))
    matrix.append(columns)

[even_matrix.append([num for num in matrix[row] if num % 2 == 0]) for row in range(rows)]

print(even_matrix)



# rows = int(input())
#
# matrix = []
# for row in range(rows):
#     columns = [int(num) for num in input().split(", ")]
#     matrix.append([num for num in columns if num % 2 == 0])
#     # matrix.append(
#     #     [
#     #         int(num) for num in input().split(", ")
#     #             if int(num) % 2 == 0
#     #     ]
#     # )
#
# print(matrix)



# even_matrix = []
# result = [[even_matrix.append([num for num in list(map(int, input().split(", "))) if num % 2 == 0]) for row in range(int(input()))], print(even_matrix)]
