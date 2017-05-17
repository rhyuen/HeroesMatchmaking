
class Game:
    """Game"""
    def __init__(self):
        self.teams = []

    def add_team(self, new_team):
        "Add team to game"
        if self.is_full():
            raise Exception("Team full.")
        else:
            self.teams.append(new_team)

    def is_full(self):
        "Check if team full"
        return len(self.teams) == 2
        