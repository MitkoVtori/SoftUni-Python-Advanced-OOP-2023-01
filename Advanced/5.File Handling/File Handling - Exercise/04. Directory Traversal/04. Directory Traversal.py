import os


def get_files():

    if os.path.exists("directory/report.txt"): # Making sure, on second run, the report won't count itself
        os.remove("directory/report.txt")

    if os.path.exists("report.txt"): # Making sure, on second run, the report won't count itself
        os.remove("report.txt")

    path = "directory" # path
    files = os.listdir(path) # files in path/directory

    return files


def sort_files(files):

    # sort files and extensions
    extensions = set()
    for file_extension in files:
        extension = file_extension.split(".")[-1] # extension. Example: html
        extensions.add(f".{extension}") # extension with dot. Example: .html

    sorted_files = sorted(files) # -> list
    sorted_extensions = sorted(extensions) # -> list

    # create report.txt
    file1 = open("report.txt", "a+") # creating report 1
    file2 = open("directory/report.txt", "a+") # creating report 2

    # combine file with extension
    for extension in sorted_extensions:
        file1.write(f"{extension}\n")
        file2.write(f"{extension}\n")

        for file in sorted_files:
            if extension in file:
                file1.write(f"- - - {file}\n")
                file2.write(f"- - - {file}\n")

    # closing opened files
    file1.close()
    file2.close()

    return "The result from the program is saved in report.txt"


files = get_files()
print(sort_files(files))