"Abstraction for a list of players."

class Party:
    "Contains a list of players."
    def __init__(self):
        self.players = []

    def get_players(self):
        "Gets players in Party"
        return self.players

    def is_full(self):
        "Check if party is full."
        if len(self.get_players()) >= 5:
            return True
        else:
            return False

    def add_player(self, potential_player):
        "Adds a player to party."
        if self.is_full():
            print("Party is full. 5 players.")
            return
        else:
            self.players.append(potential_player)

