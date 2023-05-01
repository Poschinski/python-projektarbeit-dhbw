"""
jsdnaskd
"""

import os
import random


def clear_terminal():
    """
    This function clears the terminal screen to improve the user interface.
    It works differently for Windows and Unix-based systems.
    """
    if os.name == 'posix':  # for Mac and Linux
        os.system('clear')
    elif os.name == 'nt':  # for Windows
        os.system('cls')

def create_matrix():
    """
    This function creates and returns a 11x11 matrix filled with zeros.
    """
    new_matrix = [[0 for _ in range(11)] for _ in range(11)]
    return new_matrix

def reset_matrix():
    """
    This function can be used to reset the game board before starting a new game.
    It creates and retruns a 11x11 matrix filled with zeros.
    """
    new_matrix = [[0 for _ in range(11)] for _ in range(11)]
    return new_matrix

def is_within_bounds(row, col, length, direction):
    """
    This function checks if a ship of a given length starting at a given
    row and column and oriented in a given direction can fit within the boundaries of the game board.
    It returns True if the ship can fit and False otherwise.
    """
    if direction == 'horizontal' and col + length > 10:
        return False
    if direction == 'vertical' and row + length > 10:
        return False
    return True

def does_not_overlap(matrix, row, col, length, direction):
    """
    This function checks if a ship of a given length can be placed on a given coordinate of a matrix in a given direction
    without overlapping with other ships already placed in the matrix.
    It returns True if it is safe to place the ship on the given coordinate, otherwise returns False.
    """
    can_place = True
    for i in range(length+1):
        if direction == 'horizontal':
            if matrix[row][col] == 2:
                can_place = False
            if col+i <= 10 and matrix[row][col+i] == 2:
                can_place = False
            if col+i > 0 and matrix[row][col-1] == 2:
                can_place = False
        elif direction == 'vertical':
            if matrix[row][col] == 2:
                can_place = False
            if row+i <= 10 and matrix[row+i][col] == 2:
                can_place = False
            if row+i > 0 and matrix[row-1][col] == 2:
                can_place = False
        if not can_place:
            return False
    return True

def does_not_touch_horizontal(matrix, row, col, length):
    """
    This function checks whether a horizontal ship of a given length starting at a given position (row, col) would touch another ship on the game board.
    If there is no ship directly above, below, or adjacent to the given position, the function returns True,
    indicating that the ship would not touch any other ships if placed at that position.
    If there is a ship directly above, below, or adjacent to the given position, the function returns False,
    indicating that the ship would touch another ship if placed at that position.
    """
    for i in range(length+2):
        if row-1 > 0 and col+i <= 10 and matrix[row-1][col+i] == 2:
            return False
        if row+1 <= 10 and col+i <= 10 and matrix[row+1][col+i] == 2:
            return False
        if col-1 > 0 and row-1 > 0 and matrix[row-1][col-1] == 2:
            return False
        if col-1 > 0 and row+1 <= 10 and matrix[row+1][col-1] == 2:
            return False
    return True

def does_not_touch_vertical(matrix, row, col, length):
    """
    Checks if a ship of the given length starting at the given row and column in a vertical direction
    does not touch any existing ships in the matrix.
    """
    for i in range(length+2):
        if row+i <= 10 and col-1 > 0 and matrix[row+i][col-1] == 2:
            return False
        if row+i <= 10 and col+1 <= 10 and matrix[row+i][col+1] == 2:
            return False
        if row-1 > 0 and col-1 > 0 and matrix[row-1][col-1] == 2:
            return False
        if row-1 > 0 and col+1 <= 10 and matrix[row-1][col+1] == 2:
            return False
    return True


def can_place_boat(matrix, row, col, length, direction):
    """
    Check if it's possible to place a boat of given length and direction at the given row and column position in the matrix.
    The function returns True if the boat can be placed without overlapping with other boats or touching them horizontally and vertically,
    and without going out of bounds of the matrix.

    """
    if not is_within_bounds(row, col, length, direction):
        return False
    if not does_not_overlap(matrix, row, col, length, direction):
        return False
    if not does_not_touch_horizontal(matrix, row, col, length):
        return False
    if not does_not_touch_vertical(matrix, row, col, length):
        return False
    return True

def add_surrounding_horizonal(random_matrix, row, col, length, i):
    """
    This function adds the value 1 arroud the placed boat without going out of index.
    """
    if row-1 > 0 and col+i <= 10:
        random_matrix[row-1][col+i] = 1 #top line
    if row+1 <= 10 and col+i <= 10:
        random_matrix[row+1][col+i] = 1 #bottom line
    if col-1 > 0:
        random_matrix[row][col-1] = 1 #left
    if col+length <= 10 and i==1:
        random_matrix[row][col+length] = 1 #right
    if col-1 > 0 and row-1 > 0:
        random_matrix[row-1][col-1] = 1 #top left
    if col-1 > 0 and row+1 <= 10:
        random_matrix[row+1][col-1] = 1 #bottom left
    if col+length <= 10 and row-1 > 0 and i==1:
        random_matrix[row-1][col+length] = 1 #top right
    if col+length <= 10 and row+1 <= 10 and i==1:
        random_matrix[row+1][col+length] = 1 #bottom right

def add_surrounding_vertical(random_matrix, row, col, length, i):
    """
    This function adds the value 1 arroud the placed boat without going out of index.
    """
    if row+i <= 10 and col+1 <= 10:
        random_matrix[row+i][col+1] = 1 #right line
    if row+i <= 10 and col-1 > 0:
        random_matrix[row+i][col-1] = 1 #left line
    if row-1 > 0:
        random_matrix[row-1][col] = 1 #top
    if row+length <= 10 and i==1:
        random_matrix[row+length][col] = 1 #bottom
    if col-1 > 0 and row-1 > 0:
        random_matrix[row-1][col-1] = 1 #top left
    if col-1 > 0 and row+length <= 10 and i == 1:
        random_matrix[row+length][col-1] = 1 #bottom left
    if col+1 <= 10 and row-1 > 0:
        random_matrix[row-1][col+1] = 1 #top right
    if col+1 <= 10 and row+length <= 10 and i==1:
        random_matrix[row+length][col+1] = 1 #bottom right

def random_boat_setup():
    """
    This function creates a random boat setup. Its returning a random matrix with the given rules.
    The matrix is filled with ones, twos and zeros.
    """
    random_matrix = create_matrix()
    lengths = [5,4,3,2]
    ammounts = [1,2,3,4]

    def place_boat(matrix, row, col, length, direction):
        for i in range(length):
            if direction == 'horizontal':
                matrix[row][col+i] = 2
                add_surrounding_horizonal(matrix, row, col, length, i)
            else:
                matrix[row+i][col] = 2
                add_surrounding_vertical(matrix, row, col, length, i)

    def generate_random_position():
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        direction = random.choice(['horizontal', 'vertical'])
        return row, col, direction

    # Place the boats
    while True:
        # Remove all boats from the matrix
        attempts = 0
        for index, length in enumerate(lengths):
            for _ in range(ammounts[index]):
                placed = False
                while not placed and attempts < 1000:
                    row, col, direction = generate_random_position()
                    if can_place_boat(random_matrix, row, col, length, direction):
                        place_boat(random_matrix, row, col, length, direction)
                        ammounts[index] -= 1
                        placed = True
                    else:
                        attempts += 1
                if attempts >= 1000:
                    # If we had to start over, exit inner loop
                    random_matrix = create_matrix()
                    ammounts = [1,2,3,4]
            if attempts >= 1000:
                break
        if attempts < 1000 and all([length == sum(row) for row in random_matrix] for length in lengths):
            break
    return random_matrix
