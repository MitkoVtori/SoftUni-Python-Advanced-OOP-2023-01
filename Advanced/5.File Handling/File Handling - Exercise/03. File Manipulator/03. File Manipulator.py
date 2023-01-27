import os
import time


def create_file(file_name, *args): # *args is in case we receive more than one parameter
    try:
        ''' Delete file content '''

        os.remove(file_name) # removing file
        file = open(file_name, "x") # creating file
        file.close() # closing file
        print(f"File {file_name} content was deleted") # comment that will show on the console if the content is deleted

    except FileNotFoundError:
        ''' Create file '''

        file = open(file_name, "x") # creating file
        file.close() # closing file
        print(f"File {file_name} was created") # comment, that will show on the console, if the creation was successful


def add_content(file_name, *args_content): # *args_content is in case we receive more than two parameters
    content = args_content[0]

    if os.path.exists(file_name):
        print(f"Content added to {file_name}") # comment that will show on the console if the file exists

    else:
        print(f"Created {file_name} and added content") # comment that will show, if the file does not exist

    file = open(file_name, "a+") # open file if it exists, else it creates the file.
    file.write(f"{content}\n") # adding the content
    file.close() # closing file


def replace_content(file_name, *content): # *content is in case we receive more than two parameters
    old_content, new_content, = content[0], content[1]

    try:

        file = open(file_name, "r") # open for reading
        lines = [line for line in file] # read lines
        file.close() # close for reading

        for index, line in enumerate(lines):
            line = line.replace(old_content, new_content) # replace all occurrences
            lines[index] = line

        os.remove(file_name) # remove file
        file = open(file_name, "x") # create file (delete content)
        file.close() # close file

        file = open(file_name, "a+") # open for writing
        [file.write(line) for line in lines] # rewrite the modified content
        file.close() # close for writing

        print(f"{file_name}'s content successfully changed") # if everything is successful, this will show on the console

    except FileNotFoundError:
        print("An error occurred", "# replacing content")


def delete_file(file_name, *args): # *args is in case we receive more than one parameter
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File {file_name} was removed") # this will show on the console, if the file is removed successfully
    else:
        print("An error occurred", "# Cannot delete file that does not exist") # If the file does not exists


operations = {
    "Create": create_file,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file
}

command = input()
while command != "End":

    operation, name_of_file, *more_content = command.split("-")

    operations[operation](name_of_file, *more_content)

    time.sleep(0.1) # using time.sleep, so the output will be ordered, otherwise it somehow gets mixed up

    command = input()
