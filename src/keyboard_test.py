import keyboard
import os

def clear_terminal():
    if os.name == 'posix':  # for Mac and Linux
        os.system('clear')
    elif os.name == 'nt':  # for Windows
        os.system('cls')

# create two matrices: one for the values and one for the X position
value_matrix = [[0 for _ in range(10)] for _ in range(10)]
move_matrix = [[0 for _ in range(10)] for _ in range(10)]
move_matrix[0][0] = "X"  # initialize the X position
current_pos = (0, 0)

# function to print the matrix
def print_matrix():
    display_matrix = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if move_matrix[i][j] == 'X':
                display_matrix[i][j] = 'X'
            else:
                display_matrix[i][j] = value_matrix[i][j]
    for row in display_matrix:
        print(row)

# function to update the current position of the X
def update_position(new_pos):
    global current_pos
    x, y = new_pos
    if x < 0 or x >= 10 or y < 0 or y >= 10:
        return
    move_matrix[current_pos[0]][current_pos[1]] = 0  # reset the current position to 0
    move_matrix[x][y] = "X"  # update the new position
    current_pos = new_pos
    clear_terminal()
    print_matrix()

# function to change the value at the current position
def change_value():
    global value_matrix
    x, y = current_pos
    value_matrix[x][y] = 1
    clear_terminal()
    print_matrix()

clear_terminal()
print_matrix()

# loop to handle arrow key and enter key events
while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        if event.name == 'up':
            update_position((current_pos[0]-1, current_pos[1]))
        elif event.name == 'down':
            update_position((current_pos[0]+1, current_pos[1]))
        elif event.name == 'left':
            update_position((current_pos[0], current_pos[1]-1))
        elif event.name == 'right':
            update_position((current_pos[0], current_pos[1]+1))
        elif event.name == 'enter':
            change_value()
        elif event.name == 'esc':
            break  # exit the loop if the 'esc' key is pressed
