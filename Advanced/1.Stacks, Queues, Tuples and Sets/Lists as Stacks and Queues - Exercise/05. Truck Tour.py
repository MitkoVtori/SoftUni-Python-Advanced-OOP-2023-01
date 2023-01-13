from collections import deque

number_petrol_pumps = int(input())
pumps = deque()

for pump in range(number_petrol_pumps):
    pumps.append([int(num) for num in input().split()])

for attempt in range(number_petrol_pumps):

    trunk = 0
    failed_attempt = False

    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed_attempt = True
            break

    if failed_attempt:
        pumps.append(pumps.popleft())

    elif not failed_attempt:
        print(attempt)
        break
