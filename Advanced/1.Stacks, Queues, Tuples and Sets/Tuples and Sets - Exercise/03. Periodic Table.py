lines_with_elements = int(input())

unique_elements = set()

for elements in range(lines_with_elements):
    chemical_elements = input().split()
    [unique_elements.add(elem) for elem in chemical_elements]

print('\n'.join([element for element in unique_elements]))