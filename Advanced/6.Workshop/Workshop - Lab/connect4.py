from collections import deque


class ConnectFourGame:

    def __init__(self, field: list, players: deque):
        self.field = field
        self.players = players

    def check_win(self, player):
        checks = {
            "vertical": ([1, 1, 1], 0),
            "horizontal": (0, [1, 1, 1]),
            "diagonal": [
                ([1, 1, 1], [1, 1, 1]),
                ([1, 1, 1], [-1, -1, -1]),
                ([-1, -1, -1], [1, 1, 1]),
                ([-1, -1, -1], [-1, -1, -1])
            ]
        }

        for row in range(6):

            for col in range(7):

                if self.field[row][col] == player:

                    winner = True
                    m_row = row

                    for num in checks["vertical"][0]:
                        try:

                            m_row += num

                            if self.field[m_row][col] != player:
                                winner = False
                                break

                        except IndexError:
                            winner = False
                            break

                    if winner:
                        return True

                    winner = True
                    m_col = col

                    for num in checks["horizontal"][1]:
                        try:

                            m_col += num

                            if self.field[row][m_col] != player:
                                winner = False
                                break

                        except IndexError:
                            winner = False
                            break

                    if winner:
                        return True

                    diag_winner = False

                    for movement in checks["diagonal"]:

                        dm_row = row
                        dm_col = col

                        for index in range(3):
                            try:

                                dm_row += movement[0][index]
                                dm_col += movement[1][index]

                                if self.field[dm_row][dm_col] == player and index == 2:
                                    diag_winner = True

                                if self.field[dm_row][dm_col] != player:
                                    break

                            except IndexError:
                                break

                        if diag_winner:
                            return True

        return False

    def append_to_column(self):

        player = self.players.popleft()
        print(f"Player {player}, please choose a column")

        while True:
            column = input()

            if column.isdigit():

                if 0 < int(column) <= 7:

                    found_spot = False
                    reversed_field = self.field[::-1]

                    for row in range(6):

                        if reversed_field[row][int(column)-1] == 0:
                            found_spot = True
                            reversed_field[row][int(column)-1] = player
                            self.field = reversed_field[::-1]
                            break

                    if found_spot:
                        break

                    print("The column is full!")

                else:
                    print("Column out of range!")

            else:
                print("Column must be digit in the range 1-7")

            print(f"Player {player}, please choose a column")

        self.players.append(player)
        return [self.check_win(player), player]

    def end_game_draw(self):
        if 0 not in self.field[0]:
            return True
        return False


def start_game():
    matrix = [[0] * 7 for _ in range(6)]

    while True:
        how_many_players = input("How many players will play: ")

        if how_many_players.isdigit():
            if 1 < int(how_many_players) <= 4:
                break
            print()
            print("Minimum players must be 2, maximum players must be 4.")

        else:
            print()
            print("Players must be number")

    players = deque([num + 1 for num in range(int(how_many_players))])

    print("MAP:")
    [print(row) for row in matrix]
    print()
    print()

    play(matrix, players)


def play(matrix, players):
    game = ConnectFourGame(matrix, players)

    while True:
        have_winner = game.append_to_column()

        [print(row) for row in matrix]

        if have_winner[0]:
            print(f"The winner is player {have_winner[1]}\n")
            restart = input("type \"r\" to restart the game: ").lower()

            if restart == "r":
                start_game()

            else:
                break

        draw = game.end_game_draw()

        if draw:
            print("The game is draw!")

            restart = input("type \"r\" to restart the game: ").lower()
            if restart == "r":
                start_game()

            else:
                break


start_game()
