from collections import deque

bowls_of_ramen = deque(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while bowls_of_ramen and customers:
    ramen, customer = bowls_of_ramen.pop(), customers.popleft()

    if ramen > customer:
        ramen -= customer
        bowls_of_ramen.append(ramen)

    elif customer > ramen:
        customer -= ramen
        customers.appendleft(customer)


if not customers:
    print("Great job! You served all the customers.")

    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(num) for num in bowls_of_ramen])}")

elif customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(num) for num in customers])}")
