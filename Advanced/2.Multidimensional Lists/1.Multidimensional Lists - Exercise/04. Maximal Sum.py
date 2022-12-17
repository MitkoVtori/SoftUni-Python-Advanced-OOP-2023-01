rows, columns = list(map(int, input().split()))

matrix = [
    [
        int(col) for col in input().split()
    ]
            for row in range(rows)
]

sum_square = -181
square = []

for row in range(rows):

    try:

        for column in range(columns):

            new_square = []

            ''' Getting the square numbers '''
            first_line = matrix[row][column:column+3]
            second_line = matrix[row+1][column:column+3]
            third_line = matrix[row+2][column:column+3]

            ''' Appending the square numbers to the new_square '''
            [new_square.append(num) for num in first_line]
            [new_square.append(num) for num in second_line]
            [new_square.append(num) for num in third_line]

            ''' 
                Checking if the new square sum is bigger
                Than the old one, and if so, changing the 
                Old square and square sum with the new ones.
            '''
            if sum(new_square) > sum_square:
                sum_square = sum(new_square)
                square = new_square

    except IndexError:
        continue

print(f"Sum = {sum_square}")
[
    print(' '.join(
        [
            str(col) for col in square[cols-3:cols]
        ]
    )
  )
        for cols in range(3, 9 + 1, 3)
]

# [print(' '.join([str(col) for col in square[cols-3:cols]])) for cols in range(3, 9 + 1, 3)]
