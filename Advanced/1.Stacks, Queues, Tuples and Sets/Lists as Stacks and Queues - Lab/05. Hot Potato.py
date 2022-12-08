players = input().split()

toss = int(input())
number = toss
kid_index = -1

while len(players) != 1:

    kid_index += 1
    number -= 1

    if kid_index >= len(players):
        kid_index = 0

    if number == 0:
        kid_name = players.pop(kid_index)
        kid_index -= 1
        number = toss
        print(f"Removed {kid_name}")

print(f"Last is {players[0]}")