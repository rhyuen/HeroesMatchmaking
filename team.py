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
                role_distro[curr_hero.get_role()] += 1
            else:
                role_distro[curr_hero.get_role()] = 1
        return role_distro

    def has_unique_hero(self):
        """Checks if team has a unique hero"""
        for curr_hero in self.get_heroes():
            if curr_hero.is_unique():
                return True
        return False

    def is_valid_player_addition(self, potential_player):
        """Returns True if new player fits team.  True if Yes, False otherwise"""
        if self.is_duplicate(potential_player):
            return False
        if self.has_unique_hero() and potential_player.get_hero().is_unique():
            return False
        #Makes Sure Not Too much Support is Added
        if self.has_enough_support() and (potential_player.get_hero().get_role() == "Support"):
            return False
        if len(self.players) == 4:
            if not self.has_support() and potential_player.get_hero().get_role() == "Support":
                return True
            elif not self.has_warrior() and potential_player.get_hero().get_role() == "Warrior":
                return True
            else:
                return False
        return True


    def has_enough_support(self):
        "Returns Bool on whether or not team has enough support"
        max_support = 2
        curr_team_composition = self.get_team_composition()
        if "Support" not in curr_team_composition:
            return False
        return not curr_team_composition.get("Support") < max_support


    def has_support(self):
        "Checks if teams has support."
        for curr_hero in self.get_heroes():
            if curr_hero.get_role() == "Support":
                return True
        return False

    def has_warrior(self):
        "Checks if team has a tank."
        for curr_hero in self.get_heroes():
            if curr_hero.get_role() == "Warrior":
                return True
        return False


    def is_full(self):
        "Checks if team has 5 players or not."
        return len(self.players) == 5

    def is_duplicate(self, potential_player):
        "No doubles"
        for curr_hero in self.get_heroes():
            if curr_hero.get_name() == potential_player.get_hero().get_name():
                print("%s is already on the team." % potential_player.get_hero().get_name())
                return True
        return False

    def is_cho_or_gall(self):
        "Cho/gall cannot be added as the last player.  If Ch/Ga added, other must be added next."

    def add_player(self, player):
        "Add player to team"
        print("%s added." % player.get_hero().get_name())
        self.players.append(player)
