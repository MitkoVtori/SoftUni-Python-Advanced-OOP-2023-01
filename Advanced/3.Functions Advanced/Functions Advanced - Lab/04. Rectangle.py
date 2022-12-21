def rectangle(length, width):
    if type(length) is not int or type(width) is not int:
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return length * 2 + width * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


# print(rectangle(2, 10))
# print(rectangle('2', 10))
