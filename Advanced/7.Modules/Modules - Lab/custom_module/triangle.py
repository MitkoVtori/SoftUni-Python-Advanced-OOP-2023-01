def triangle(number):
    for row in range(1, number + 2):
        result = []

        for num in range(1, row):
            result.append(str(num))

        print(' '.join(result))

    for row in range(number, 0, -1):
        result = []

        for num in range(1, row):
            result.append(str(num))

        print(' '.join(result))