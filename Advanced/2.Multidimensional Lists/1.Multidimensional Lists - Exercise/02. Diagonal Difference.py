rows = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    ''' Appending the columns into the matrix '''
    columns = [int(num) for num in input().split()]
    matrix.append(columns)

    ''' Getting the matrix primary diagonal'''
    column = row
    primary_diagonal.append(matrix[row][column])

    ''' Getting the matrix secondary diagonal '''
    secondary_columns = columns[::-1]
    secondary_diagonal.append(secondary_columns[row])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))