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
curr_game_players = []
ready_teams = []

#Pairs of Similar Teams
completed_games = []

def randomly_generate_players(num_to_make=1):
    "Number of RNG players to make."
    count = 0
    while count < num_to_make:
        player_number = random.randint(0, 99999999999)
        latest_player = {}
        latest_player["name"] = "Player" + str(player_number)
        latest_player["playerLevel"] = random.randint(1, 500)
        latest_player["latency"] = random.randint(1, 1000)
        PLAYERS.append(latest_player)
        count += 1
    print("%s players were added to the pool." % num_to_make)

def add_players_to_game():
    """PLAYER DATA to PLAYER Class"""
    for curr_player in PLAYERS:
        curr_game_players.append(
            player.Player(
                curr_player["name"],
                curr_player["playerLevel"],
                curr_player["latency"]
            ))

def add_heroes_to_game():
    """HERO Data to Hero Class"""
    for curr_hero in HEROES:
        curr_game_heroes.append(hero.Hero(curr_hero["name"], curr_hero["type"], curr_hero["unique"]))

def players_set_heroes(player_list):
    """Randomly assign heroes to players"""
    for player_in_list in player_list:
        player_in_list.set_hero(curr_game_heroes[random.randint(0, len(curr_game_heroes) - 1)])

def set_rules():
    """Add special rules to matchmaking"""
    # Two Supporters at most per Team
    # At most One Special Per Team

def assemble_team():
    "Make a balanced team"
    newest_team = team.Team()
    cycle_count = 0
    cycle_limit = 300
    while not newest_team.is_full():
        newest_player = curr_game_players[random.randint(0, len(curr_game_players) - 1)]
        if newest_team.is_valid_player_addition(newest_player):
            newest_team.add_player(newest_player)

        cycle_count += 1
        if cycle_count >= cycle_limit:
            return print("Assemble_team is stuck in an infinite loop.")

    return newest_team

def matchmaking():
    """Do matching for teams"""
    print_team_composition(assemble_team())
    print_team_composition(assemble_team())

def print_team_composition(denoted_team):
    "Prints heroes and team level."
    print("--------------------------------------------------")
    print("Team Level: %s\n" % denoted_team.get_team_level())
    print(denoted_team.get_team_composition())
    for team_hero in denoted_team.get_heroes():
        print("%s | %s" % (team_hero.get_name(), team_hero.get_role()))
    print("--------------------------------------------------")

def setup_world_state():
    """Add players and heroes to game."""
    randomly_generate_players(50)
    add_heroes_to_game()
    add_players_to_game()
    players_set_heroes(curr_game_players)

def main():
    """Main"""
    setup_world_state()
    matchmaking()

main()
