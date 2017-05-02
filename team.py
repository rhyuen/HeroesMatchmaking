"""Team module for MatchMaking"""

class Team:
    "Team class.  Composed of players."
    def __init__(self):
        self.players = []

    def get_heroes(self):
        """Returns list of heroes on team"""
        return self.players

    def get_team_level(self):
        """Adds all members levels together"""
        agg_team_level = 0
        for player in self.players:
            agg_team_level += player.get_player_level()
        return agg_team_level

    def is_full(self):
        "Checks if team has 5 players or not."
        return len(self.players) == 5

    def add_player(self, player):
        "Add player to team"
        self.players.append(player)

