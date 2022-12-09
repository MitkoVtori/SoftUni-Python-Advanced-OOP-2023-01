from collections import deque

bullet_price = int(input())
size_barrel = int(input())

bullets = input().split()
bullets = deque([int(item) for item in bullets])

org_bullets = deque(bullets)

locks = input().split(' ')
locks = deque([int(item) for item in locks])

intelligence = int(input())
shoot = 0

while bullets and locks:
    
    if bullets and shoot == size_barrel:
        print(f'Reloading!')
        shoot = 0

    if bullets[-1] <= locks[0]:
        print('Bang!')
        bullets.pop()
        locks.popleft()
        shoot += 1

    else:
        print('Ping!')
        bullets.pop()
        shoot += 1

if bullets and shoot == size_barrel:
    print(f'Reloading!')
    shoot = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")

else:
    cost = (len(org_bullets) - len(bullets)) * bullet_price
    profit = intelligence - cost
    print(f"{len(bullets)} bullets left. Earned ${profit}")