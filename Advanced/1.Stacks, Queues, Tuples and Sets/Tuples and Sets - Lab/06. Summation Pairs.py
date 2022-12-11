numbers = list(map(int, input().split()))
target = int(input())

summations = []
indexes = set()

for index, number_one in enumerate(numbers):

    if index in indexes:
        continue

    for second_index, number_two in enumerate(numbers):

        if second_index in indexes or second_index == index or index in indexes:
            continue

        if number_one + number_two == target:

            summations.append([number_one, number_two])
            indexes.add(index)
            indexes.add(second_index)

for summation in summations:

    first_number = summation[0]
    second_number = summation[1]

    print(f'{first_number} + {second_number} = {target}')