"Makes it go."

import random
import hero
import player
import team
import game

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
    {"name": "Abathur", "type": "Specialist", "unique": True},
    {"name": "Probius", "type": "Specialist", "unique": True},
    {"name": "The Lost Vikings", "type": "Specialist", "unique": True},
    {"name": "Murky", "type": "Specialist", "unique": True},
    {"name": "Gazlowe", "type": "Specialist", "unique": False},
    {"name": "Azmodan", "type": "Specialist", "unique": False},
    {"name": "Nazeebo", "type": "Specialist", "unique": False},
    {"name": "Sylvanas", "type": "Specialist", "unique": False},
    {"name": "Sgt. Hammer", "type": "Specialist", "unique": False},
    {"name": "Xul", "type": "Specialist", "unique": False},
    {"name": "Medivh", "type": "Specialist", "unique": False},
    {"name": "Zagara", "type": "Specialist", "unique": False},
    {"name": "Brightwing", "type": "Support", "unique": False},
    {"name": "Kharazim", "type": "Support", "unique": False},
    {"name": "Lili", "type": "Support", "unique": False},
    {"name": "Malfurion", "type": "Support", "unique": False},
    {"name": "Rehgar", "type": "Support", "unique": False},
    {"name": "Auriel", "type": "Support", "unique": False},
    {"name": "Uther", "type": "Support", "unique": False},
    {"name": "Tyrande", "type": "Support", "unique": False},
    {"name": "Lucio", "type": "Support", "unique": False},
    {"name": "Lt. Morales", "type": "Support", "unique": False},
    {"name": "Tassadar", "type": "Support", "unique": False},
    {"name": "Li-Ming", "type": "Assassin", "unique": False},
    {"name": "Arthas", "type": "Warrior", "unique": False},
    {"name": "Chen", "type": "Warrior", "unique": False},
    {"name": "ETC", "type": "Warrior", "unique": False},
    {"name": "Anub'arak", "type": "Warrior", "unique": False},
    {"name": "Artanis", "type": "Warrior", "unique": False},
    {"name": "Johanna", "type": "Warrior", "unique": False},
    {"name": "Muradin", "type": "Warrior", "unique": False},
    {"name": "Rexxar", "type": "Warrior", "unique": False},
    {"name": "Sonya", "type": "Warrior", "unique": False},
    {"name": "Stitches", "type": "Warrior", "unique": False},
    {"name": "Tyrael", "type": "Warrior", "unique": False},
    {"name": "Zarya", "type": "Warrior", "unique": False},
    {"name": "Varian", "type": "Warrior", "unique": False},
    {"name": "Diablo", "type": "Warrior", "unique": False},
    {"name": "Leoric", "type": "Warrior", "unique": False},
    {"name": "Dehaka", "type": "Warrior", "unique": False},
    {"name": "Alarak", "type": "Assassin", "unique": False},
    {"name": "Cassia", "type": "Assassin", "unique": False},
    {"name": "Chromie", "type": "Assassin", "unique": False},
    {"name": "Falstad", "type": "Assassin", "unique": False},
    {"name": "Genji", "type": "Assassin", "unique": False},
    {"name": "Guldan", "type": "Assassin", "unique": False},
    {"name": "Greymane", "type": "Assassin", "unique": False},
    {"name": "Illidan", "type": "Assassin", "unique": False},
    {"name": "Jaina", "type": "Assassin", "unique": False},
    {"name": "Kaelthas", "type": "Assassin", "unique": False},
    {"name": "Kerrigan", "type": "Assassin", "unique": False},
    {"name": "Lunara", "type": "Assassin", "unique": False},
    {"name": "Thrall", "type": "Assassin", "unique": False},
    {"name": "Tracer", "type": "Assassin", "unique": False},
    {"name": "Tychus", "type": "Assassin", "unique": False},
    {"name": "Raynor", "type": "Assassin", "unique": False},
    {"name": "Ragnaros", "type": "Assassin", "unique": False},
    {"name": "Samuro", "type": "Assassin", "unique": False},
    {"name": "Valeera", "type": "Assassin", "unique": False},
    {"name": "Butcher", "type": "Assassin", "unique": False},
    {"name": "Valla", "type": "Assassin", "unique": False},
    {"name": "Nova", "type": "Assassin", "unique": False},
    {"name": "Zeratul", "type": "Assassin", "unique": False},
    {"name": "Zul'jin", "type": "Assassin", "unique": False}
]

curr_game_heroes = []
curr_game_players = []
ready_teams = []

#Pairs of Similar Teams
completed_games = []

def randomly_generate_players(num_to_make=1):
    "Number of RNG players to make."
    count = 0
    uuid = {}
    while count < num_to_make:
        player_number = random.randint(0, num_to_make*10)
        if str(player_number) in uuid:
            print("Number already in use: %s" % player_number)
            continue
        else:
            uuid[str(player_number)] = 0

            PLAYERS.append({
                "name": "Player" + str(player_number),
                "playerLevel": random.randint(1, 500),
                "latency": random.randint(1, 1000)
            })
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

def assemble_team():
    "Make a balanced team"
    newest_team = team.Team()
    cycle_count = 0
    cycle_limit = 1000
    while not newest_team.is_full():
        newest_player = curr_game_players[random.randint(0, len(curr_game_players) - 1)]

        if cycle_count >= cycle_limit * 0.8:
            if newest_team.is_valid_player_addition(newest_player, True):
                newest_team.add_player(newest_player)
                print("Subideal addition: %s (%s)" % (newest_player.get_hero().get_name(), newest_player.get_name()))
                remove_player_from_region_pool(newest_player)
            else:
                print("Unaccounted for case.")
        else:
            if newest_team.is_valid_player_addition(newest_player):
                newest_team.add_player(newest_player)
                remove_player_from_region_pool(newest_player)

        cycle_count += 1
        if cycle_count >= cycle_limit:
            print("Assemble_team with Ideal Conditions taking too long.\n")
            print(get_unassigned_players_roles())
            # del newest_team
            return

    return newest_team

def remove_player_from_region_pool(selected_player):
    "Remove player from pool"
    curr_game_players.remove(selected_player)
    print("%s (%s) removed from region pool." % (selected_player.get_name(), selected_player.get_hero().get_name()))

# def remove_players_from_pool(remove_players_in_team):
#     "Removes players in teams from pool."
#     print(len(curr_game_players))
#     for curr_player in remove_players_in_team.get_players():
#         curr_game_players.remove(curr_player)
#         print("%s removed from pool." % curr_player.get_name())
#     print(len(curr_game_players))

"TODO: Match teams together."
"TODO: While teams are in array, keep matching."
"TODO: Return rates of matching and time to match."
"TODO: Return length of time a player is in the wait queue for."
def matchmaking():
    """Do matching for teams"""

    for num in range(3):
        print("---------------------------------")
        ready_teams.append(assemble_team())
        print("---------------------------------")
    print_global_team_levels()

def find_opponent():
    "Find opponent for matchmaking"
    return ""

def print_global_team_levels():
    "Get agg team levels for all teams"
    for index, curr_team in enumerate(ready_teams):
        print("TEAM%s: %s" % (index, curr_team.get_team_level()))


def get_all_free_class_players(class_name):
    "returns all available supports"
    if not class_name in ["Warrior", "Support", "Specialist", "Assasin"]:
        raise ValueError("%s is an invalid class name." % class_name)
    else:
        avail_class_player = []
        for curr_player in curr_game_players:
            if curr_player.get_hero().get_role() == class_name:
                avail_class_player.append(curr_player)
    return avail_class_player



def get_unassigned_players_roles():
    "returns roles of teamless players."
    teamless_player_dist = {}
    for unassigned_player in curr_game_players:
        role = unassigned_player.get_hero().get_role()
        if role in teamless_player_dist:
            teamless_player_dist[role] += 1
        else:
            teamless_player_dist[role] = 1
    return teamless_player_dist

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
    randomly_generate_players(10)
    add_heroes_to_game()
    add_players_to_game()
    players_set_heroes(curr_game_players)

def main():
    """Main"""
    setup_world_state()
    matchmaking()

main()
