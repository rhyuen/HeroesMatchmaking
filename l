[1mdiff --git a/beginmatch.py b/beginmatch.py[m
[1mindex c2d592c..b2b84e9 100644[m
[1m--- a/beginmatch.py[m
[1m+++ b/beginmatch.py[m
[36m@@ -3,7 +3,6 @@[m [mimport hero[m
 import player[m
 import team[m
 [m
[31m-[m
 PLAYERS = [[m
     {"name": "PlayerOne", "playerLevel": 14, "latency": 29},[m
     {"name": "PlayerTwo", "playerLevel": 450, "latency": 12},[m
[36m@@ -54,20 +53,34 @@[m [mHEROES = [[m
 ][m
 [m
 curr_game_heroes = [][m
[31m-curr_game_teams = [][m
 curr_game_players = [][m
[32m+[m[32mready_teams = [][m
[32m+[m
[32m+[m[32m#Pairs of Similar Teams[m
 completed_games = [][m
 [m
[31m-def set_rules():[m
[31m-    """Add special rules to matchmaking"""[m
[32m+[m[32mdef randomly_generate_players(num_to_make = 1):[m
[32m+[m[32m    "Number of RNG players to make."[m
[32m+[m[32m    count = 0[m
[32m+[m[32m    while count < num_to_make:[m
[32m+[m[32m        player_number = random.randint(0, 99999999999)[m
[32m+[m[32m        latest_player = {}[m
[32m+[m[32m        latest_player["name"] = "Player" + str(player_number)[m
[32m+[m[32m        latest_player["playerLevel"] = random.randint(1, 500)[m
[32m+[m[32m        latest_player["latency"] = random.randint(1, 1000)[m
[32m+[m[32m        PLAYERS.append(latest_player)[m
[32m+[m[32m        count += 1[m
[32m+[m[32m    print("%s players were added to the pool." % num_to_make)[m
 [m
 def add_players_to_game():[m
     """PLAYER DATA to PLAYER Class"""[m
     for curr_player in PLAYERS:[m
         curr_game_players.append([m
             player.Player([m
[31m-                curr_player["name"], curr_player["playerLevel"], curr_player["latency"][m
[31m-                ))[m
[32m+[m[32m                curr_player["name"],[m
[32m+[m[32m                curr_player["playerLevel"],[m
[32m+[m[32m                curr_player["latency"][m
[32m+[m[32m            ))[m
 [m
 def add_heroes_to_game():[m
     """HERO Data to Hero Class"""[m
[36m@@ -76,28 +89,38 @@[m [mdef add_heroes_to_game():[m
 [m
 def players_set_heroes(player_list):[m
     """Randomly assign heroes to players"""[m
[31m-    for listplayer in player_list:[m
[31m-        listplayer.set_hero(curr_game_heroes[random.randint(0, len(curr_game_heroes))])[m
[32m+[m[32m    count = 0[m
[32m+[m[32m    for player_in_list in player_list:[m
[32m+[m[32m        print(count)[m
[32m+[m[32m        count += 1[m
[32m+[m[32m        player_in_list.set_hero(curr_game_heroes[random.randint(0, len(curr_game_heroes) - 1)])[m
[32m+[m
[32m+[m[32mdef set_rules():[m
[32m+[m[32m    """Add special rules to matchmaking"""[m
[32m+[m[32m    # Two Supporters at most per Team[m
[32m+[m[32m    # At most One Special Per Team[m
[32m+[m
 [m
 [m
 def matchmaking():[m
     """Do matching for teams"""[m
[31m-    teamOne = team.Team()[m
[31m-    teamTwo = team.Team()[m
[31m-    while (not teamOne.is_full()) and (not teamTwo.is_full()):[m
[31m-        teamOne.add_player(curr_game_players[random.randint(0, 9)])[m
[31m-        teamTwo.add_player(curr_game_players[random.randint(0, 9)])[m
[31m-    print("done")[m
[31m-    print(teamOne)[m
[31m-    print(teamTwo)[m
[32m+[m[32m    team_one = team.Team()[m
[32m+[m[32m    team_two = team.Team()[m
[32m+[m[32m    while (not team_one.is_full()) and (not team_two.is_full()):[m
[32m+[m[32m        team_one.add_player(curr_game_players[random.randint(0, len(curr_game_players) - 1)])[m
[32m+[m[32m        team_two.add_player(curr_game_players[random.randint(0, len(curr_game_players) - 1)])[m
[32m+[m[32m    print_team_composition(team_one)[m
[32m+[m[32m    print_team_composition(team_two)[m
 [m
 def print_team_composition(denoted_team):[m
     "Prints heroes and team level."[m
[31m-    print(denoted_team.get_team_level())[m
[31m-    print(denoted_team.get_heroes())[m
[32m+[m[32m    print("Team Level: %s\n" % denoted_team.get_team_level())[m
[32m+[m[32m    for team_hero in denoted_team.get_heroes():[m
[32m+[m[32m        print(team_hero.get_name())[m
 [m
 def setup():[m
     """Setup matching state"""[m
[32m+[m[32m    randomly_generate_players(50)[m
     add_heroes_to_game()[m
     add_players_to_game()[m
     players_set_heroes(curr_game_players)[m
[1mdiff --git a/team.py b/team.py[m
[1mindex 4477ab6..af6e414 100644[m
[1m--- a/team.py[m
[1m+++ b/team.py[m
[36m@@ -7,7 +7,10 @@[m [mclass Team:[m
 [m
     def get_heroes(self):[m
         """Returns list of heroes on team"""[m
[31m-        return self.players[m
[32m+[m[32m        team_heroes = [][m
[32m+[m[32m        for curr_player in self.players:[m
[32m+[m[32m            team_heroes.append(curr_player.get_hero())[m
[32m+[m[32m        return team_heroes[m
 [m
     def get_team_level(self):[m
         """Adds all members levels together"""[m
[36m@@ -22,5 +25,8 @@[m [mclass Team:[m
 [m
     def add_player(self, player):[m
         "Add player to team"[m
[32m+[m[32m        for curr_hero in self.get_heroes():[m
[32m+[m[32m            if curr_hero.get_name() == player.get_hero().get_name():[m
[32m+[m[32m                print("%s is already on the team." % player.get_hero().get_name())[m
         self.players.append(player)[m
 [m
