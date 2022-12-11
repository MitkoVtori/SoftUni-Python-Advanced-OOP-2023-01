symbols = tuple(sorted([char for char in input()])) # makes a tuple of every single character

counted_characters = [] # checks if a character is already counted

for symbol in symbols:

    if symbol not in counted_characters:
        print(f"{symbol}: {symbols.count(symbol)} time/s")
        counted_characters.append(symbol)