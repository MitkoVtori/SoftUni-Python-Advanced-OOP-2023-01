from collections import deque

market = deque()

customer = input()
while customer != "End":
    paid = False

    if customer == "Paid":
        paid = True
        for name in range(len(market)):
            print(market.popleft())

    if not paid:
        market.append(customer)

    customer = input()

print(f"{len(market)} people remaining.")