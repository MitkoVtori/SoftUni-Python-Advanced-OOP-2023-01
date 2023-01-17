lines = int(input())

periodic_table = set()

for element in range(lines):
    chemical_elements = input().split()
    [periodic_table.add(elem) for elem in chemical_elements]

print('\n'.join(periodic_table))