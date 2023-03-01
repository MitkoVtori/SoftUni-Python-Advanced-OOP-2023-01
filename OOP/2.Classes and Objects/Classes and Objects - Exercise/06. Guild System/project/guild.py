from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        player = [name for name in self.players if name.name == player_name]

        if player:
            player[0].guild = "Unaffiliated"
            self.players.remove(player[0])
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players = '\n'.join([player.player_info() for player in self.players])
        return f"Guild: {self.name}\n{players}"


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
