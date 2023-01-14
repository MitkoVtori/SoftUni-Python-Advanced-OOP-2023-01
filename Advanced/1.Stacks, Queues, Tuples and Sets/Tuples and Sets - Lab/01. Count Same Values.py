numbers = tuple(map(float, input().split()))
used_numbers = set()

for num in numbers:
    if num not in used_numbers:
        print(f"{num:.1f} - {numbers.count(num)} times")
        used_numbers.add(num)