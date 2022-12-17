import string

letters_to_numbers = dict(zip(string.ascii_lowercase, range(1, 26 + 1)))

numbers_to_letters = {number: letter for letter, number in letters_to_numbers.items()}

rows, columns = [int(num) for num in input().split()]

palindromes_matrix = []

for row in range(rows):

    cols = []

    for column in range(columns):

        palindrome = numbers_to_letters[row+1] + numbers_to_letters[row+1 + column] + numbers_to_letters[row+1]
        cols.append(palindrome)

    palindromes_matrix.append(cols)

[print(' '.join(palindromes)) for palindromes in palindromes_matrix]