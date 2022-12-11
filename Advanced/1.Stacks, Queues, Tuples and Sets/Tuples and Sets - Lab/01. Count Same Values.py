nums = [float(num) for num in input().split()]

numbers = tuple(nums)

checked_numbers = []

for num in numbers:
    if num not in checked_numbers:
        checked_numbers.append(num)
        print(f"{num:.1f} - {numbers.count(num)} times")