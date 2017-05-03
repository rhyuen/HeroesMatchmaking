"""Team module for MatchMaking"""

class Team:
    "Team class.  Composed of players."
    def __init__(self):
        self.players = []

    def get_heroes(self):
        """Returns list of heroes on team"""
        team_heroes = []
        for curr_player in self.players:
            team_heroes.append(curr_player.get_hero())
        return team_heroes

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
        for curr_hero in self.get_heroes():
            if curr_hero.get_name() == player.get_hero().get_name():
                print("%s is already on the team." % player.get_hero().get_name())
        self.players.append(player)

