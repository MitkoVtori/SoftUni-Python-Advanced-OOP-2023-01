from collections import deque

cups = deque(int(cup) for cup in input().split())
bottles = list(int(bottle) for bottle in input().split())

wasted_water = 0

while True:
    if cups and bottles:
        current_cup = cups.popleft()
        current_bottle = bottles.pop()

        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup

        else:
            cups.appendleft(current_cup - current_bottle)
    else:
        break

if cups:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")

if bottles:
    print(f"Bottles: {' '.join([str(bottle) for bottle in bottles])}")

print(f"Wasted litters of water: {wasted_water}")