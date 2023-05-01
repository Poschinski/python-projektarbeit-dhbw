"""
dasd
"""
import sys
import json
from game import GameSetup, Game
from menu import Menu
from utilities import random_boat_setup


class Main():
    """
    Class for combining the other classes to a playable game.
    """

    def __init__(self):
        self.play = Game()
        self.game_setup = GameSetup()
        self.menu = Menu()

    def handle_main_menu(self):
        """
        This function handles the main menu of the game and based on the user's input,
        it calls the appropriate function to handle the game menu or exits the game.
        """
        player_input = self.menu.main_menu()
        if player_input == "1":
            self.handle_game_menu(1)
        if player_input == "2":
            self.handle_game_menu(2)
        if player_input == "3":
            sys.exit()

    def handle_game_menu(self, gamemode):
        """
        handles the user input for the game menu and calls appropriate functions based on the user's choice.
        It can start a new game, load a saved game, or exit the game.
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
        This function starts a new game based on the selected game mode.
        It prompts the user(s) to enter their names and set up their boats on their game boards.
        It then initializes the game parameters and starts the game
        """
        if gamemode == 1:
            player_name_one = self.menu.enter_player_name(1)
            check, player_matrix_one = self.game_setup.setup_boats(
                player_name_one)
            if check is False:
                return False
            player_name_two = "Bot"
            player_matrix_two = random_boat_setup()
        if gamemode == 2:
            player_name_one = self.menu.enter_player_name(1)
            player_name_two = self.menu.enter_player_name(2)
            check, player_matrix_one = self.game_setup.setup_boats(
                player_name_one)
            if check is False:
                return False
            check, player_matrix_two = self.game_setup.setup_boats(
                player_name_two)
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
        Load saved game data for the specified game mode from the JSON file and return as a dictionary.
        If no saved game data is found, print 'No saved game found' and return an empty dictionary.
        """
        try:
            with open('save.json', 'r', encoding='utf-8') as file:
                game_data_list = json.load(file)
            for game_data in game_data_list:
                if game_data['gamemode'] == gamemode:
                    self.start_game(game_data)
                    return
        except FileNotFoundError:
            print('No saved game found')
            return
        except json.JSONDecodeError:
            print('Saved game file is empty or corrupted')
            return
        finally:
            print('Error loading saved game')
        return

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

    def main(self):
        """
        This function is the main loop of the game.
        It continuously calls the handle_main_menu() function until the game is exited.
        """
        while True:
            self.handle_main_menu()


if __name__ == '__main__':
    main = Main()
    main.main()
