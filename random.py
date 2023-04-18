import random

# Initialize a 10x10 matrix with zeros
matrix = [[0 for j in range(10)] for i in range(10)]

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
            if col+i < 10 and matrix[row][col] == 1:
                return False
            if col+i < 10 and matrix[row][col+i] == 1:
                return False
            if col+i > 0 and matrix[row][col+i-1] == 1:
                return False
        elif direction == 'vertical':
            if row+i < 10 and matrix[row][col] == 1:
                return False
            if row+i < 10 and matrix[row+i][col] == 1:
                return False
            if row+i > 0 and matrix[row+i-1][col] == 1:
                return False
    # Check if the boat would touch another boat
    for i in range(size+1):
        if direction == 'horizontal':
            if row > 0 and col+i < 10 and matrix[row-1][col+i] == 1:
                return False
            if row < 9 and col+i < 10 and matrix[row+1][col+i] == 1:
                return False
            if col+i > 0 and row > 0 and matrix[row-1][col+i-1] == 1:
                return False
            if col+i > 0 and row < 9 and matrix[row+1][col+i-1] == 1:
                return False
        elif direction == 'vertical':
            if row+i < 10 and col > 0 and matrix[row+i][col-1] == 1:
                return False
            if row+i < 10 and col < 9 and matrix[row+i][col+1] == 1:
                return False
            if row > 0 and col > 0 and matrix[row+i-1][col-1] == 1:
                return False
            if row > 0 and col < 9 and matrix[row+i-1][col+1] == 1:
                return False
    # If all checks pass, the boat can be placed
    return True


# Place the boats
# Place the boats
attempts = 0
while True:
    # Remove all boats from the matrix
    matrix = [[0 for j in range(10)] for i in range(10)]
    for size in boat_sizes:
        placed = False
        while not placed:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            direction = random.choice(['horizontal', 'vertical'])
            if can_place_boat(matrix, row, col, size, direction):
                for i in range(size):
                    if direction == 'horizontal':
                        matrix[row][col+i] = 1
                    else:
                        matrix[row+i][col] = 1
                placed = True
            else:
                # Generate new random position and direction for the boat
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                direction = random.choice(['horizontal', 'vertical'])
    # Check if all boats were placed and exit loop if so
    if all([size == sum(row) for row in matrix] for size in boat_sizes):
        break
    attempts += 1
    if attempts >= 1000:
        print("Too many attempts, restarting...")


# Print the matrix
for row in matrix:
    print(' '.join(map(str, row)))


