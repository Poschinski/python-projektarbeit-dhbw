"""""
    Testing board.py
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
from board import *


class BoardTests(unittest.TestCase):
    """""
        Testing various functions of board.py
    """""

    def test_color_matrix_positions_boat_setup(self):
        """""
            Testing if matrix colors are corresponding with the boats
        """""
        board = Board()
        move_matrix = [[0 for _ in range(11)] for _ in range(11)]
        value_matrix = [[0 for _ in range(11)] for _ in range(11)]
        move_matrix[1][1] = 3
        value_matrix[1][1] = 2

        board.color_matrix_positions_boat_setup(move_matrix, value_matrix)

        # Check that the display matrix was updated correctly
        self.assertEqual(board.display_matrix[1][1], 4)

        # Check that the board1 matrix was updated correctly
        self.assertEqual(board.board1[1][1], '\x1b[101m   \x1b[0m |')


if __name__ == '__main__':
    unittest.main()
