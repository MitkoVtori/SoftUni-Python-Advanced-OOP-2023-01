try:

    file = open("numbers.txt")
    print(sum([int(num) for num in file]))

except ValueError:
    print("String cannot be summed")

except FileNotFoundError:
    print("File not found")