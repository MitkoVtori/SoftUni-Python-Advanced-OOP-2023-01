from collections import deque

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = deque(map(int, input().split(", ")))

bombs_pouch = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

bombs = {
    "Cherry Bombs": 60,
    "Datura Bombs": 40,
    "Smoke Decoy Bombs": 120
}

while bomb_effects and bomb_casings:

    if len([bomb for bomb in bombs_pouch.keys() if bombs_pouch[bomb] >= 3]) == 3:
        break

    effect, casing = bomb_effects.popleft(), bomb_casings.pop()

    while effect >= 0 and casing >= 0:

        have_bomb = False

        for bomb in bombs:

            if effect + casing == bombs[bomb]:

                bombs_pouch[bomb] += 1
                have_bomb = True

                break

        if have_bomb:
            break

        casing -= 5

if len([bomb for bomb in bombs_pouch.keys() if bombs_pouch[bomb] >= 3]) == 3:
    print("Bene! You have successfully filled the bomb pouch!")

else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(eff) for eff in bomb_effects])}")

else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(cass) for cass in bomb_casings])}")

else:
    print("Bomb Casings: empty")

[print(f"{bomb}: {amount}") for bomb, amount in bombs_pouch.items()]
