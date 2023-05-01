"""""
    Testing utilities.py
    pylint:
        disabling undefined-variable, wildcard-import, import-error
        because imports work fine, but python doesn't recognise that.
        Because imports are seen as wrong, functions of the import are also seen as undefined
"""""
# pylint: disable=C
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=import-error
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from utilities import *


class UtilitiesTestCase(unittest.TestCase):
    """""
        Testing various functions of utilities.py
    """""

    def test_out_of_bounds_horizontal(self):
        """""
            Tests the placement of a horizontal boat out of bounds
        """""
        matrix = create_matrix()
        self.assertFalse(can_place_boat(matrix, 3, 8, 3, 'horizontal'))

    def test_out_of_bounds_vertical(self):
        """""
            Tests the placement of a vertical boat out of bounds
        """""
        matrix = create_matrix()
        self.assertFalse(can_place_boat(matrix, 8, 3, 4, 'vertical'))

    def test_overlap_horizontal(self):
        """""
            Tests the placement of a overlapping horizontal boat
        """""
        matrix = create_matrix()
        matrix[3][5] = 2
        matrix[3][6] = 2
        self.assertFalse(can_place_boat(matrix, 3, 4, 3, 'horizontal'))

    def test_overlap_vertical(self):
        """""
            Tests the placement of a overlapping vertical boat
        """""
        matrix = create_matrix()
        matrix[2][2] = 2
        matrix[3][2] = 2
        self.assertFalse(can_place_boat(matrix, 1, 2, 3, 'vertical'))

    def test_touching_horizontal(self):
        """""
            Tests the placement of a touching horizontal boat
        """""
        matrix = create_matrix()
        matrix[4][6] = 2
        matrix[3][7] = 2
        self.assertFalse(can_place_boat(matrix, 4, 4, 4, 'horizontal'))

    def test_touching_vertical(self):
        """""
            Tests the placement of a touching vertical boat
        """""
        matrix = create_matrix()
        matrix[3][3] = 2
        matrix[2][3] = 2
        self.assertFalse(can_place_boat(matrix, 4, 4, 3, 'vertical'))

    def test_valid_horizontal(self):
        """""
            Tests the placement of a horizontal boat
        """""
        matrix = create_matrix()
        self.assertTrue(can_place_boat(matrix, 3, 4, 3, 'horizontal'))

    def test_valid_vertical(self):
        """""
            Tests the placement of a vertical boat
        """""
        matrix = create_matrix()
        self.assertTrue(can_place_boat(matrix, 5, 7, 2, 'vertical'))

    def test_boat_overlap(self):
        """""
            Tests if the random_boat_setup overlaps 
        """""
        board = random_boat_setup()
        for i in range(11):
            for j in range(11):
                if board[i][j] == 2:
                    # Check for any overlapping boats horizontally
                    if (j < 10 and board[i][j + 1] == 2) or board[i][j - 1] == 2:
                        if i < 10 and board[i + 1][j] == 2 and board[i - 1][j] == 2:
                            self.fail("Boats are overlapping")
                        elif i == 10 and board[i - 1][j] == 2:
                            self.fail("Boats are overlapping")
                    elif (i < 10 and board[i + 1][j] == 2) or board[i - 1][j] == 2:
                        if j < 10 and board[i][j + 1] == 2 and board[i][j - 1] == 2:
                            self.fail("Boats are overlapping")
                        elif j == 10 and board[i][j - 1] == "":
                            self.fail("Boats are overlapping")


if __name__ == '__main__':
    unittest.main()
