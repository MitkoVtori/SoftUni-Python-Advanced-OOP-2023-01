def read_text():

    try:

        file = open("text.txt", "r")
        lines = [line for line in file] # getting every line from the text
        file.close()

    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    for line in range(len(lines)):

        letters = 0
        punctuation_marks = 0

        for character in range(len(lines[line])):

            char = lines[line][character]

            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122: # if char is letter
                letters += 1

            elif 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64: # if char is punctuation mark
                punctuation_marks += 1

        if lines[line][-1] == '\n': # if the sentence ends with '\n' which stands for new line.
            lines[line] = lines[line][:-1] # We remove it, because otherwise it would give us wrong output

        lines[line] = f"Line {line+1}: {lines[line]} ({letters})({punctuation_marks})\n"

    return lines


def output_txt(text):

    file = open("output.txt", "w") # create for writing
    [file.write(line) for line in text] # write the output in
    file.close() # close for writing

    file = open("output.txt", "r") # open for reading
    output = ''.join([line for line in file]) # read every line from the text
    file.close() # close file for reading

    return output


text = read_text()
print(output_txt(text))