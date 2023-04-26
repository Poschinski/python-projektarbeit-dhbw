"""
    Code Description
"""

from utilities import clear_terminal


class Menu:
    """
    Class Description
    """

    def __init__(self):
        self.optionen = ['single player', 'multi player',
                         'ranking board', 'exit the game']
        self.single_player_options = ['New game', 'Continue', 'back']
        self.multiplayer_options = ['New game', 'Continue', 'back']

    def display(self):
        print('Welcome to battleships!')
        print('Please choose an option:')
        for i, option in enumerate(self.optionen):
            print(f'{i+1}. {option}')

    def select_option(self):
        choice = input('Your choice: ')
        while not choice.isdigit() or int(choice) not in range(1, len(self.optionen)+1):
            print(
                f'Invalid input. Please enter a number between 1 and {len(self.optionen)}.')
            choice = input('Your choice: ')
        return int(choice)

    def single_player_menu(self):
        print("single player mode selected.")
        print("Please select an option: ")
        for i, option in enumerate(self.single_player_options):
            print(f'{i+1}. {option}')
        choice = input('Your choice: ')
        while not choice.isdigit() or int(choice) not in range(1, len(self.single_player_options)+1):
            print(
                f'Invalid input. Please enter a number between 1 and {len(self.single_player_options)}.')
            choice = input('Your choice: ')
        return choice

    def multiplayer_menu(self):
        print('Multiplayer selected.')
        print('Please select an option:')
        for i, option in enumerate(self.multiplayer_options):
            print(f'{i+1}. {option}')
        choice = input('Your choice: ')
        while not choice.isdigit() or int(choice) not in range(1, len(self.multiplayer_options)+1):
            print(
                f'Invalid input. Please enter a number between 1 and {len(self.multiplayer_options)}.')
            choice = input('Your choice: ')
        return choice

    def leaderboard(self):
        print('Leaderboard selected.')

        while True:
            choice = input("Enter 'b' to go back to the main menu: ")
            if choice.lower() == 'b':
                clear_terminal()
                return  # Return from the function to go back to the main menu
            else:
                print("Invalid choice. Please enter 'b' to go back to the main menu.")

    def run(self):
        while True:
            self.display()
            selection = self.select_option()
            if selection == 1:
                clear_terminal()
                sub_selection = self.single_player_menu()
                if sub_selection == '1':
                    print('Starting new single player game.')
                    game = Game()
                    game.start_new_singleplayer_game()
                elif sub_selection == '2':
                    print('Continuing single player game.')
                    game = Game()
                    game.load_singleplayer_game()
                elif sub_selection == '3':
                    clear_terminal()

            elif selection == 2:
                clear_terminal()
                sub_selection = self.multiplayer_menu()
                if sub_selection == '1':
                    print('Starting new multiplayer game.')
                    game = Game()
                    game.start_new_multiplayer_game()
                elif sub_selection == '2':
                    print('Continuing multiplayer game.')
                    game = Game()
                    game.load_multiplayer_game()
                elif sub_selection == '3':
                    clear_terminal()
            elif selection == 3:
                clear_terminal()
                self.leaderboard()
            elif selection == 4:
                print('Exiting game...')
                clear_terminal()
                return

