rows = int(input())

matrix = []
for row in range(rows):
    columns = [int(num) for num in input().split(", ")]
    matrix.append([num for num in columns if num % 2 == 0])
    # matrix.append(
    #     [
    #         int(num) for num in input().split(", ")
    #             if int(num) % 2 == 0
    #     ]
    # )

print(matrix)