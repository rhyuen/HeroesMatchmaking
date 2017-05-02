
class Game:
    """Game"""
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def are_team_skills_even(self, stdev=10):
        "Checks if Team Levels are about equal."
        diff = abs(self.team_one.get_team_level() - self.team_two.get_team_level())
        return diff <= stdev


        