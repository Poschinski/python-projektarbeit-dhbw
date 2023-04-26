"""
    Code Description
"""
import os
import random
import keyboard



def clear_terminal():
    if os.name == 'posix':  # for Mac and Linux
        os.system('clear')
    elif os.name == 'nt':  # for Windows
        os.system('cls')


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
        self.boat_ammount = [1, 2, 3, 4]
        self.boat_lengths = [5, 4, 3, 2]
        self.selected_boat = 0
        self.direction = "horizontal"
        self.changed_direction = False
        self.value_matrix = [[0 for _ in range(11)] for _ in range(11)]
        self.move_matrix = [[0 for _ in range(11)] for _ in range(11)]
        for i in range(5):
            self.move_matrix[1][1+i] = 3

    def update_position(self, new_pos, changed_direction, boat_length):
        length = boat_length
        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
        self.board.print_single_board()
        x, y = new_pos
        if self.direction == "horizontal":
            if x < 1 or x >= 11 or y < 1 or y+length >= 12:
                if changed_direction is True:
                    self.direction = "vertical"
                return
        else:
            if x < 1 or x+length >= 12 or y < 1 or y >= 11:
                if changed_direction is True:
                    self.direction = "horizontal"
                return

        for i, row in enumerate(self.move_matrix):  #reset all position
                        for j, _ in enumerate(row):
                            self.move_matrix[i][j] = 0

        for i in range(length):
            if self.direction == "horizontal":
                self.move_matrix[x][y+i] = 3  # update the new position
            else:
                self.move_matrix[x+i][y] = 3  # update the new position
        
        self.current_pos = new_pos
        clear_terminal()
        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
        self.board.print_single_board()

    def change_value(self, boat_length, direction):
        row, col = self.current_pos
        print(row, col)
        if direction == "horizontal":
            for i in range(boat_length):
                print(boat_length)
                if self.value_matrix[row][col+i] == 1 or self.value_matrix[row][col+i] == 2:
                    return
            for i in range(boat_length):
                self.value_matrix[row][col+i] = 2
                if row+1 <= 10 and col+i <= 10:
                    self.value_matrix[row+1][col+i] = 1 #bottom line
                if row-1 > 0 and col+i <= 10:
                    self.value_matrix[row-1][col+i] = 1 #top line
                if row-1 > 0 and col-1 > 0:
                    self.value_matrix[row-1][col-1] = 1 #top left
                if row+1 <= 10 and col-1 > 0:
                    self.value_matrix[row+1][col-1] = 1 #bottm left
                if col-1 >0:
                    self.value_matrix[row][col-1] = 1 #left
                if col+boat_length <= 10:
                    self.value_matrix[row][col+boat_length] = 1 #right
                if row-1 > 0 and col+boat_length <= 10:
                    self.value_matrix[row-1][col+boat_length] = 1 #top right
                if row+1 <= 10 and col+boat_length <= 10:
                    self.value_matrix[row+1][col+boat_length] = 1 #bottom right
        else:
            for i in range(boat_length):
                print(boat_length)
                if self.value_matrix[row+i][col] == 1 or self.value_matrix[row+i][col] == 2:
                    return
            for i in range(boat_length):
                self.value_matrix[row+i][col] = 2
                if row+i <= 10 and col-1 > 0:
                    self.value_matrix[row+i][col-1] = 1 #left line
                if row+i <= 10 and col+1 <= 10:
                    self.value_matrix[row+i][col+1] = 1 #right line
                if row-1 > 0 and col-1 > 0:
                    self.value_matrix[row-1][col-1] = 1 #top left
                if row-1 > 0 and col+1 <= 10:
                    self.value_matrix[row-1][col+1] = 1 #top right
                if row-1 >0:
                    self.value_matrix[row-1][col] = 1 #top
                if row+boat_length <= 10:
                    self.value_matrix[row+boat_length][col] = 1 #bottom
                if row+boat_length <= 10 and col-1 > 0:
                    self.value_matrix[row+boat_length][col-1] = 1 #bottom left
                if row+boat_length <= 10 and col+1 <= 10:
                    self.value_matrix[row+boat_length][col+1] = 1 #bottom right
        clear_terminal()
        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
        self.board.print_single_board()


        
    def setup_boats(self):
        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
        self.board.print_single_board()
        print(self.boat_ammount[1])
        
        while True:
            event = keyboard.read_event()
            changed_direction = False
            all_boats_placed = all(amount == 0 for amount in self.boat_ammount)
            if not all_boats_placed:
                for i, amount in enumerate(self.boat_ammount):
                    if amount != 0:
                        length = self.boat_lengths[i]
                        self.selected_boat = i
                        break
            else:
                for i, row in enumerate(self.move_matrix):  #reset all position
                        for j, _ in enumerate(row):
                            self.move_matrix[i][j] = 0
                self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
                self.board.print_single_board()

            if event.event_type == 'down':
                if event.name == 'up' or event.name == 'nach-oben':
                    self.update_position((self.current_pos[0]-1, self.current_pos[1]),changed_direction, length)
                elif event.name == 'down' or event.name == 'nach-unten':
                    self.update_position((self.current_pos[0]+1, self.current_pos[1]),changed_direction, length)
                elif event.name == 'left' or event.name == 'nach-links':
                    self.update_position((self.current_pos[0], self.current_pos[1]-1),changed_direction, length)
                elif event.name == 'right' or event.name == 'nach-rechts':
                    self.update_position((self.current_pos[0], self.current_pos[1]+1),changed_direction, length)
                elif event.name == 'enter':
                    self.change_value(length, self.direction)
                    self.boat_ammount[self.selected_boat] -= 1
                    self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
                    self.board.print_single_board()
                    print(self.boat_ammount)
                elif event.name == 'shift' or event.name == 'umschalt':
                    changed_direction = True
                    if self.direction == "horizontal":
                        self.direction = "vertical"
                        self.update_position((self.current_pos[0], self.current_pos[1]),changed_direction, length)
                    else:
                        self.direction = "horizontal"
                        self.update_position((self.current_pos[0], self.current_pos[1]),changed_direction, length)
                elif event.name == 'r':
                    board = Board()
                    self.value_matrix = board.random_boat_setup()
                    allBoatsPlaced = True
                    for i, row in enumerate(self.move_matrix):
                        for j, _ in enumerate(row):
                            self.move_matrix[i][j] = 0
                    self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
                    self.board.print_single_board()
                elif event.name == 'tab':
                    print("TAB")
                elif event.name == 'esc':
                    break  # exit the loop if the 'esc' key is pressed

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


class Board:
    """
    Class Description
    """

    def __init__(self):
        self.board1 = [[' ' for i in range(13)] for j in range(12)]
        self.board2 = [[' ' for i in range(13)] for j in range(12)]
        self.display_matrix = [[0 for _ in range(11)] for _ in range(11)]
        self.random_matrix = [[0 for j in range(11)] for i in range(11)]
        self.value_matrix = [[0 for j in range(11)] for i in range(11)]
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

    def random_boat_setup(self):
    # Initialize a 10x10 matrix with zeros

        # Define the boat sizes
        boat_sizes = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]

        def can_place_boat(matrix, row, col, size, direction):
            # Check if the boat would go out of bounds
            if direction == 'horizontal' and col + size > 10:
                return False
            elif direction == 'vertical' and row + size > 10:
                return False
            # Check if the boat would overlap with another boat
            for i in range(size+1):
                if direction == 'horizontal':
                    if col+i <= 10 and matrix[row][col] == 2:
                        return False
                    if col+i <= 10 and matrix[row][col+i] == 2:
                        return False
                    if col+i > 0 and matrix[row][col-1] == 2:
                        return False
                elif direction == 'vertical':
                    if row+i <= 10 and matrix[row][col] == 2:
                        return False
                    if row+i <= 10 and matrix[row+i][col] == 2:
                        return False
                    if row+i > 0 and matrix[row-1][col] == 2:
                        return False
            # Check if the boat would touch another boat
            for i in range(size+1):
                if direction == 'horizontal':
                    if row-1 > 0 and col+i <= 10 and self.random_matrix[row-1][col+i] == 2:
                        return False
                    if row+1 <= 10 and col+i <= 10 and self.random_matrix[row+1][col+i] == 2:
                        return False
                    if col-1 > 0 and row-1 > 0 and self.random_matrix[row-1][col-1] == 2:
                        return False
                    if col-1 > 0 and row+1 <= 10 and self.random_matrix[row+1][col-1] == 2:
                        return False
                elif direction == 'vertical':
                    if row+i <= 10 and col-1 > 0 and self.random_matrix[row+i][col-1] == 2:
                        return False
                    if row+i <= 10 and col+1 <= 10 and self.random_matrix[row+i][col+1] == 2:
                        return False
                    if row-1 > 0 and col-1 > 0 and self.random_matrix[row-1][col-1] == 2:
                        return False
                    if row-1 > 0 and col+1 <= 10 and self.random_matrix[row-1][col+1] == 2:
                        return False
            # If all checks pass, the boat can be placed
            return True
        # Place the boats
        while True:
            # Remove all boats from the matrix
            for size in boat_sizes:
                placed = False
                while not placed:
                        row = random.randint(1, 10)
                        col = random.randint(1, 10)
                        direction = random.choice(['horizontal', 'vertical'])
                        if can_place_boat(self.random_matrix, row, col, size, direction):
                            for i in range(size):
                                if direction == 'horizontal':
                                    self.random_matrix[row][col+i] = 2
                                    if row-1 > 0 and col+i <= 10:
                                        self.random_matrix[row-1][col+i] = 1 #top line
                                    if row+1 <= 10 and col+i <= 10:
                                        self.random_matrix[row+1][col+i] = 1 #bottom line
                                    if col-1 > 0:
                                        self.random_matrix[row][col-1] = 1 #left
                                    if col+size <= 10 and i==1:
                                        self.random_matrix[row][col+size] = 1 #right
                                    if col-1 > 0 and row-1 > 0:
                                        self.random_matrix[row-1][col-1] = 1 #top left
                                    if col-1 > 0 and row+1 <= 10:
                                        self.random_matrix[row+1][col-1] = 1 #bottom left
                                    if col+size <= 10 and row-1 > 0 and i==1:
                                        self.random_matrix[row-1][col+size] = 1 #top right
                                    if col+size <= 10 and row+1 <= 10 and i==1:
                                        self.random_matrix[row+1][col+size] = 1 #bottom right
                                else:
                                    self.random_matrix[row+i][col] = 2
                                    if row+i <= 10 and col+1 <= 10:
                                        self.random_matrix[row+i][col+1] = 1 #right line
                                    if row+i <= 10 and col-1 > 0:
                                        self.random_matrix[row+i][col-1] = 1 #left line
                                    if row-1 > 0:
                                        self.random_matrix[row-1][col] = 1 #top
                                    if row+size <= 10 and i==1:
                                        self.random_matrix[row+size][col] = 1 #bottom
                                    if col-1 > 0 and row-1 > 0:
                                        self.random_matrix[row-1][col-1] = 1 #top left
                                    if col-1 > 0 and row+size <= 10 and i == 1:
                                        self.random_matrix[row+size][col-1] = 1 #bottom left
                                    if col+1 <= 10 and row-1 > 0:
                                        self.random_matrix[row-1][col+1] = 1 #top right
                                    if col+1 <= 10 and row+size <= 10 and i==1:
                                        self.random_matrix[row+size][col+1] = 1 #bottom right
                            placed = True
                        else:
                            # Generate new random position and direction for the boat
                            row = random.randint(1, 10)
                            col = random.randint(1, 10)
                            direction = random.choice(['horizontal', 'vertical'])
            # Check if all boats were placed and exit loop if so
            if all([size == sum(row) for row in self.random_matrix] for size in boat_sizes):
                break
        return self.random_matrix


    
    def color_matrix_positions(self, move_matrix, value_matrix, grey='\u001b[100m', blue='\u001b[94;106m', red='\u001b[101m', green='\u001b[102m' ):
        
        for i in range(1, 11):
            for j in range(1, 11):
                if move_matrix[i][j] == 3:
                    if value_matrix[i][j] == 0:
                        self.display_matrix[i][j] = 3
                    else: 
                        self.display_matrix[i][j] = 4
                else:
                    self.display_matrix[i][j] = value_matrix[i][j]
        for i in range(1, 11):
            for j in range(1,11):
                if self.display_matrix[i][j] == 0 or self.display_matrix[i][j] == 1:
                    self.board1[i][j] = f'{blue} ~ \u001b[0m |'
                elif self.display_matrix[i][j] == 2:
                    self.board1[i][j] = f'{grey}   \u001b[0m |'
                elif self.display_matrix[i][j] == 3:
                    self.board1[i][j] = f'{green}   \u001b[0m |'
                elif self.display_matrix[i][j] == 4:
                    self.board1[i][j] = f'{red}   \u001b[0m |'



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
        clear_terminal()
        print(board_display)



    def print_double_board(self):
        for i, (row1, row2) in enumerate(zip(self.board1, self.board2)):
            if i == 0:
                clear_terminal()
                print(' \n ')
                print(' ' * 8 + 'Player 1'.center(50) +
                      ' ' * 24 + 'Player 2'.center(50))
                print(' ' * 5 + '-'*61 + ' ' * 13 + '-'*61)
                print(' '.join(row1) + ' ' * 4 + ' '.join(row2))
            else:
                print('--'*33 + ' ' * 8 + '--'*33)
                print(' '.join(row1) + ' ' * 4 + ' '.join(row2))


# board = Board()
# board.random_boat_setup()
# board.print_single_board()
# board.print_double_board()

game = Game()
game.setup_boats()

# menu = MainMenu()
# menu.run()

#R - rotate
#
