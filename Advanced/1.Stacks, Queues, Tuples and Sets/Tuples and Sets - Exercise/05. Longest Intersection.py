lines = int(input())

max_intersection = 0

longest_intersection = set()
first_set = set()
second_set = set()

for index in range(lines):

    intersections = input().split("-")

    range_1 = [int(num) for num in intersections[0].split(",")]
    range_2 = [int(num) for num in intersections[1].split(",")]

    for number in range(range_1[0], range_1[1] + 1):
        first_set.add(number)

    for number in range(range_2[0], range_2[1] + 1):
        second_set.add(number)

    sets_intersection = first_set.intersection(second_set)

    if len(sets_intersection) > max_intersection:

        max_intersection = len(sets_intersection)
        longest_intersection = sets_intersection

    first_set.clear()
    second_set.clear()

print(f"Longest intersection is {[num for num in longest_intersection]} with length {max_intersection}")