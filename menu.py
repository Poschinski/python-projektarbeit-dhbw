"""
sadd
"""
from utilities import clear_terminal
class Menu:
    """
    sadd
    """
    def __init__(self):
        self.option_input = ""
        self.name_input = ""

    def main_menu(self):
        """
        sadd
        """
        first_loop_round = True
        self.option_input = ""
        while self.option_input not in ("1", "2", "3"):
            clear_terminal()
            print("Main Menu:")
            print("1. Singleplayer")
            print("2. Multiplayer")
            print("3. Exit Game")
            if first_loop_round is False:
                print("Invalid input. Please try again.")
            else:
                first_loop_round = False
            self.option_input = input("\nEnter your choice: ")
        clear_terminal()
        return self.option_input



    def game_menu(self):
        """
        sadd
        """
        first_loop_round = True
        self.option_input = ""
        while self.option_input not in ("1", "2", "3"):
            clear_terminal()
            print("Main Menu:")
            print("1. New Game")
            print("2. Load Game")
            print("3. Back to Main Menu")
            if first_loop_round is False:
                print("Invalid input. Please try again.")
            else:
                first_loop_round = False
            self.option_input = input("\nEnter your choice: ")
        clear_terminal()
        return self.option_input

    def enter_player_name(self, player):
        """
        sadd
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
