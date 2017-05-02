import random
import hero
import player
import team


PLAYERS = [
    {"name": "PlayerOne", "playerLevel": 14, "latency": 29},
    {"name": "PlayerTwo", "playerLevel": 450, "latency": 12},
    {"name": "PlayerThree", "playerLevel": 999, "latency": 250},
    {"name": "PlayerFour", "playerLevel": 15, "latency": 76},
    {"name": "PlayerFive", "playerLevel": 1, "latency": 44},
    {"name": "PlayerSix", "playerLevel": 0, "latency": 5000},
    {"name": "PlayerSeven", "playerLevel": 55, "latency": 400},
    {"name": "PlayerEight", "playerLevel": 767, "latency": 99},
    {"name": "PlayerNine", "playerLevel": 540, "latency": 29},
    {"name": "PlayerTen", "playerLevel": 113, "latency": 19}
]

HEROES = [
    {"name": "Thrall", "type": "Assassin", "unique": False},
    {"name": "Abathur", "type": "Specialist", "unique": True},
    {"name": "ETC", "type": "Warrior", "unique": False},
    {"name": "Artanis", "type": "Warrior", "unique": False},
    {"name": "Probius", "type": "Specialist", "unique": True},
    {"name": "The Lost Vikings", "type": "Specialist", "unique": True},
    {"name": "Murky", "type": "Specialist", "unique": True},
    {"name": "Nazeebo", "type": "Specialist", "unique": False},
    {"name": "Sylvanas", "type": "Specialist", "unique": False},
    {"name": "Sgt. Hammer", "type": "Specialist", "unique": False},
    {"name": "Xul", "type": "Specialist", "unique": False},
    {"name": "Medivh", "type": "Specialist", "unique": False},
    {"name": "Zagara", "type": "Specialist", "unique": False},
    {"name": "Lili", "type": "Support", "unique": False},
    {"name": "Jaina", "type": "Assassin", "unique": False},
    {"name": "Kaelthas", "type": "Assassin", "unique": False},
    {"name": "Rehgar", "type": "Support", "unique": False},
    {"name": "Auriel", "type": "Support", "unique": False},
    {"name": "Uther", "type": "Support", "unique": False},
    {"name": "Tyrande", "type": "Support", "unique": False},
    {"name": "Lucio", "type": "Support", "unique": False},
    {"name": "Lt. Morales", "type": "Support", "unique": False},
    {"name": "Tassadar", "type": "Support", "unique": False},
    {"name": "Li-Ming", "type": "Assassin", "unique": False},
    {"name": "Tyrael", "type": "Warrior", "unique": False},
    {"name": "Diablo", "type": "Warrior", "unique": False},
    {"name": "Leoric", "type": "Warrior", "unique": False},
    {"name": "Dehaka", "type": "Warrior", "unique": False},
    {"name": "Tracer", "type": "Assassin", "unique": False},
    {"name": "Ragnaros", "type": "Assassin", "unique": False},
    {"name": "Valla", "type": "Assassin", "unique": False},
    {"name": "Nova", "type": "Assassin", "unique": False},
    {"name": "Zeratul", "type": "Assassin", "unique": False},
]

curr_game_heroes = []
curr_game_teams = []
curr_game_players = []
completed_games = []

def set_rules():
    """Add special rules to matchmaking"""

def add_players_to_game():
    """PLAYER DATA to PLAYER Class"""
    for curr_player in PLAYERS:
        curr_game_players.append(
            player.Player(
                curr_player["name"], curr_player["playerLevel"], curr_player["latency"]
                ))

def add_heroes_to_game():
    """HERO Data to Hero Class"""
    for curr_hero in HEROES:
        curr_game_heroes.append(hero.Hero(curr_hero["name"], curr_hero["type"], curr_hero["unique"]))

def players_set_heroes(player_list):
    """Randomly assign heroes to players"""
    for listplayer in player_list:
        listplayer.set_hero(curr_game_heroes[random.randint(0, len(curr_game_heroes))])


def matchmaking():
    """Do matching for teams"""
    teamOne = team.Team()
    teamTwo = team.Team()
    while (not teamOne.is_full()) and (not teamTwo.is_full()):
        teamOne.add_player(curr_game_players[random.randint(0, 9)])
        teamTwo.add_player(curr_game_players[random.randint(0, 9)])
    print("done")
    print(teamOne)
    print(teamTwo)

def print_team_composition(denoted_team):
    "Prints heroes and team level."
    print(denoted_team.get_team_level())
    print(denoted_team.get_heroes())

def setup():
    """Setup matching state"""
    add_heroes_to_game()
    add_players_to_game()
    players_set_heroes(curr_game_players)

def main():
    """Main"""
    setup()
    matchmaking()


main()