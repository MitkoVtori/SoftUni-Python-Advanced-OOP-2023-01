def rhombus_stars(number):
    for row in range(number * 2 - 1):
        spaces = abs(number - row - 1)
        stars = number - spaces
        print(' ' * spaces + '* ' * stars)


num = int(input())
rhombus_stars(num)
