from collections import deque

green_light = int(input())
window = int(input())

cars = deque()
cars_counter = 0
crashed = False

command = input()
while command != "END":
    if command == "green":
        if cars:
            current_car = cars.popleft()
            seconds_left = green_light - len(current_car)

            while seconds_left > 0:
                cars_counter += 1

                if cars:
                    current_car = cars.popleft()
                    seconds_left -= len(current_car)

                else:
                    break

            if seconds_left == 0:
                cars_counter += 1

            if window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1

            else:
                index = window + seconds_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
    else:
        cars.append(command)

    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")