from collections import deque

supermarket = deque()

command = input()
while command != "End":

    if command == "Paid":
        queue_length = len(supermarket)
        [print(supermarket.popleft()) for _ in range(queue_length)]

    else:
        supermarket.append(command)

    command = input()

print(f"{len(supermarket)} people remaining.")