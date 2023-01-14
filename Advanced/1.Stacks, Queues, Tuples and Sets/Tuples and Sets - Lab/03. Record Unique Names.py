names = int(input())

unique_names = set()

for curr_name in range(names):
    name = input()
    unique_names.add(name)

print('\n'.join(unique_names))


# names = set([input() for name in range(int(input()))])
# print('\n'.join(names))


# print('\n'.join(set([input() for name in range(int(input()))])))
