rows = int(input())

matrix = [
    [
        int(num)
            for num in input().split()
     ]
            for row in range(rows)
]

sum_diagonal = 0

for column in range(rows):
    row = column
    sum_diagonal += matrix[row][column]

print(sum_diagonal)