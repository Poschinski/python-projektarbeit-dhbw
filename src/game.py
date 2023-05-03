"""
    Game
"""
# pylint: disable=import-error
import random
import json
import time

import keyboard
from utilities import clear_terminal, create_matrix, reset_matrix, random_boat_setup
from board import Board


class GameSetup:
    """
    Class for creating boat setups.
    """

    def __init__(self):
        self.board = Board()
        self.current_pos = [1, 1]
        self.ammount = [1, 2, 3, 4]
        self.direction = "horizontal"
        self.changed_direction = False
        self.value_matrix = create_matrix()
        self.move_matrix = create_matrix()
        for i in range(5):
            self.move_matrix[1][1+i] = 3

    def update_position(self, new_pos, changed_direction, boat_length, player_name):
        """
        Update the current boat position and display the changes on the board.
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
        self.board.color_matrix_positions_boat_setup(
            self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount, player_name)

    def add_boat_surrounding_horizontal(self, row, col, boat_length, i):
        """
        Update value_matrix by marking the surrounding positions of a boat that is placed horizontally.
        """
        if row+1 <= 10 and col+i <= 10:
            self.value_matrix[row+1][col+i] = 1  # bottom line
        if row-1 > 0 and col+i <= 10:
            self.value_matrix[row-1][col+i] = 1  # top line
        if row-1 > 0 and col-1 > 0:
            self.value_matrix[row-1][col-1] = 1  # top left
        if row+1 <= 10 and col-1 > 0:
            self.value_matrix[row+1][col-1] = 1  # bottm left
        if col-1 > 0:
            self.value_matrix[row][col-1] = 1  # left
        if col+boat_length <= 10:
            self.value_matrix[row][col+boat_length] = 1  # right
        if row-1 > 0 and col+boat_length <= 10:
            self.value_matrix[row-1][col+boat_length] = 1  # top right
        if row+1 <= 10 and col+boat_length <= 10:
            self.value_matrix[row+1][col+boat_length] = 1  # bottom right

    def add_boat_surrounding_vertical(self, row, col, boat_length, i):
        """
        Update the value matrix with the surrounding values for a vertical boat
        """
        if row+i <= 10 and col-1 > 0:
            self.value_matrix[row+i][col-1] = 1  # left line
        if row+i <= 10 and col+1 <= 10:
            self.value_matrix[row+i][col+1] = 1  # right line
        if row-1 > 0 and col-1 > 0:
            self.value_matrix[row-1][col-1] = 1  # top left
        if row-1 > 0 and col+1 <= 10:
            self.value_matrix[row-1][col+1] = 1  # top right
        if row-1 > 0:
            self.value_matrix[row-1][col] = 1  # top
        if row+boat_length <= 10:
            self.value_matrix[row+boat_length][col] = 1  # bottom
        if row+boat_length <= 10 and col-1 > 0:
            self.value_matrix[row+boat_length][col-1] = 1  # bottom left
        if row+boat_length <= 10 and col+1 <= 10:
            self.value_matrix[row+boat_length][col+1] = 1  # bottom right

    def change_value(self, boat_length, direction, player_name):
        """
        Updates the value_matrix to indicate the new position of a boat.
        """
        row, col = self.current_pos
        if direction == "horizontal":
            for i in range(boat_length):
                if self.value_matrix[row][col+i] == 1 or self.value_matrix[row][col+i] == 2:
                    return False
            for i in range(boat_length):
                self.value_matrix[row][col+i] = 2
                self.add_boat_surrounding_horizontal(row, col, boat_length, i)
        else:
            for i in range(boat_length):
                if self.value_matrix[row+i][col] == 1 or self.value_matrix[row+i][col] == 2:
                    return False
            for i in range(boat_length):
                self.value_matrix[row+i][col] = 2
                self.add_boat_surrounding_vertical(row, col, boat_length, i)
        clear_terminal()
        self.board.color_matrix_positions_boat_setup(
            self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount, player_name)
        return True

    def reset_boat_setup(self, player_name):
        """
        Resets the boat setup to start again.
        """
        self.value_matrix = reset_matrix()
        self.move_matrix = reset_matrix()
        for i in range(5):
            self.move_matrix[1][1+i] = 3
        self.direction = "horizontal"
        self.ammount = [1, 2, 3, 4]
        clear_terminal()
        self.board.color_matrix_positions_boat_setup(
            self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount, player_name)

    def change_direction(self, length, player_name):
        """
        Changes the current boat placement direction from horizontal to vertical
        or vice versa.
        """

        changed_direction = True
        if self.direction == "horizontal":
            self.direction = "vertical"
            self.update_position(
                (self.current_pos[0], self.current_pos[1]), changed_direction, length, player_name)
        else:
            self.direction = "horizontal"
            self.update_position(
                (self.current_pos[0], self.current_pos[1]), changed_direction, length, player_name)

    def handle_key_event_before_placement(self, event, length, selected_boat, player_name):
        """
        Handles the key events during the game.
        """
        changed_direction = False
        if event.name in ('up', 'nach-oben'):
            self.update_position(
                (self.current_pos[0]-1, self.current_pos[1]), changed_direction, length, player_name)
        elif event.name in ('down', 'nach-unten'):
            self.update_position(
                (self.current_pos[0]+1, self.current_pos[1]), changed_direction, length, player_name)
        elif event.name in ('left', 'nach-links'):
            self.update_position(
                (self.current_pos[0], self.current_pos[1]-1), changed_direction, length, player_name)
        elif event.name in ('right', 'nach-rechts'):
            self.update_position(
                (self.current_pos[0], self.current_pos[1]+1), changed_direction, length, player_name)
        elif event.name == 'enter':
            if self.change_value(length, self.direction, player_name) is True:
                self.ammount[selected_boat] -= 1
            clear_terminal()
            self.board.color_matrix_positions_boat_setup(
                self.move_matrix, self.value_matrix)
            self.board.print_single_board(self.ammount, player_name)
        elif event.name in ('shift', 'umschalt'):
            self.change_direction(length, player_name)
        elif event.name == 'r':
            self.ammount = [1, 2, 3, 4]
            self.value_matrix = random_boat_setup()
            self.move_matrix = reset_matrix()
            for index, _ in enumerate(self.ammount):
                self.ammount[index] = 0
            clear_terminal()
            self.board.color_matrix_positions_boat_setup(
                self.move_matrix, self.value_matrix)
            self.board.print_single_board(self.ammount, player_name)
        elif event.name == 'esc':
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
        """
        if event.name == 'esc':
            self.ammount = [1, 2, 3, 4]
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
        """
        selected_boat = 0
        lengths = [5, 4, 3, 2]
        self.ammount = [1, 2, 3, 4]
        return_val_one = True
        return_val_two = False
        all_boats_placed = False
        self.reset_boat_setup(player_name)
        clear_terminal()
        self.board.color_matrix_positions_boat_setup(
            self.move_matrix, self.value_matrix)
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
                self.board.color_matrix_positions_boat_setup(
                    self.move_matrix, self.value_matrix)
                self.board.print_single_board(self.ammount, player_name)

            if event.event_type == 'down':
                if all_boats_placed is False:
                    return_val_one, return_val_two = self.handle_key_event_before_placement(
                        event, length, selected_boat, player_name)
                else:
                    return_val_one, return_val_two = self.handle_key_event_after_placement(
                        event, player_name)
            if return_val_one:
                if return_val_two:  # True True
                    break
            else:
                if return_val_two:  # False True
                    all_boats_placed = False
                    self.current_pos = [1, 1]
                else:  # False False
                    return False, None
        return True, self.value_matrix


class Game:
    """
    Class for the game logic during the game.
    """

    def __init__(self):
        self.board = Board()
        self.current_pos = [1, 1]
        self.move_matrix = create_matrix()
        self.win = False
        self.confirm_key = ''
        self.miss = False
        self.is_bot = False

    def handle_keyboard_event(self, matrix_one, matrix_two, player_names):
        """
        Handles a keyboard event for a player's turn in the game.
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
                if self.confirm_key != 'enter':
                    hit = self.attack(matrix_one, matrix_two, player_names)
                    if hit:
                        print("hit!")
                    elif self.miss is True:
                        self.move_matrix = reset_matrix()
                        self.board.color_matrix_positions_board_one(
                            self.move_matrix, matrix_one)
                        self.confirm_key = 'enter'
                        print('press enter again to finish you round')
                else:
                    self.confirm_key = ''
                    return True, False

            if event.name == 'esc':
                return True, True

            if self.win:
                return True, False
        return False, False

    def update_board(self, move_matrix, matrix_one, matrix_two, player_names):
        """
        Updates the colors of the board and prints the board
        """
        clear_terminal()
        if self.is_bot:
            self.board.color_matrix_positions_board_one(
                move_matrix, matrix_two)
            self.board.color_matrix_positions_board_two(matrix_one)
            self.board.print_double_board(
                player_names['name_one'], player_names['name_two'])
        else:
            self.board.color_matrix_positions_board_one(
                move_matrix, matrix_one)
            self.board.color_matrix_positions_board_two(matrix_two)
            self.board.print_double_board(
                player_names['name_one'], player_names['name_two'])

    def move(self, matrix_one, matrix_two, direction, player_names):
        """
        Updates the player's cursor position on their board based on the given direction.
        """
        if direction == 'up':
            row, col = (self.current_pos[0]-1, self.current_pos[1])
            if row > 0:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row, col)
                self.update_board(self.move_matrix, matrix_one,
                                  matrix_two, player_names)
                return
        if direction == 'down':
            row, col = (self.current_pos[0]+1, self.current_pos[1])
            if row <= 10:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row, col)
                self.update_board(self.move_matrix, matrix_one,
                                  matrix_two, player_names)
                return
        if direction == 'left':
            row, col = (self.current_pos[0], self.current_pos[1]-1)
            if col > 0:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row, col)
                self.update_board(self.move_matrix, matrix_one,
                                  matrix_two, player_names)
                return
        if direction == 'right':
            row, col = (self.current_pos[0], self.current_pos[1]+1)
            if col <= 10:
                self.move_matrix = reset_matrix()
                self.move_matrix[row][col] = 3
                self.current_pos = (row, col)
                self.update_board(self.move_matrix, matrix_one,
                                  matrix_two, player_names)
                return

    def mark_destroyed_boat(self, matrix, row, col):
        """
        Given a matrix, the row and column of a destroyed boat,
        mark all other positions of the boat with 7 without going out of index.
        """
        # check if the boat is vertical or horizontal
        if matrix[row][col] == 7 and ((row-1 >= 0 and matrix[row-1][col] == 6) or (row+1 <= 9 and matrix[row+1][col] == 6)):
            # the boat is vertical, mark all other positions of the boat with 7
            start_row = row
            while start_row > 0 and matrix[start_row-1][col] == 6:
                start_row -= 1
            end_row = row
            while end_row < 10 and matrix[end_row+1][col] == 6:
                end_row += 1
            for i in range(start_row, end_row+1):
                matrix[i][col] = 7
        else:
            # the boat is horizontal, mark all other positions of the boat with 7
            start_col = col
            while start_col > 0 and matrix[row][start_col-1] == 6:
                start_col -= 1
            end_col = col
            while end_col < 10 and matrix[row][end_col+1] == 6:
                end_col += 1
            for j in range(start_col, end_col+1):
                matrix[row][j] = 7

    def check_for_game_ending(self, value_matrix):
        """
        checks if there are still undestroyed boats on the board
        """
        for row in range(11):
            for col in range(11):
                if value_matrix[row][col] == 2:
                    return False
        self.win = True
        return True

    def mark_destroyed_boat_surrounding(self, value_matrix):
        """
        marks the surrounding of a destroyed boat in the matrix
        """
        for row in range(11):
            for col in range(11):
                if value_matrix[row][col] == 7:
                    if row-1 > 0 and col-1 > 0 and value_matrix[row-1][col-1] != 7:
                        value_matrix[row-1][col-1] = 5
                    if row-1 > 0 and value_matrix[row-1][col] != 7:
                        value_matrix[row-1][col] = 5
                    if row-1 > 0 and col+1 <= 10 and value_matrix[row-1][col+1] != 7:
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

    def check_for_destroyed_boats(self, row, col, value_matrix):
        """
        checks if a boat is destroyed
        """
        # Find the starting and ending positions of the boat in the same row.
        start_col = col
        while start_col > 0 and value_matrix[row][start_col - 1] in (2, 6):
            start_col -= 1
        end_col = col
        while end_col < 10 and value_matrix[row][end_col + 1] in (2, 6):
            end_col += 1

        # Find the starting and ending positions of the boat in the same column.
        start_row = row
        while start_row > 0 and value_matrix[start_row - 1][col] in (2, 6):
            start_row -= 1
        end_row = row
        while end_row < 10 and value_matrix[end_row + 1][col] in (2, 6):
            end_row += 1

        # Check if all the positions between the starting and ending positions have been hit.
        for i in range(start_col, end_col + 1):
            if value_matrix[row][i] == 2:
                return False
        for i in range(start_row, end_row + 1):
            if value_matrix[i][col] == 2:
                return False
        value_matrix[row][col] = 7
        self.mark_destroyed_boat(value_matrix, row, col)
        self.mark_destroyed_boat_surrounding(value_matrix)
        self.check_for_game_ending(value_matrix)
        return False

    def attack(self, value_matrix, matrix_two, player_names):
        """
        function for attacking the enemy with the position of the cursor
        """
        row, col = (self.current_pos[0], self.current_pos[1])
        if value_matrix[row][col] == 5 or value_matrix[row][col] == 6:
            self.miss = False
            return False
        if value_matrix[row][col] == 0 or value_matrix[row][col] == 1:
            value_matrix[row][col] = 5
            self.miss = True
            self.update_board(self.move_matrix, value_matrix,
                              matrix_two, player_names)
            return False
        if value_matrix[row][col] == 2:
            value_matrix[row][col] = 6
            self.miss = False
            self.check_for_destroyed_boats(row, col, value_matrix)
            self.update_board(self.move_matrix, value_matrix,
                              matrix_two, player_names)
            return True
        return False

    def bot(self, matrix_player, matrix_bot, player_names):
        """
        function for bot playing the game
        """
        while self.miss is False:
            self.current_pos = [(random.randint(1, 10)),
                                (random.randint(1, 10))]
            self.attack(matrix_bot, matrix_player, player_names)
        return True

    def save_game(self, gamemode, game_params, filename='save.json'):
        """
        Clear the existing game parameters in the JSON file at id 1 and save the provided game_params.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                game_params_list = json.load(file)
        except json.decoder.JSONDecodeError:
            # If the file is empty or invalid JSON, create an empty list of game parameters
            game_params_list = []

            # Find the game parameters with id 1
        for params in game_params_list:
            if params['gamemode'] == 1 and gamemode == 1:
                # Clear the existing game parameters and replace them with the new ones
                params.clear()
                params.update(game_params)
                break
            if params['gamemode'] == 2 and gamemode == 2:
                # Clear the existing game parameters and replace them with the new ones
                params.clear()
                params.update(game_params)
                break
        else:
            # If no game parameters with id 1 were found, add the new parameters to the list
            game_params_list.append(game_params)

            # Save the updated game parameters to the file
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(game_params_list, file)
            print("Saved")
            time.sleep(1)

    def delete_save(self, gamemode, filename='save.json'):
        """""
            Deletes saved game after the game is finished
        """""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                game_params_list = json.load(file)
        except json.decoder.JSONDecodeError:
            # If the file is empty or invalid JSON, create an empty list of game parameters
            game_params_list = []

        for params in game_params_list:
            if params['gamemode'] == gamemode:
                game_params_list.remove(params)
                print(f"Removed game parameters for gamemode {gamemode}")
                break
        else:
            print(f"No game parameters found for gamemode {gamemode}")

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(game_params_list, file)

    def display_text(self, option, player_names, player_one_turn, exit_game):
        """
        displays which user starts the game and waits for enter to be pressed
        """
        if option == 0:
            clear_terminal()
            if player_one_turn:
                print(
                    f"{player_names['name_one']} is starting! \nPress 'Enter' to show Boards")
            else:
                print(
                    f"{player_names['name_two']} is starting! \nPress 'Enter' to show Boards")

            keyboard.wait('enter')
            return
        if option == 1:
            if not self.win and not exit_game:
                clear_terminal()
                print(f"{player_names['name_one']}`s turn! \nPress 'enter' to show Boards")
                keyboard.wait('enter')
                return
        if option == 2:
            if not self.win and not exit_game:
                clear_terminal()
                print(f"{player_names['name_one']}`s turn! \nPress 'enter' to show Boards")
                keyboard.wait('enter')
                return
        if option == 3:
            clear_terminal()
            if player_one_turn:
                print(f"And the winner of this game is: {player_names['name_two']}")
            else:
                print(f"And the winner of this game is: {player_names['name_two']}")
            print("\n\n\nPress 'enter' to continue.")
            keyboard.wait('enter')
            return

    def singleplayer(self, player_one_name, player_two_name, player_two_matrix, player_one_matrix):
        """
        function for playing singleplayer with the given args
        """
        self.move_matrix[1][1] = 3
        player_names = {
            'name_one': player_one_name,
            'name_two': player_two_name
        }
        self.update_board(self.move_matrix, player_one_matrix,
                          player_two_matrix, player_names)
        player_one_turn = random.randint(1, 2)
        game_round = False
        exit_game = False

        while True:
            if player_one_turn == 1:
                self.move_matrix[1][1] = 3
                self.is_bot = False
                while game_round is False:
                    self.update_board(
                        self.move_matrix, player_one_matrix, player_two_matrix, player_names)
                    game_round, exit_game = self.handle_keyboard_event(
                        player_one_matrix, player_two_matrix, player_names)
                player_one_turn = 2
                game_round = False
                self.miss = False
                self.current_pos = (1, 1)
            else:
                while game_round is False:
                    self.is_bot = True
                    self.update_board(
                        self.move_matrix, player_two_matrix, player_one_matrix, player_names)
                    game_round = self.bot(
                        player_one_matrix, player_two_matrix, player_names)
                    print(self.miss)
                player_one_turn = 1
                game_round = False
                self.miss = False
                self.current_pos = (1, 1)

            if self.win:
                self.win = False
                print("Game over!")
                time.sleep(1)
                self.delete_save(1)
                return
            if exit_game:
                game_params = {
                    'gamemode': 1,
                    'player_name_one': player_one_name,
                    'player_name_two': player_two_name,
                    'player_matrix_one': player_one_matrix,
                    'player_matrix_two': player_two_matrix,
                    'starting_player': player_one_turn
                }
                self.save_game(1, game_params)
                print("Saved")
                time.sleep(1)
                break



    def multiplayer(self, player_one_name, player_two_name, player_two_matrix, player_one_matrix):
        """
        function for playing multiplayer with the given args
        """
        self.move_matrix[1][1] = 3
        player_one_turn = random.choice([True, False])
        game_round = False
        exit_game = False
        player_names = {
                    'name_one': player_one_name,
                    'name_two': player_two_name
                }

        self.display_text(0, player_names, player_one_turn, exit_game)

        while True:
            if player_one_turn:
                player_names = {
                    'name_one': player_two_name,
                    'name_two': player_one_name
                }
                self.move_matrix[1][1] = 3
                while game_round is False:
                    self.update_board(
                        self.move_matrix, player_one_matrix, player_two_matrix, player_names)
                    game_round, exit_game = self.handle_keyboard_event(
                        player_one_matrix, player_two_matrix, player_names)
                player_one_turn = False
                game_round = False
                self.miss = False
                self.current_pos = (1, 1)
                if exit_game is False:
                    self.display_text(1, player_names, player_one_turn, exit_game)
            else:
                player_names = {
                    'name_one': player_one_name,
                    'name_two': player_two_name
                }
                self.move_matrix[1][1] = 3
                while game_round is False:
                    self.update_board(
                        self.move_matrix, player_two_matrix, player_one_matrix, player_names)
                    game_round, exit_game = self.handle_keyboard_event(
                        player_two_matrix, player_one_matrix, player_names)
                player_one_turn = True
                game_round = False
                self.miss = False
                self.current_pos = (1, 1)
                if exit_game is False:
                    self.display_text(2, player_names, player_one_turn, exit_game)

            if self.win:
                print("Game over!")
                time.sleep(1)
                self.delete_save(2)
                self.display_text(3, player_names, player_one_turn, exit_game)
                self.win = False
                return
            if exit_game:
                game_params = {
                    'gamemode': 2,
                    'player_name_one': player_one_name,
                    'player_name_two': player_two_name,
                    'player_matrix_one': player_one_matrix,
                    'player_matrix_two': player_two_matrix,
                    'starting_player': player_one_turn
                }
                self.save_game(2, game_params)
                time.sleep(1)
                break