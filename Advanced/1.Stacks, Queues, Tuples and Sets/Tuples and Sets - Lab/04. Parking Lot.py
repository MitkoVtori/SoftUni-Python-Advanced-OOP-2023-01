directions = int(input())

cars = set()

for car_direction in range(directions):
    direction, car_number = input().split(', ')

    if direction == "IN":
        cars.add(car_number)

    else:
        cars.remove(car_number)

if cars:
    print('\n'.join(cars))

else:
    print("Parking Lot is Empty")