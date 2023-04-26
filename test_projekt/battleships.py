"""
    Code Description
"""
import os
import keyboard

# class Singleplayer:

#     def setup_boats(self):
#         #Code for setting up the boats goas here

#     def display_board(self):

#     def play(self):


# class Multiplayer:

#     def setup_boats(self):
#         #Code for setting up the boats goes here

class Game:
    """
    Class Description
    """

    def __init__(self):
        self.board = Board()
        self.current_pos = [1, 1]
        self.current_boat = 0
        self.direction = "horizontal"

    def setup_boats(self):
        boat_lengths = [5, 4, 3, 2]
        prev_pos = None
        prev_color = None
        length = 5
        self.board.color_position(self.current_pos, length, self.direction)
        self.board.print_single_board()

        for i, length in enumerate(boat_lengths):
            for j in range(1, 6 - i):
                self.board.print_single_board()
                while True:
                    event = keyboard.read_event()
                    if event.event_type == 'down':
                        key = event.name
                        if key == "enter":
                            if self.current_boat < 4:
                                if self.board.check_valid_position(self.current_pos, length, self.direction):
                                    self.board.place_boat(
                                        self.current_pos, length, self.direction)
                                    prev_pos = None
                                    prev_color = None
                                    self.current_boat += 1
                                    break
                                else:
                                    print("Invalid position. Try again.")
                            else:
                                print("All boats placed.")
                                return
                        elif key == "shift":
                            if self.direction == "horizontal":
                                self.direction = "vertical"
                                self.board.color_position(
                                    self.current_pos, length, self.direction)
                                self.board.print_single_board()
                            else:
                                self.direction = "horizontal"
                                self.board.color_position(
                                    self.current_pos, length, self.direction)
                                self.board.print_single_board()
                        elif key == "tab":
                            self.current_boat = (self.current_boat + 1) % 4
                        elif key == "esc":
                            self.board.clear_board()
                            self.current_boat = 0
                            self.current_pos = [0, 0]
                            self.direction = "horizontal"
                            prev_pos = None
                            prev_color = None
                            break
                        elif key == "up":
                            if self.current_pos[0] > 0:
                                self.board.color_position(prev_pos, length, self.direction, prev_color)
                                prev_pos, prev_color = self.current_pos.copy(), self.board.color_position(self.current_pos, length, self.direction)
                                self.current_pos[0] -= 1
                                self.board.print_single_board()
                        elif key == "down":
                            if self.current_pos[0] < 9 - length + 1:
                                if prev_pos is not None and prev_color is not None:
                                    self.board.color_position(
                                        prev_pos, length, self.direction, prev_color)
                                prev_pos, prev_color = self.current_pos.copy(), self.board.color_position(
                                    self.current_pos, length, self.direction)
                                self.current_pos[0] += 1
                                self.board.print_single_board()
                        elif key == "left":
                            if self.current_pos[1] > 0:
                                if prev_pos is not None and prev_color is not None:
                                    self.board.color_position(
                                        prev_pos, length, self.direction, prev_color)
                                prev_pos, prev_color = self.current_pos.copy(), self.board.color_position(
                                    self.current_pos, length, self.direction)
                                self.current_pos[1] -= 1
                                self.board.print_single_board()
                        elif key == "right":
                            if self.current_pos[1] < 9 - length + 1:
                                if prev_pos is not None and prev_color is not None:
                                    self.board.color_position(
                                        prev_pos, length, self.direction, prev_color)
                                prev_pos, prev_color = self.current_pos.copy(), self.board.color_position(
                                    self.current_pos, length, self.direction)
                                self.current_pos[1] += 1
                                self.board.print_single_board()

                        else:
                            print("Invalid key. Try again.")

    def start_new_singleplayer_game(self):
        # Code to start a new single player game goes here
        print("Starting new single player game")

    def start_new_multiplayer_game(self):
        # Code to start a new multiplayer game goes here
        print("Starting new multiplayer game")

    def load_singleplayer_game(self):
        # Code to load a saved single player game goes here
        print("Loading saved single player game")

    def load_multiplayer_game(self):
        # Code to load a saved multiplayer game goes here
        print("Loading saved multiplayer game")


class MainMenu:
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
                os.system('clear')
                return  # Return from the function to go back to the main menu
            else:
                print("Invalid choice. Please enter 'b' to go back to the main menu.")

    def run(self):
        while True:
            self.display()
            selection = self.select_option()
            if selection == 1:
                os.system('clear')
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
                    os.system('clear')

            elif selection == 2:
                os.system('clear')
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
                    os.system('clear')
            elif selection == 3:
                os.system('clear')
                self.leaderboard()
            elif selection == 4:
                print('Exiting game...')
                os.system('clear')
                return


class Board:
    """
    Class Description
    """

    def __init__(self):
        self.board1 = [[' ' for i in range(13)] for j in range(12)]
        self.board2 = [[' ' for i in range(13)] for j in range(12)]
        self.color_blue = '\u001b[94;106m'
        self.color_grey = '\u001b[100m'
        self.add_column_labels()
        self.add_row_labels_and_color()

    def add_column_labels(self):
        for i, label in enumerate(['    ', '|  A ', '|  B ', '|  C ', '|  D ', '|  E ', '|  F ', '|  G ', '|  H ', '|  I ', '|  J  |']):
            self.board1[0][i] = label
            self.board2[0][i] = label
            self.sizes = [5, 4, 3, 2]
            self.num_boats = [1, 2, 3, 4]

    # color = light blue
    def add_row_labels_and_color(self, color='\u001b[94;106m'):
        for i in range(1, 11):
            # pad single-digit labels with leading zero
            row_label = '{:02d}'.format(i)
            self.board1[i][0] = '| ' + row_label + ' |'
            self.board2[i][0] = '| ' + row_label + ' |'
            for j in range(1, 11):
                # add light blue background color to box
                self.board1[i][j] = f'{color} ~ \u001b[0m |'
                # add light blue background color to box
                self.board2[i][j] = f'{color} ~ \u001b[0m |'

    # color = grey
    def color_position(self, pos, length, direction, color='\u001b[100m'):
        for i in range(length):
            if direction == "horizontal":
                # change color to grey
                self.board1[pos[0]][pos[1] + i] = f'{color}   \u001b[0m |'
            else:
                self.board1[pos[0] + i][pos[1]
                                        ] = f'{color}   \u001b[0m |'  # change color to grey
        return color
    
    def color_matrix_positions(self, matrix, grey='\u001b[100m', blue='\u001b[94;106m'):
        for i in range(1, 11):
            for j in range(1, 11):
                if matrix[i-1][j-1] == 2:
                    self.board1[i][j] = f'{grey}   \u001b[0m |'
                else:
                    self.board1[i][j] = f'{blue} ~ \u001b[0m |'


    def print_single_board(self):
        instructions = ["Use", "'Arrow keys' to move the boat,", "'Tab' to switch boat", "'Shift' to rotate the boat,",
                        "'Enter' to place the boat,", "'R' for random boat setup,", "'Esc' to reset,", "'S' to save,", "'B' to go back.", ""]
        boat_list = ['Battleship (5)', 'Cruiser (4)',
                     'Destroyer (3)', 'Submarine (2)']
        board_display = ''
        for i, row in enumerate(self.board1):
            if i == 0:
                board_display += ' \n '
                # print horizontal divider before column labels row
                board_display += '    ' + '-'*61 + '\n'
                # print column labels row and first instruction
                board_display += ' '.join(row) + '   ' + instructions[0] + '\n'
                instructions.pop(0)  # remove first instruction from list
            else:
                # print horizontal divider before current row
                board_display += '--'*33 + '\n'
                # print current row and next instruction
                board_display += ' '.join(row) + '   ' + instructions[0] + '\n'
                if len(instructions) > 1:
                    instructions.pop(0)  # remove next instruction from list

        # Add boat list and remaining boats count to bottom of display
        boat_list_display = 'Boats: '
        for i, boat in enumerate(boat_list):
            if i == len(boat_list)-1:
                boat_list_display += str(self.num_boats[i]) + 'x ' + boat
            else:
                boat_list_display += str(self.num_boats[i]
                                         ) + 'x ' + boat + ', '
        board_display += '\n' + boat_list_display + '\n'
        os.system('clear')
        print(board_display)



    def print_double_board(self):
        for i, (row1, row2) in enumerate(zip(self.board1, self.board2)):
            if i == 0:
                os.system('clear')
                print(' \n ')
                print(' ' * 8 + 'Player 1'.center(50) +
                      ' ' * 24 + 'Player 2'.center(50))
                print(' ' * 5 + '-'*61 + ' ' * 13 + '-'*61)
                print(' '.join(row1) + ' ' * 4 + ' '.join(row2))
            else:
                print('--'*33 + ' ' * 8 + '--'*33)
                print(' '.join(row1) + ' ' * 4 + ' '.join(row2))


# board = Board()
# board.print_single_board()
# board.print_double_board()

game = Game()
game.setup_boats()

# menu = MainMenu()
# menu.run()

#R - rotate
#