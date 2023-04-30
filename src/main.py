"""
dasd
"""
import sys
import json
from game import GameSetup, Game
from menu import Menu
from utilities import clear_terminal, random_boat_setup

class Main():
    """
    dasd
    """
    def __init__(self):
        self.play = Game()
        self.game_setup = GameSetup()
        self.menu = Menu()

    def handle_main_menu(self):
        """
        dasd
        """
        player_input = self.menu.main_menu()
        if player_input == "1":
            self.handle_game_menu(1)
        if player_input == "2":
            self.handle_game_menu(2)
        if player_input == "3":
            sys.exit()
        else:
            print("ELSE")

    def handle_game_menu(self, gamemode):
        """
        dasd
        """
        player_input = self.menu.game_menu()
        if player_input == "1":
            self.start_new_game(gamemode)
            return
        if player_input == "2":
            self.load_game(gamemode)
            return
        if player_input == "3":
            return

    def start_new_game(self, gamemode):
        """
        dasd
        """
        if gamemode == 1:
            player_name_one = self.menu.enter_player_name(1)
            check, player_matrix_one = self.game_setup.setup_boats(player_name_one)
            if check is False:
                return False
            player_name_two = "Bot"
            player_matrix_two = random_boat_setup()
        if gamemode == 2:
            player_name_one = self.menu.enter_player_name(1)
            player_name_two = self.menu.enter_player_name(2)
            check, player_matrix_one = self.game_setup.setup_boats(player_name_one)
            if check is False:
                return False
            check, player_matrix_two = self.game_setup.setup_boats(player_name_two)
            if check is False:
                return False
        game_params = {
            'gamemode': gamemode,
            'player_name_one': player_name_one,
            'player_name_two': player_name_two,
            'player_matrix_one': player_matrix_one,
            'player_matrix_two': player_matrix_two,
            'starting_player': 1
        }
        self.start_game(game_params)
        return True

    def load_game(self, gamemode):
        """
        dasd
        """





    def start_game(self, game_params):
        """
        Start a game with the given parameters.
        """
        if game_params['gamemode'] == 1:
            self.play.singleplayer(game_params['player_name_one'], game_params['player_name_two'],
                                game_params['player_matrix_one'], game_params['player_matrix_two'])
        elif game_params['gamemode'] == 2:
            self.play.multiplayer(game_params['player_name_one'], game_params['player_name_two'],
                                game_params['player_matrix_one'], game_params['player_matrix_two'])

# main = Main()
# while True:
#     main.handle_main_menu()
