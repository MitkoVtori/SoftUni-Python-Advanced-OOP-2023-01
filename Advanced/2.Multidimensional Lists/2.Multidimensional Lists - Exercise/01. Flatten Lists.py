matrix = input().split("|")

matrix = [char.split() for char in matrix]

[[print(value, end=" ") for value in lst] for lst in matrix[::-1]]