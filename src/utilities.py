"""
jsdnaskd
"""

import os
import random


def clear_terminal():
    """
    jsdnaskd
    """
    if os.name == 'posix':  # for Mac and Linux
        os.system('clear')
    elif os.name == 'nt':  # for Windows
        os.system('cls')

def create_matrix():
    """
    jsdnaskd
    """
    new_matrix = [[0 for _ in range(11)] for _ in range(11)]
    return new_matrix

def reset_matrix():
    """
    sadas
    """
    new_matrix = [[0 for _ in range(11)] for _ in range(11)]
    return new_matrix

def is_within_bounds(row, col, length, direction):
    """
    jsdnaskd
    """
    if direction == 'horizontal' and col + length > 10:
        return False
    if direction == 'vertical' and row + length > 10:
        return False
    return True

def does_not_overlap(matrix, row, col, length, direction):
    """
    jsdnaskd
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
    jsdnaskd
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
    jsdnaskd
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
    jsdnaskd
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
    jsdnaskd
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
    jsdnaskd
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
    jsdnaskd
    """
    random_matrix = create_matrix()
    lengths = [5,4,3,2]#boat_lengths
    ammounts = [1,2,3,4] #boat_ammount

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
