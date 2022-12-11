def even_odd_or_equal(even: set, odd: set):

    if sum(even) == sum(odd):
        return ", ".join([str(num) for num in odd | even])

    elif sum(odd) > sum(even):
        return ", ".join([str(num) for num in odd - even])

    elif sum(even) > sum(odd):
        return ", ".join([str(num) for num in odd ^ even])


names = int(input())

even_set = set()
odd_set = set()

for row in range(1, names + 1):

    name_ascii_sum = sum([ord(char) for char in input()]) / row
    name_ascii_sum = int(name_ascii_sum)

    if name_ascii_sum % 2 == 0:
        even_set.add(name_ascii_sum)

    elif name_ascii_sum % 2 != 0:
        odd_set.add(name_ascii_sum)

print(even_odd_or_equal(even_set, odd_set))