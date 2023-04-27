import unittest
import sys
sys.path.append("..")
import src.utilities as utilities


class MyTestCase(unittest.TestCase):
    def test_out_of_bounds_horizontal(self):
        matrix = [[0] * 11 for _ in range(11)]
        self.assertFalse(utilities.can_place_boat(matrix, 3, 8, 3, 'horizontal'))

    def test_out_of_bounds_vertical(self):
        matrix = [[0] * 11 for _ in range(11)]
        self.assertFalse(utilities.can_place_boat(matrix, 8, 3, 4, 'vertical'))

    def test_overlap_horizontal(self):
        matrix = [[0] * 11 for _ in range(11)]
        matrix[3][5] = 2
        matrix[3][6] = 2
        self.assertFalse(utilities.can_place_boat(matrix, 3, 4, 3, 'horizontal'))

    def test_overlap_vertical(self):
        matrix = [[0] * 11 for _ in range(11)]
        matrix[2][2] = 2
        matrix[3][2] = 2
        self.assertFalse(utilities.can_place_boat(matrix, 1, 2, 3, 'vertical'))

    def test_touching_horizontal(self):
        matrix = [[0] * 11 for _ in range(11)]
        matrix[4][6] = 2
        matrix[3][7] = 2
        self.assertFalse(utilities.can_place_boat(matrix, 4, 4, 4, 'horizontal'))

    def test_touching_vertical(self):
        matrix = [[0] * 11 for _ in range(11)]
        matrix[3][3] = 2
        matrix[2][3] = 2
        self.assertFalse(utilities.can_place_boat(matrix, 4, 4, 3, 'vertical'))

    def test_valid_horizontal(self):
        matrix = [[0] * 11 for _ in range(11)]
        self.assertTrue(utilities.can_place_boat(matrix, 3, 4, 3, 'horizontal'))

    def test_valid_vertical(self):
        matrix = [[0] * 11 for _ in range(11)]
        self.assertTrue(utilities.can_place_boat(matrix, 5, 7, 2, 'vertical'))

    def test_boat_overlap(self):
        board = utilities.random_boat_setup()
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
