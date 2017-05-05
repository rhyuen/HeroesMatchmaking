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

    def get_team_composition(self):
        "As name suggests.  Returns Dict with Team Composition"
        role_distro = {}
        for curr_hero in self.get_heroes():
            if curr_hero.get_role() in role_distro:
                role_distro[str(curr_hero.get_role())] += 1
            else:
                role_distro[str(curr_hero.get_role())] = 1
        return role_distro

    def has_unique_hero(self):
        """Checks if team has a unique hero"""
        for curr_hero in self.get_heroes():
            if curr_hero.is_unique():
                return True
        return False

    def is_valid_player_addition(self, potential_player):
        """Returns True if new player fits team.  True if Yes, False otherwise"""
        return not (self.has_unique_hero() and potential_player.get_hero().is_unique())

    def has_enough_support(self, potential_support, min_support=1, max_support=2):
        "Returns Bool on whether or not team has enough support"
        curr_team_composition = self.get_team_composition()
        return False

    def is_full(self):
        "Checks if team has 5 players or not."
        return len(self.players) == 5

    def add_player(self, player):
        "Add player to team"
        for curr_hero in self.get_heroes():
            if curr_hero.get_name() == player.get_hero().get_name():
                print("%s is already on the team." % player.get_hero().get_name())
                return
        self.players.append(player)
        