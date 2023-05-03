"""
    Menu
"""
# pylint: disable=import-error
from utilities import clear_terminal
class Menu:
    """
    Class for Menu handle and displaying
    """
    def __init__(self):
        self.option_input = ""
        self.name_input = ""

    def main_menu(self):
        """
        This function displays a main menu with three options: singleplayer, multiplayer, and exit game.
        It then waits for the user to input a valid option and returns the user's input.
        """
        self.option_input = ""
        while self.option_input not in ("1", "2", "3"):
            clear_terminal()
            print("Main Menu:")
            print("1. Singleplayer")
            print("2. Multiplayer")
            print("3. Exit Game")
            self.option_input = input("\nEnter your choice: ")
        clear_terminal()
        return self.option_input



    def game_menu(self):
        """
        This function displays a game menu with three options: starting a new game, loading a saved game, or returning to the main menu.
        It prompts the user to enter their choice and returns it.
        """
        self.option_input = ""
        while self.option_input not in ("1", "2", "3"):
            clear_terminal()
            print("Main Menu:")
            print("1. New Game")
            print("2. Load Game")
            print("3. Back to Main Menu")
            self.option_input = input("\nEnter your choice: ")
        clear_terminal()
        return self.option_input

    def enter_player_name(self, player):
        """
        This function prompts the user to enter a player name and returns the name as a string.
        It also validates that the name entered contains at least 3 characters.
        The function takes in an integer parameter "player" to determine if it is player 1 or player 2 entering their name.
        """
        self.name_input = ""
        if player == 1:
            player_number = "Player 1"
        else:
            player_number = "Player 2"
        first_loop_round = True
        while len(self.name_input) < 3:
            clear_terminal()
            if first_loop_round:
                first_loop_round = False
            else:
                print("Name must contain at least 3 characters!")
            self.name_input = input(f"{player_number} enter your name: ")

        return self.name_input
