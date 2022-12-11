names = int(input())

unique_usernames = {input() for username in range(names)}

[print(username) for username in unique_usernames]


# print('\n'.join({input() for username in range(int(input()))}))