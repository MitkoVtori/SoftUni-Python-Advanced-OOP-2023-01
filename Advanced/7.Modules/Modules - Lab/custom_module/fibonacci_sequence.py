sequence = [0, 1]


def create_sequence(number):
    global sequence

    if number == 0:
        sequence = []

    elif number == 1:
        sequence = [0]

    else:

        sequence = [0, 1]

        for _ in range(2, number):
            sequence.append(sequence[-1] + sequence[-2])

    return ' '.join([str(num) for num in sequence])


def locate(x):

    if x in sequence:
        return f"The number - {x} is at index {sequence.index(x)}"
    return f"The number {x} is not in the sequence"

