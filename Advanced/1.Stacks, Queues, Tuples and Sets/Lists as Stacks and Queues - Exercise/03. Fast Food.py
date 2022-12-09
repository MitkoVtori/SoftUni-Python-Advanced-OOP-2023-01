from collections import deque

quantity_food = int(input())
orders_food_quantity = deque([int(num) for num in input().split()])

print(max(orders_food_quantity))

orders_complete = True

index = -1

while orders_food_quantity:

    index += 1
    order = orders_food_quantity[index]

    if order <= quantity_food:
        index -= 1
        quantity_food -= order
        orders_food_quantity.popleft()

    elif order > quantity_food:
        orders_complete = False
        break

if orders_complete:
    print("Orders complete")
elif not orders_complete:
    uncompleted_orders = [str(num) for num in orders_food_quantity]
    print(f"Orders left: {' '.join(uncompleted_orders)}")