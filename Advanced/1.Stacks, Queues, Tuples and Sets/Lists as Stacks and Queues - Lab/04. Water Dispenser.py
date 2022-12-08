from collections import deque

people_waiting = deque()

water_in_dispenser = int(input())

name = input()
while name != "Start":
    people_waiting.append(name)
    name = input()

command = input()
while command != "End":

    current_command = command.split()

    if current_command[0].isdigit():
        liters = int(current_command[0])
        if liters <= water_in_dispenser:
            water_in_dispenser -= liters
            print(f"{people_waiting.popleft()} got water")
        elif liters > water_in_dispenser:
            print(f"{people_waiting.popleft()} must wait")

    elif current_command[0] == "refill":
        liters = int(current_command[1])
        water_in_dispenser += liters

    command = input()

print(f"{water_in_dispenser} liters left")