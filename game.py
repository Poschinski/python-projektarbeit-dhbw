"""
    Code Description
"""
import random
import json
import keyboard
from utilities import clear_terminal, create_matrix, reset_matrix, random_boat_setup
from board import Board


class GameSetup:
    """
    Class Description
    """

    def __init__(self):
        self.board = Board()
        self.current_pos = [1, 1]
        self.ammount = [1,2,3,4]
        self.direction = "horizontal"
        self.changed_direction = False
        self.value_matrix = create_matrix()
        self.move_matrix = create_matrix()
        for i in range(5):
            self.move_matrix[1][1+i] = 3


    def update_position(self, new_pos, changed_direction, boat_length, player_name):
        """
        Update the current boat position and display the changes on the board.

        Args:
            new_pos (tuple): The new position to update the boat position to, as a tuple (row, col).
            changed_direction (bool): True if the boat direction has changed, False otherwise.
            boat_length (int): The length of the current boat being placed.

        Returns:
            None

        """
        length = boat_length
        row, col = new_pos
        if self.direction == "horizontal":
            if row < 1 or row >= 11 or col < 1 or col+length >= 12:
                if changed_direction is True:
                    self.direction = "vertical"
                return
        else:
            if row < 1 or row+length >= 12 or col < 1 or col >= 11:
                if changed_direction is True:
                    self.direction = "horizontal"
                return
        self.move_matrix = reset_matrix()

        for i in range(length):
            if self.direction == "horizontal":
                self.move_matrix[row][col+i] = 3  # update the new position
            else:
                self.move_matrix[row+i][col] = 3  # update the new position
        self.current_pos = new_pos
        clear_terminal()
        self.board.color_matrix_positions_boat_setup(self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount, player_name)

    def add_boat_surrounding_horizontol(self, row, col, boat_length, i):
        """
        Update value_matrix by marking the surrounding positions of a boat that is placed horizontally.

        Parameters:
        row (int): The row index of the boat's starting position.
        col (int): The column index of the boat's starting position.
        boat_length (int): The length of the boat.
        i (int): The index of the boat's position.

        Returns:
        None
        """
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

    def add_boat_surrounding_vertical(self, row, col, boat_length, i):
        """
        Update the value matrix with the surrounding values for a vertical boat

        Parameters:
        row (int): The row index of the starting position of the boat
        col (int): The column index of the starting position of the boat
        boat_length (int): The length of the boat to be added
        i (int): The current index being updated in the boat

        Returns:
        None
        """
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

    def change_value(self, boat_length, direction, player_name):
        """
        Updates the value_matrix to indicate the new position of a boat.

        Args:
            boat_length (int): The length of the boat being moved.
            direction (str): The direction in which the boat is being moved. Must be either "horizontal" or "vertical".

        Returns:
            bool: True if the boat was successfully placed in the new position, False otherwise.

        """
        row, col = self.current_pos
        if direction == "horizontal":
            for i in range(boat_length):
                if self.value_matrix[row][col+i] == 1 or self.value_matrix[row][col+i] == 2:
                    return False
            for i in range(boat_length):
                self.value_matrix[row][col+i] = 2
                self.add_boat_surrounding_horizontol(row, col, boat_length, i)
        else:
            for i in range(boat_length):
                if self.value_matrix[row+i][col] == 1 or self.value_matrix[row+i][col] == 2:
                    return False
            for i in range(boat_length):
                self.value_matrix[row+i][col] = 2
                self.add_boat_surrounding_vertical(row, col, boat_length, i)
        clear_terminal()
        self.board.color_matrix_positions_boat_setup(self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount, player_name)
        return True

    def reset_boat_setup(self, player_name):
        """
        Resets the boat setup to start again.

        Resets the value_matrix and move_matrix to their initial values, places
        the first boat in the move_matrix, and resets the all_boats_placed and
        direction instance variables. Clears the terminal, updates the
        color_matrix_positions_boat_setup, and prints the board.
        """
        self.value_matrix = reset_matrix()
        self.move_matrix = reset_matrix()
        for i in range(5):
            self.move_matrix[1][1+i] = 3
        self.direction = "horizontal"
        clear_terminal()
        self.board.color_matrix_positions_boat_setup(self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount, player_name)

    def change_direction(self, length, player_name):
        """
        Changes the current boat placement direction from horizontal to vertical
        or vice versa.

        Args:
            length (int): The length of the boat being placed.

        Returns:
            None
        """

        changed_direction = True
        if self.direction == "horizontal":
            self.direction = "vertical"
            self.update_position((self.current_pos[0], self.current_pos[1]),changed_direction, length, player_name)
        else:
            self.direction = "horizontal"
            self.update_position((self.current_pos[0], self.current_pos[1]),changed_direction, length, player_name)

    def handle_key_event_befor_placement(self, event, length, selected_boat, player_name):
        """
        Handles the key events during the game.

        Parameters:
            event (keyboard.KeyboardEvent): A keyboard event.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        changed_direction = False
        if event.name in ('up', 'nach-oben'):
            self.update_position((self.current_pos[0]-1, self.current_pos[1]),changed_direction, length, player_name)
        elif event.name in ('down', 'nach-unten'):
            self.update_position((self.current_pos[0]+1, self.current_pos[1]),changed_direction, length, player_name)
        elif event.name in ('left', 'nach-links'):
            self.update_position((self.current_pos[0], self.current_pos[1]-1),changed_direction, length, player_name)
        elif event.name in ('right', 'nach-rechts'):
            self.update_position((self.current_pos[0], self.current_pos[1]+1),changed_direction, length, player_name)
        elif event.name == 'enter':
            if self.change_value(length, self.direction, player_name) is True:
                self.ammount[selected_boat] -= 1
            clear_terminal()
            self.board.color_matrix_positions_boat_setup(self.move_matrix, self.value_matrix)
            self.board.print_single_board(self.ammount, player_name)
        elif event.name in ('shift', 'umschalt'):
            self.change_direction(length, player_name)
        elif event.name == 'r':
            self.ammount = [1,2,3,4]
            self.value_matrix = random_boat_setup()
            self.move_matrix = reset_matrix()
            for index, _ in enumerate(self.ammount):
                self.ammount[index] = 0
            clear_terminal()
            self.board.color_matrix_positions_boat_setup(self.move_matrix, self.value_matrix)
            self.board.print_single_board(self.ammount, player_name)
        elif event.name == 'esc':
            self.ammount = [1,2,3,4]
            self.reset_boat_setup(player_name)
            return False, True
        elif event.name == 's':
            print("you still have boats to be placed!")
        elif event.name == 'b':
            return False, False
        return True, False

    def handle_key_event_after_placement(self, event, player_name):
        """
        Method for handling key events after boat placement is complete.
        Args:
            event (keyboard.KeyboardEvent): the keyboard event to handle
        Returns:
            bool or None: Returns True if 's' key is pressed and all boats have been placed,
                        False if 'b' key is pressed to go back to boat placement,
                        None otherwise.
        """
        if event.name == 'esc':
            self.ammount = [1,2,3,4]
            self.reset_boat_setup(player_name)
            return False, True
        if event.name == 's':
            return True, True
        if event.name == 'b':
            return False, False
        return True, False


    def setup_boats(self, player_name):
        """
        Method for setting up boats on the board.

        Returns:
        - False if the game should be terminated
        - True if the boat setup is complete and the game should start
        """
        selected_boat = 0
        lengths = [5,4,3,2]
        self.ammount = [1,2,3,4]
        return_val_one = True
        return_val_two = False
        all_boats_placed = False
        self.reset_boat_setup(player_name)
        clear_terminal()
        self.board.color_matrix_positions_boat_setup(self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount, player_name)
        while True:
            event = keyboard.read_event()
            all_boats_placed = all(amount == 0 for amount in self.ammount)
            if not all_boats_placed:
                for i, amount in enumerate(self.ammount):
                    if amount != 0:
                        length = lengths[i]
                        selected_boat = i
                        break
            else:
                self.move_matrix = reset_matrix()
                clear_terminal()
                self.board.color_matrix_positions_boat_setup(self.move_matrix, self.value_matrix)
                self.board.print_single_board(self.ammount, player_name)

            if event.event_type == 'down':
                if all_boats_placed is False:
                    return_val_one, return_val_two = self.handle_key_event_befor_placement(event, length, selected_boat, player_name)
                else:
                    return_val_one, return_val_two = self.handle_key_event_after_placement(event, player_name)
            if return_val_one:
                if return_val_two: #True True
                    break
            else:
                if return_val_two: #False True
                    all_boats_placed = False
                    self.current_pos = [1,1]
                else:       #False False
                    return False, None
        return True, self.value_matrix

class Game:
    """
    asdasd
    """
    def __init__(self):
        self.board = Board()
        self.current_pos = [1,1]
        self.move_matrix = create_matrix()
        self.win = False
        self.confirm_key = ''
        self.miss = False
        self.is_bot = False

    def handle_keyboard_event(self, matrix_one, matrix_two, player_names):
        """
        Handles a keyboard event for a player's turn in the game.

        Args:
            matrix_one (list): A matrix representing the first player's board
            matrix_two (list): A matrix representing the second player's board

        Returns:
            A tuple of two boolean values. The first value indicates whether the player's
            turn has ended (True) or not (False). The second value indicates whether the
            game should end (True) or not (False).
        """
        event = keyboard.read_event()
        direction = ''
        if event.event_type == 'down':
            if event.name in ('up', 'nach-oben') and self.miss is False:
                direction = 'up'
                self.move(matrix_one, matrix_two, direction, player_names)

            if event.name in ('down', 'nach-unten') and self.miss is False:
                direction = 'down'
                self.move(matrix_one, matrix_two, direction, player_names)

            if event.name in ('left', 'nach-links') and self.miss is False:
                direction = 'left'
                self.move(matrix_one, matrix_two, direction, player_names)

            if event.name in ('right', 'nach-rechts') and self.miss is False:
                direction = 'right'
                self.move(matrix_one, matrix_two, direction, player_names)

            if event.name == 'enter':
                if self.confirm_key !='enter':
                    hit = self.attack(matrix_one, matrix_two, player_names)
                    if hit:
                        print("hit!")
                    elif self.miss is True:
                        self.move_matrix = reset_matrix()
                        self.board.color_matrix_positions_board_one(self.move_matrix, matrix_one)
                        self.confirm_key = 'enter'
                        print('press enter again to finish you round')
                else:
                    self.confirm_key = ''
                    return True, False

            if event.name == 'esc':
                return True, True

            if self.win:
                return True ,False
        return False, False

    def update_board(self, move_matrix, matrix_one, matrix_two, player_names):
        """
        Updates the colors of the board and prints the board

        Functions:
            board.color_matrix_positions_board_one()
            board.color_matrix_positions_board_two()
            board.print_double_board

        Args:
            move_matrix (list of litst)
            matrix_one (list of lists)
            matrix_two (list of lists)

        Returns:
            None
        """
        clear_terminal()
        if self.is_bot:
            self.board.color_matrix_positions_board_one(move_matrix, matrix_two)
            self.board.color_matrix_positions_board_two(matrix_one)
            self.board.print_double_board(player_names['name_one'], player_names['name_two'])
        else:
            self.board.color_matrix_positions_board_one(move_matrix, matrix_one)
            self.board.color_matrix_positions_board_two(matrix_two)
            self.board.print_double_board(player_names['name_one'], player_names['name_two'])

    def move(self, matrix_one, matrix_two, direction, player_names):
        """
        Updates the player's cursor position on their board based on the given direction.

        Functions:
            reset_matrix()
            self.update_board()

        Args:
            matrix_one (list): The player's board matrix.
            matrix_two (list): The opponent's board matrix.
            direction (str): The direction to move the cursor. Can be 'up', 'down', 'left', or 'right'.

        Returns:
            None

        """
        if direction == 'up':
            row, col = (self.current_pos[0]-1, self.current_pos[1])
            if row > 0:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row,col)
                self.update_board(self.move_matrix, matrix_one, matrix_two, player_names)
                return
        if direction == 'down':
            row, col = (self.current_pos[0]+1, self.current_pos[1])
            if row <= 10:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row,col)
                self.update_board(self.move_matrix, matrix_one, matrix_two, player_names)
                return
        if direction == 'left':
            row, col = (self.current_pos[0],self.current_pos[1]-1)
            if col > 0:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row,col)
                self.update_board(self.move_matrix, matrix_one, matrix_two, player_names)
                return
        if direction == 'right':
            row, col = (self.current_pos[0],self.current_pos[1]+1)
            if col <= 10:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row,col)
                self.update_board(self.move_matrix, matrix_one, matrix_two, player_names)
                return

    def mark_destroyed_boat(self, matrix, row, col):
        """
        Given a matrix, the row and column of a destroyed boat,
        mark all other positions of the boat with 7 without going out of index.

        Args:
            matrix (list of list)
        """
        # check if the boat is vertical or horizontal
        if matrix[row][col] == 7 and ((row-1 >= 0 and matrix[row-1][col] == 6) or (row+1 <= 9 and matrix[row+1][col] == 6)):
            # the boat is vertical, mark all other positions of the boat with 7
            start_row = row
            while start_row > 0 and matrix[start_row-1][col] == 6:
                start_row -= 1
            end_row = row
            while end_row < 9 and matrix[end_row+1][col] == 6:
                end_row += 1
            for i in range(start_row, end_row+1):
                matrix[i][col] = 7
        else:
            # the boat is horizontal, mark all other positions of the boat with 7
            start_col = col
            while start_col > 0 and matrix[row][start_col-1] == 6:
                start_col -= 1
            end_col = col
            while end_col < 9 and matrix[row][end_col+1] == 6:
                end_col += 1
            for j in range(start_col, end_col+1):
                matrix[row][j] = 7


    def check_for_game_ending(self, value_matrix):
        """
        kasmdmads
        """
        for row in range(11):
            for col in range(11):
                if value_matrix[row][col] == 2:
                    return False
        self.win = True
        return True

    def mark_destroyed_boat_surrounding(self, value_matrix):
        """
        kasmdmads
        """
        for row in range(11):
            for col in range (11):
                if value_matrix[row][col] == 7:
                    if row-1 > 0 and col-1 > 0 and value_matrix[row-1][col-1] != 7:
                        value_matrix[row-1][col-1] = 5
                    if row-1 > 0 and value_matrix[row-1][col] != 7:
                        value_matrix[row-1][col] = 5
                    if row-1 > 0 and col+1 <=10 and value_matrix[row-1][col+1] != 7:
                        value_matrix[row-1][col+1] = 5
                    if col+1 <= 10 and value_matrix[row][col+1] != 7:
                        value_matrix[row][col+1] = 5
                    if row+1 <= 10 and col+1 <= 10 and value_matrix[row+1][col+1] != 7:
                        value_matrix[row+1][col+1] = 5
                    if row+1 <= 10 and value_matrix[row+1][col] != 7:
                        value_matrix[row+1][col] = 5
                    if row+1 <= 10 and col-1 > 0 and value_matrix[row+1][col-1] != 7:
                        value_matrix[row+1][col-1] = 5
                    if col-1 > 0 and value_matrix[row][col-1] != 7:
                        value_matrix[row][col-1] = 5

    def check_for_detroyed_boats(self, row, col, value_matrix):
        """
        asdasd
        """
        if row-1 > 0:
            if value_matrix[row-1][col] == 2:
                return False
        if row+1 <= 10:
            if value_matrix[row+1][col] == 2:
                return False
        if col-1 > 0:
            if value_matrix[row][col-1] == 2:
                return False
        if col+1 <= 10:
            if value_matrix[row][col+1] == 2:
                return False
        value_matrix[row][col] = 7
        self.mark_destroyed_boat(value_matrix, row, col)
        self.mark_destroyed_boat_surrounding(value_matrix)
        self.check_for_game_ending(value_matrix)
        return False

    def attack(self, value_matrix, matrix_two, player_names):
        """
        asdasd
        """
        row, col = (self.current_pos[0],self.current_pos[1])
        if value_matrix[row][col] == 5 or value_matrix[row][col] == 6:
            self.miss = False
            return False
        if value_matrix[row][col] == 0 or value_matrix[row][col] == 1:
            value_matrix[row][col] = 5
            self.miss = True
            self.update_board(self.move_matrix, value_matrix, matrix_two, player_names)
            return False
        if value_matrix[row][col] == 2:
            value_matrix[row][col] = 6
            self.miss = False
            self.check_for_detroyed_boats(row, col, value_matrix)
            self.update_board(self.move_matrix, value_matrix, matrix_two, player_names)
            return True
        return False

    def bot(self, matrix_player, matrix_bot, player_names):
        """
        Class Description
        """
        while self.miss is False:
            self.current_pos = [(random.randint(1,10)),(random.randint(1,10))]
            self.attack(matrix_bot, matrix_player, player_names)
        return True
    def save_game(self, game_params, filename='game_params.json'):
        """
        Clear the existing game parameters in the JSON file at id 1 and save the provided game_params.
        """
        with open(filename, 'r') as file:
            game_params_list = json.load(file)

        # Find the game parameters with id 1
        for params in game_params_list:
            if params['id'] == 1:
                # Clear the existing game parameters and replace them with the new ones
                params.clear()
                params.update(game_params)
                break

        # Save the updated game parameters to the file
        with open(filename, 'w') as file:
            json.dump(game_params_list, file)

    def display_befor_round(self, option, player_one_name, player_two_name, player_one_turn, exit_game):
        """
        asdasd
        """
        if option == 0:
            clear_terminal()
            if player_one_turn:
                print(f"{player_one_name} is starting! \nPress 'Enter' to show Boards")
            else:
                print(f"{player_two_name} is starting! \nPress 'Enter' to show Boards")

            keyboard.wait('enter')
            return
        if option == 1:
            if not self.win and not exit_game:
                clear_terminal()
                print(f"{player_two_name}`s turn! \nPress 'enter' to show Boards")
                keyboard.wait('enter')
                return
        if option == 2:
            if not self.win and not exit_game:
                clear_terminal()
                print(f"{player_one_name}`s turn! \nPress 'enter' to show Boards")
                keyboard.wait('enter')
                return


    def singleplayer(self,player_one_name, player_two_name, player_two_matrix, player_one_matrix):
        """
        Class Description
        """
        self.move_matrix[1][1] = 3
        player_names = {
            'name_one': player_one_name,
            'name_two': player_two_name
        }
        self.update_board(self.move_matrix, player_one_matrix, player_two_matrix, player_names)
        player_one_turn = random.randint(1,2)
        game_round = False
        exit_game = False

        while True:
            if player_one_turn == 1:
                self.move_matrix[1][1] = 3
                self.is_bot = False
                while game_round is False:
                    self.update_board(self.move_matrix, player_one_matrix, player_two_matrix, player_names)
                    game_round, exit_game = self.handle_keyboard_event(player_one_matrix, player_two_matrix, player_names)
                player_one_turn = 2
                game_round = False
                self.miss = False
                self.current_pos = (1,1)
            else:
                while game_round is False:
                    self.is_bot = True
                    self.update_board(self.move_matrix, player_two_matrix, player_one_matrix,player_names)
                    game_round = self.bot(player_one_matrix, player_two_matrix, player_names)
                    print(self.miss)
                player_one_turn = 1
                game_round = False
                self.miss = False
                self.current_pos = (1,1)

            if self.win:
                print("Game over!")
                return True
            if exit_game:
                game_params = {
                    'gamemode': 1,
                    'player_name_one': player_one_name,
                    'player_name_two': player_two_name,
                    'player_matrix_one': player_one_matrix,
                    'player_matrix_two': player_two_matrix,
                    'starting_player': player_one_turn
                }
                self.save_game(game_params)
                break


    def multiplayer(self, player_one_name, player_two_name, player_two_matrix, player_one_matrix):
        """
        asdasd
        """
        self.move_matrix[1][1] = 3
        player_one_turn = random.choice([True, False])
        game_round = False
        exit_game = False

        self.display_befor_round(0, player_one_name, player_two_name, player_one_turn, exit_game)

        while True:
            if player_one_turn:
                player_names = {
                    'name_one': player_two_name,
                    'name_two': player_one_name
                }
                self.move_matrix[1][1] = 3
                while game_round is False:
                    self.update_board(self.move_matrix, player_one_matrix, player_two_matrix, player_names)
                    game_round, exit_game = self.handle_keyboard_event(player_one_matrix, player_two_matrix, player_names)
                player_one_turn = False
                game_round = False
                self.miss = False
                self.current_pos = (1,1)
                self.display_befor_round(1, player_one_name, player_two_name, player_one_turn, exit_game)
            else:
                player_names = {
                    'name_one': player_one_name,
                    'name_two': player_two_name
                }
                self.move_matrix[1][1] = 3
                while game_round is False:
                    self.update_board(self.move_matrix, player_two_matrix, player_one_matrix, player_names)
                    game_round, exit_game = self.handle_keyboard_event(player_two_matrix, player_one_matrix, player_names)
                player_one_turn = True
                game_round = False
                self.miss = False
                self.current_pos = (1,1)
                self.display_befor_round(2, player_one_name, player_two_name, player_one_turn, exit_game)

            if self.win:
                print("Game over!")
                return True
            if exit_game:
                return True
