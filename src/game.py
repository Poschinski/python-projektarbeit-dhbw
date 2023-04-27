"""
    Code Description
"""
import keyboard
from src.utilities import clear_terminal, create_matrix, reset_matrix, random_boat_setup
from src.config import boat_ammount, boat_lengths
from src.board import Board


class GameSetup:
    """
    Class Description
    """

    def __init__(self):
        self.board = Board()
        self.current_pos = [1, 1]
        self.current_boat = 0
        self.ammount = boat_ammount
        self.lengths = boat_lengths
        self.selected_boat = 0
        self.direction = "horizontal"
        self.changed_direction = False
        self.all_boats_placed = False
        self.value_matrix = create_matrix()
        self.move_matrix = create_matrix()
        for i in range(5):
            self.move_matrix[1][1+i] = 3


    def update_position(self, new_pos, changed_direction, boat_length):
        """
        function for updating the current boat position 
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
        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount)



    def change_value(self, boat_length, direction):
        """
        update value_matrix
        """
        row, col = self.current_pos
        if direction == "horizontal":
            for i in range(boat_length):
                if self.value_matrix[row][col+i] == 1 or self.value_matrix[row][col+i] == 2:
                    return False
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
                if self.value_matrix[row+i][col] == 1 or self.value_matrix[row+i][col] == 2:
                    return False
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
        self.board.print_single_board(self.ammount)
        return True

    def reset_boat_setup(self):
        """
        reset the boat setup to start again
        """
        self.value_matrix = reset_matrix()
        self.move_matrix = reset_matrix()
        for i in range(5):
            self.move_matrix[1][1+i] = 3
        self.all_boats_placed = False
        self.direction = "horizontal"
        clear_terminal()
        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount)

    def setup_boats(self):
        """
        method for setting up boats 
        """
        clear_terminal()
        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
        self.board.print_single_board(self.ammount)
        while True:
            event = keyboard.read_event()
            changed_direction = False
            self.all_boats_placed = all(amount == 0 for amount in self.ammount)
            if not self.all_boats_placed:
                for i, amount in enumerate(self.ammount):
                    if amount != 0:
                        length = self.lengths[i]
                        self.selected_boat = i
                        break
            else:
                for i, row in enumerate(self.move_matrix):  #reset all position
                    for j, _ in enumerate(row):
                        self.move_matrix[i][j] = 0
                clear_terminal()
                self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
                self.board.print_single_board(self.ammount)

            if event.event_type == 'down':
                if self.all_boats_placed is False:
                    if event.name in ('up', 'nach-oben'):
                        self.update_position((self.current_pos[0]-1, self.current_pos[1]),changed_direction, length)
                    elif event.name in ('down', 'nach-unten'):
                        self.update_position((self.current_pos[0]+1, self.current_pos[1]),changed_direction, length)
                    elif event.name in ('left', 'nach-links'):
                        self.update_position((self.current_pos[0], self.current_pos[1]-1),changed_direction, length)
                    elif event.name in ('right', 'nach-rechts'):
                        self.update_position((self.current_pos[0], self.current_pos[1]+1),changed_direction, length)
                    elif event.name == 'enter':
                        check = self.change_value(length, self.direction)
                        if check is True:
                            self.ammount[self.selected_boat] -= 1
                            clear_terminal()
                        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
                        self.board.print_single_board(self.ammount)
                    elif event.name in ('shift', 'umschalt'):
                        changed_direction = True
                        if self.direction == "horizontal":
                            self.direction = "vertical"
                            self.update_position((self.current_pos[0], self.current_pos[1]),changed_direction, length)
                        else:
                            self.direction = "horizontal"
                            self.update_position((self.current_pos[0], self.current_pos[1]),changed_direction, length)
                    elif event.name == 'r':
                        self.ammount = boat_ammount
                        self.value_matrix = random_boat_setup()
                        self.move_matrix = reset_matrix()
                        for index, _ in enumerate(self.ammount):
                            self.ammount[index] = 0
                        clear_terminal()
                        self.board.color_matrix_positions(self.move_matrix, self.value_matrix)
                        self.board.print_single_board(self.ammount)
                    elif event.name == 's':
                        print("you still have boats to be placed!")
                    elif event.name == 'b':
                        return False
                else:
                    if event.name == 'esc':
                        self.ammount = [1,2,3,4]
                        self.reset_boat_setup()
                        
                        # self.setup_boats()
                    elif event.name == 's':
                        return True and self.value_matrix
                    elif event.name == 'b':
                        return False
                    elif event.name == 'e':
                        exit()



if __name__ == "__main__":
    game = GameSetup()

# test = game.setup_boats()
# print(test)