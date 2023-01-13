from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))
too_many_orders = False

print(max(orders))

for order in range(len(orders)):
    if food_quantity - orders[0] >= 0:
        food_quantity -= orders.popleft()

    else:
        too_many_orders = True
        print("Orders left:", ' '.join([str(order) for order in orders]))
        break

if not too_many_orders:
    print('Orders complete')