"""Hero Module for Matchmaking"""

class Player:
    """player class for match making"""
    def __init__(self, name, player_level, latency):
        self.name = name
        self.player_level = player_level
        self.latency = latency
        self.hero = ""

    def get_hero(self):
        """Hero getter"""
        return self.hero

    def get_latency(self):
        """Get player latency"""
        return self.latency

    def get_player_level(self):
        """Get player level"""
        return self.player_level

    def set_hero(self, hero):
        """Set Hero"""
        self.hero = hero
