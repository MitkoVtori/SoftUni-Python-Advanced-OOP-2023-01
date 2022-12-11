invited_guests = int(input())

regular_guests = set()
vip_guests = set()

for invite in range(invited_guests):
    guest_number = input()

    if len(guest_number) == 8:

        if guest_number[0].isdigit():
            vip_guests.add(guest_number)

        elif not guest_number[0].isdigit():
            regular_guests.add(guest_number)

guest = input()
while guest != "END":

    if guest in regular_guests:
        regular_guests.remove(guest)

    if guest in vip_guests:
        vip_guests.remove(guest)

    guest = input()

print(len(vip_guests) + len(regular_guests))

if vip_guests:
    vip_guests_did_not_come = sorted(list(vip_guests))
    [print(guest) for guest in vip_guests_did_not_come]

if regular_guests:
    regular_guests_did_not_come = sorted(list(regular_guests))
    [print(guest) for guest in regular_guests_did_not_come]