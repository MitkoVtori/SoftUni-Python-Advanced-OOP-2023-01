from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))

owned_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

while textiles and medicaments:
    textile, medicament = textiles.popleft(), medicaments.pop()
    textile_medicaments_sum = textile + medicament

    match = False

    for item in items.keys():
        if textile_medicaments_sum == items[item]:
            owned_items[item] += 1
            match = True
            break

    if not match:
        if textile_medicaments_sum > items["MedKit"]:
            owned_items["MedKit"] += 1
            if medicaments:
                medicament = medicaments.pop()
                medicament += textile_medicaments_sum - items["MedKit"]
                medicaments.append(medicament)

        else:
            medicament += 10
            medicaments.append(medicament)

if medicaments and not textiles:
    print("Textiles are empty.")

elif textiles and not medicaments:
    print("Medicaments are empty.")

else:
    print("Textiles and medicaments are both empty.")

items_amount = sorted(owned_items.items(), key=lambda x: (-x[1], x[0]))

for item_amount in items_amount:
    item, amount = item_amount

    if amount > 0:
        print(f"{item} - {amount}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(num) for num in list(medicaments)[::-1]])}")

if textiles:
    print(f"Textiles left: {', '.join([str(num) for num in textiles])}")
