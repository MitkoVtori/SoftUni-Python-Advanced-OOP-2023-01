parking_lot = set()

commands = int(input())

for command in range(commands):
    in_out, car_number = input().split(', ')

    if in_out == 'OUT' and car_number in parking_lot:
        parking_lot.remove(car_number)

    elif in_out == 'IN':
        parking_lot.add(car_number)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")