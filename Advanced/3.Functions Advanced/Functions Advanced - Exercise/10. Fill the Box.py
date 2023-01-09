def fill_the_box(*args):
    height, length, width, *data = args
    size_of_the_box = height * length * width
    no_free_space = 0

    for symbol in data:

        if symbol == "Finish":
            break

        if size_of_the_box - symbol <= 0:
            symbol -= size_of_the_box
            size_of_the_box = 0

        if size_of_the_box > 0:
            size_of_the_box -= symbol

        else:
            no_free_space += symbol

    if size_of_the_box > 0:
        return f"There is free space in the box. You could put {size_of_the_box} more cubes."

    return f"No more free space! You have {no_free_space} more cubes."


''' TESTS '''
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
