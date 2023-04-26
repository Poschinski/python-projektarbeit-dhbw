import os
import random
import sys

sys.path.append("../src")

from config import boat_lengths, boat_ammount


def clear_terminal():
    if os.name == 'posix':  # for Mac and Linux
        os.system('clear')
    elif os.name == 'nt':  # for Windows
        os.system('cls')

def create_matrix():
    create_matrix = [[0 for _ in range(11)] for _ in range(11)]
    return create_matrix

def reset_matrix():
    reset_matrix = [[0 for _ in range(11)] for _ in range(11)]
    return reset_matrix


def can_place_boat(matrix, row, col, length, direction):
    # Check if the boat would go out of bounds
    if direction == 'horizontal' and col + length > 10:
        return False
    if direction == 'vertical' and row + length > 10:
        return False
    # Check if the boat would overlap with another boat
    for i in range(length+1):
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
    for i in range(length+1):
        if direction == 'horizontal':
            if row-1 > 0 and col+i <= 10 and matrix[row-1][col+i] == 2:
                return False
            if row+1 <= 10 and col+i <= 10 and matrix[row+1][col+i] == 2:
                return False
            if col-1 > 0 and row-1 > 0 and matrix[row-1][col-1] == 2:
                return False
            if col-1 > 0 and row+1 <= 10 and matrix[row+1][col-1] == 2:
                return False
        elif direction == 'vertical':
            if row+i <= 10 and col-1 > 0 and matrix[row+i][col-1] == 2:
                return False
            if row+i <= 10 and col+1 <= 10 and matrix[row+i][col+1] == 2:
                return False
            if row-1 > 0 and col-1 > 0 and matrix[row-1][col-1] == 2:
                return False
            if row-1 > 0 and col+1 <= 10 and matrix[row-1][col+1] == 2:
                return False
    # If all checks pass, the boat can be placed
    return True

def random_boat_setup():
    random_matrix = create_matrix()
    lengths = [5,4,3,2]#boat_lengths
    ammounts = [1,2,3,4] #boat_ammount
    # Place the boats
    while True:
        # Remove all boats from the matrix
        attempts = 0
        for index, length in enumerate(lengths):
            for _ in range(ammounts[index]):
                placed = False
                while not placed and attempts < 1000:
                    row = random.randint(1, 10)
                    col = random.randint(1, 10)
                    direction = random.choice(['horizontal', 'vertical'])
                    if can_place_boat(random_matrix, row, col, length, direction):
                        for i in range(length):
                            if direction == 'horizontal':
                                random_matrix[row][col+i] = 2
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
                            else:
                                random_matrix[row+i][col] = 2
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
                        ammounts[index] -= 1
                        placed = True
                    else:
                        # Generate new random position and direction for the boat
                        row = random.randint(1, 10)
                        col = random.randint(1, 10)
                        direction = random.choice(['horizontal', 'vertical'])
                        attempts += 1
        # Check if all boats were placed and exit loop if so
        if all([length == sum(row) for row in random_matrix] for length in lengths):
            print(random_matrix)
            break
    return random_matrix


# test = random_boat_setup()
# for row in range(11):
#     print(test[row][0],test[row][1],test[row][2],test[row][3],test[row][4],test[row][5],test[row][6],test[row][7],test[row][8],test[row][9],test[row][10])

