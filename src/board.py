"""
    Board
"""


class Board:
    """
    Class for creating, changing and displaying Game Boards.
    """

    def __init__(self):
        self.board1 = [[' ' for i in range(13)] for j in range(12)]
        self.board2 = [[' ' for i in range(13)] for j in range(12)]
        self.display_matrix = [[0 for _ in range(11)] for _ in range(11)]
        self.random_matrix = [[0 for j in range(11)] for i in range(11)]
        self.value_matrix = [[0 for j in range(11)] for i in range(11)]
        self.add_column_labels()
        self.add_row_labels_and_color()


    def add_column_labels(self):
        """
        This function adds the column Labels to the Board
        """
        for i, label in enumerate(['    ', '|  A ', '|  B ', '|  C ', '|  D ', '|  E ', '|  F ', '|  G ', '|  H ', '|  I ', '|  J  |']):
            self.board1[0][i] = label
            self.board2[0][i] = label
            self.sizes = [5, 4, 3, 2]
            self.num_boats = [1, 2, 3, 4]

    # color = light blue
    def add_row_labels_and_color(self, color='\u001b[94;106m'):
        """
        This function adds the row labels to the Board and is also creating a 10x10 Game Board,
        with a light blue and the ~ character for displaying water.
        """
        for i in range(1, 11):
            # pad single-digit labels with leading zero
            row_label = f'{i:02d}'
            self.board1[i][0] = '| ' + row_label + ' |'
            self.board2[i][0] = '| ' + row_label + ' |'
            for j in range(1, 11):
                # add light blue background color to box
                self.board1[i][j] = f'{color} ~ \u001b[0m |'
                # add light blue background color to box
                self.board2[i][j] = f'{color} ~ \u001b[0m |'


    def color_matrix_positions_boat_setup(self, move_matrix, value_matrix):
        """
        This function gets the move_matrix and the value_matrix.
        Those two functions combined are creating a third matrix called display_matrix.
        The display_matrix is for updating the colors of the board 1.
        """
        grey_dark='\u001b[48;5;240m'
        blue='\u001b[94;106m'
        red='\u001b[101m'
        green='\u001b[102m'
        for row in range(1, 11):
            for col in range(1, 11):
                if move_matrix[row][col] == 3:
                    if value_matrix[row][col] == 0:
                        self.display_matrix[row][col] = 3
                    else:
                        self.display_matrix[row][col] = 4
                else:
                    self.display_matrix[row][col] = value_matrix[row][col]
        for row in range(1, 11):
            for col in range(1,11):
                if self.display_matrix[row][col] == 0 or self.display_matrix[row][col] == 1:
                    self.board1[row][col] = f'{blue} ~ \u001b[0m |'
                elif self.display_matrix[row][col] == 2:
                    self.board1[row][col] = f'{grey_dark}   \u001b[0m |'
                elif self.display_matrix[row][col] == 3:
                    self.board1[row][col] = f'{green}   \u001b[0m |'
                elif self.display_matrix[row][col] == 4:
                    self.board1[row][col] = f'{red}   \u001b[0m |'

    def color_matrix_positions_board_one(self, move_matrix, value_matrix):
        """
        This function gets the move_matrix and the value_matrix.
        Those two functions combined are creating a third matrix called display_matrix.
        The display_matrix is for updating the colors of the board 1.
        """
        grey_dark='\u001b[48;5;240m'
        grey_light='\u001b[48;5;247m'
        blue='\u001b[94;106m'
        blue_dark='\u001b[44m'
        red='\u001b[101m'
        green='\u001b[102m'
        color_table = {
            0: f'{blue} ~ \u001b[0m |',
            1: f'{blue} ~ \u001b[0m |',
            2: f'{blue} ~ \u001b[0m |',
            3: f'{green}   \u001b[0m |',
            4: f'{red}   \u001b[0m |',
            5: f'{blue_dark} X \u001b[0m |',
            6: f'{grey_light} X \u001b[0m |',
            7: f'{grey_dark} X \u001b[0m |',
        }

        for row in range(1, 11):
            for col in range(1, 11):
                if move_matrix[row][col] == 3:
                    if value_matrix[row][col] == 0 or value_matrix[row][col] == 1 or value_matrix[row][col] == 2:
                        self.display_matrix[row][col] = 3
                    else:
                        self.display_matrix[row][col] = 4
                else:
                    self.display_matrix[row][col] = value_matrix[row][col]
        for row in range(1, 11):
            for col in range(1, 11):
                self.board1[row][col] = color_table.get(self.display_matrix[row][col], '')

    def color_matrix_positions_board_two(self, value_matrix):
        """
        This function gets the move_matrix and the value_matrix.
        Those two functions combined are creating a third matrix called display_matrix.
        The display_matrix is for updating the colors of the board 2.
        """
        grey_dark='\u001b[48;5;240m'
        grey_light='\u001b[48;5;247m'
        blue='\u001b[94;106m'
        blue_dark='\u001b[44m'
        color_table = {
            0: f'{blue} ~ \u001b[0m |',
            1: f'{blue} ~ \u001b[0m |',
            2: f'{grey_light}   \u001b[0m |',
            5: f'{blue_dark} X \u001b[0m |',
            6: f'{grey_light} X \u001b[0m |',
            7: f'{grey_dark} X \u001b[0m |',
        }
        for row in range(1, 11):
            for col in range(1, 11):
                self.display_matrix[row][col] = value_matrix[row][col]
        for row in range(1, 11):
            for col in range(1,11):
                self.board2[row][col] = color_table.get(self.display_matrix[row][col], '')


    def print_single_board(self, ammount, player_name):
        """
        Function for printing the board 1 in the Terminal.
        """
        instructions = ["Use", "'Arrow keys' to move the boat,", "'Shift' to rotate the boat,",
                        "'Enter' to place the boat,", "'R' for random boat setup,", "'Esc' to reset,", "'S' to save and continue,", "'B' to go back.", ""]
        boat_list = ['Battleship (5)', 'Cruiser (4)',
                     'Destroyer (3)', 'Submarine (2)']
        board_display = ''
        for i, row in enumerate(self.board1):
            if i == 0:
                board_display += ' \n '
                # print horizontal divider before column labels row
                board_display += ' ' * 8 + f'{player_name}`s boat setup'.center(50) + ' ' * 24 + '\n'
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
        boat_list_display = 'Boats remaining: '
        for i, boat in enumerate(boat_list):
            if i == len(boat_list)-1:
                boat_list_display += str(ammount[i]) + 'x ' + boat
            else:
                boat_list_display += str(ammount[i]) + 'x ' + boat + ', '
        board_display += '\n' + boat_list_display + '\n'
        print(board_display)



    def print_double_board(self, player_one, player_two):
        """
        Function for printing 2 Boards in the Terminal
        """
        instructions = ["Use", "'Arrow keys' to move,", "'enter' to attack,", "'enter' to end round,", "'esc' for save and exit", ""]
        for i, (row1, row2) in enumerate(zip(self.board1, self.board2)):
            if i == 0:
                print(' \n ')
                print(' ' * 8 + f'{player_one}`s Board'.center(50) +
                      ' ' * 24 + f'{player_two}`s Board'.center(50))
                print(' ' * 5 + '-'*61 + ' ' * 13 + '-'*61)
                print(' '.join(row1) + ' ' * 4 + ' '.join(row2))
            else:
                print('--'*33 + ' ' * 8 + '--'*33)
                print(' '.join(row1) + ' ' * 4 + ' '.join(row2)+ '   ' + instructions[0])
                if len(instructions) > 1:
                    instructions.pop(0)  # remove next instruction from list
