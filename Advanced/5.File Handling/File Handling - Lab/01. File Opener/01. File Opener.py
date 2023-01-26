try:

    file = open("text.txt", 'r')
    print("File found")

except FileNotFoundError:
    print("File not found")