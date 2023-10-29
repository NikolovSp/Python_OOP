from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            #player.guild comes from the other class/py where self.name is from this class

            return f"Player {player.name} is already in the guild."

        if player.guild != Player.DEFAULT_GUILD:

            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        try:
            player_ = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            #filter is empty, meaning there is an error

            return f"Player {player_name} is not in the guild."

        self.players.remove(player_)
        player.guild = Player.DEFAULT_GUILD

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join([p.player_info() for p in self.players])

        return (f"Guild: {self.name}\n"
                f"{players_info}")

