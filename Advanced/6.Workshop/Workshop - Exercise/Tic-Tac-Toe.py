from collections import deque


class TicTacToeGame:

    def __init__(self, matrix: list, board: str, players: dict, move: deque):
        self.matrix = matrix
        self.board = board
        self.players = players
        self.move = move

    def check_win(self, player):
        checks = {
            "vertical": ([-1, -1], 0),
            "horizontal": (0, [1, 1]),
            "diagonal": [(-1, -1, 1, 1), (1, -1, -1, 1)]
        }

        symbol = self.players[player]

        for row in range(3):

            for col in range(3):

                if self.matrix[row][col] == symbol:

                    winner = True
                    m_row = row

                    for num in checks["vertical"][0]:
                        try:

                            m_row += num

                            if self.matrix[m_row][col] != symbol:
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

                            if self.matrix[row][m_col] != symbol:
                                winner = False
                                break

                        except IndexError:
                            winner = False
                            break

                    if winner:
                        return True

                    if self.matrix[0][0] == symbol and self.matrix[1][1] == symbol and self.matrix[2][2] == symbol or \
                            self.matrix[0][-1] == symbol and self.matrix[1][-2] == symbol and self.matrix[2][-3] == symbol:
                        return True

        return False

    def new_position(self):
        player = self.move.popleft()

        while True:
            position = input(f"{player} choose a free position [1-9]: ")

            if position.isdigit():
                if 1 <= int(position) <= 3:
                    if self.matrix[0][int(position)-1] == 'X' or self.matrix[0][int(position)-1] == 'O':
                        print("Position is not free!")
                    else:
                        self.matrix[0][int(position)-1] = self.players[player]
                        break

                elif 4 <= int(position) <= 6:
                    if self.matrix[1][int(position)-4] == 'X' or self.matrix[1][int(position)-4] == 'O':
                        print("Position is not free!")
                    else:
                        self.matrix[1][int(position)-4] = self.players[player]
                        break

                elif 7 <= int(position) <= 9:
                    if self.matrix[2][int(position)-7] == 'X' or self.matrix[2][int(position)-7] == 'O':
                        print("Position is not free!")
                    else:
                        self.matrix[2][int(position)-7] = self.players[player]
                        break
                else:
                    print("Choose valid position [1-9]")

            else:
                print("Position must be digit between 1-9")

        print(self.edit_board())

        self.move.append(player)
        return [self.check_win(player), player]

    def draw(self):
        for row in range(3):

            for col in range(3):
                if self.matrix[row][col] == ' ':
                    return False
        return True

    def edit_board(self):
        self.board = f"| {self.matrix[0][0]} | {self.matrix[0][1]} | {self.matrix[0][2]} |\n| {self.matrix[1][0]} | {self.matrix[1][1]} | {self.matrix[1][2]} |\n| {self.matrix[2][0]} | {self.matrix[2][1]} | {self.matrix[2][2]} |"
        return self.board


def setup():
    matrix = [[' '] * 3 for _ in range(3)]
    board = "|   |   |   |\n|   |   |   |\n|   |   |   |"

    player_one = input("Player one name: ")

    while True:

        player_two = input("Player two name: ")

        if player_two != player_one:
            break

        print("Second player cannot have the same name as the first player!")

    player_one_plays_with = input(f"{player_one} would like to play with 'X' or 'O'? ").upper()

    if player_one_plays_with == "O":
        players = {player_one: "O", player_two: "X"}
        move = deque([player_two, player_one])

    else: # if player one plays with 'X' or gave invalid character
        players = {player_one: 'X', player_two: 'O'}
        move = deque([player_one, player_two])

    return [matrix, board, players, move]


def start_game(items):
    print("This is the numeration of the board:\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
    print(f"{items[-1][0]} plays with 'X', he starts first!")

    game = TicTacToeGame(*items)

    return game


def play():
    game = start_game(setup())

    while True:
        have_winner = game.new_position()

        if have_winner[0]:
            print(f"{have_winner[1]} won!")
            restart = input("type \"r\" to restart the game: ").lower()

            if restart == "r":
                play()

            else:
                break

        draw = game.draw()

        if draw:
            print("The game is draw!")
            restart = input("type \"r\" to restart the game: ").lower()

            if restart == "r":
                play()

            else:
                break


play()
