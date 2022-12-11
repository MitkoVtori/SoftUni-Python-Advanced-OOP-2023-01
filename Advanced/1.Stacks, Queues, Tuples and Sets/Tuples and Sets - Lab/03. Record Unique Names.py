names = int(input())

unique_names = set()

for person in range(names):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)
