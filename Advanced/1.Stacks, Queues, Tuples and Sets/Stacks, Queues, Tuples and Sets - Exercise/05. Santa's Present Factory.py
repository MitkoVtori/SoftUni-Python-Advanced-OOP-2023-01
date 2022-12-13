from collections import deque

boxes_with_materials = [int(num) for num in input().split()]
magic_values = deque(int(num) for num in input().split())

presents = {
    "Bicycle": [0, 400],
    "Doll": [0, 150],
    "Teddy bear": [0, 300],
    "Wooden train": [0, 250]
}

while boxes_with_materials and magic_values:
    material = boxes_with_materials.pop()
    magic = magic_values.popleft()

    if material == 0 and magic == 0:
        continue

    if material == 0:
        magic_values.appendleft(magic)
        continue

    if magic == 0:
        boxes_with_materials.append(material)
        continue

    product_of_operation = material * magic
    if product_of_operation < 0:
        result = material + magic
        boxes_with_materials.append(result)

    else:
        found_present = False
        for gift, data in presents.items():
            _, magic_level = data
            if magic_level == product_of_operation:
                presents[gift][0] += 1
                found_present = True
                break
        if product_of_operation > 0 and not found_present:
            boxes_with_materials.append(material + 15)

if (presents["Bicycle"][0] >= 1 and presents["Teddy bear"][0] >= 1) or \
        (presents["Doll"][0] >= 1 and presents["Wooden train"][0] >= 1):
    print(f"The presents are crafted! Merry Christmas!")

else:
    print(f"No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join(str(num) for num in boxes_with_materials[::-1])}")

if magic_values:
    print(f"Magic left: {', '.join(str(num) for num in magic_values)}")

for gift, data in presents.items():
    amount, _ = data
    if amount >= 1:
        print(f"{gift}: {amount}")