from collections import deque

queue = deque()

dispenser_quantity = int(input())

command = input()
while command != "Start":
    queue.append(command)
    command = input()

command = input()
while command != "End":

    if command.isdigit():
        liters = int(command)

        if liters <= dispenser_quantity:
            dispenser_quantity -= liters
            print(f"{queue.popleft()} got water")

        elif liters > dispenser_quantity:
            print(f"{queue.popleft()} must wait")

    elif command.startswith("refill"):
        liters = int(command.split()[1])
        dispenser_quantity += liters

    command = input()

print(f"{dispenser_quantity} liters left")