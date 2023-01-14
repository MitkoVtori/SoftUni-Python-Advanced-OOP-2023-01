numbers = list(map(int, input().split()))
number_indexes = set()
target_number = int(input())

for first_index in range(len(numbers)):

    for second_index in range(len(numbers)):

        if first_index != second_index and first_index not in number_indexes and second_index not in number_indexes \
                and numbers[first_index] + numbers[second_index] == target_number:

            print(f"{numbers[first_index]} + {numbers[second_index]} = {target_number}")
            number_indexes.add(first_index), number_indexes.add(second_index)
            break



# ---- OLD ----
# numbers = list(map(int, input().split()))
# target = int(input())
#
# summations = []
# indexes = set()
#
# for index, number_one in enumerate(numbers):
#
#     if index in indexes:
#         continue
#
#     for second_index, number_two in enumerate(numbers):
#
#         if second_index in indexes or second_index == index or index in indexes:
#             continue
#
#         if number_one + number_two == target:
#
#             summations.append([number_one, number_two])
#             indexes.add(index)
#             indexes.add(second_index)
#
# for summation in summations:
#
#     first_number = summation[0]
#     second_number = summation[1]
#
#     print(f'{first_number} + {second_number} = {target}')
