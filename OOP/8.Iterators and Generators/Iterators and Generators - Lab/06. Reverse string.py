def reverse_text(string):
    string = string[::-1]
    for char in string:
        yield char

