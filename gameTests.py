import unittest
from game import GameSetup
import utilities


class GameTests(unittest.TestCase):
    def test_update_position_horizontal_valid(self):
        setup = GameSetup()
        setup.update_position([2, 1], False, 2)
        self.assertEqual(setup.current_pos, [2, 1])
        self.assertEqual(setup.direction, "horizontal")
        matrix = utilities.create_matrix()
        matrix[2][1] = 3
        matrix[2][2] = 3
        self.assertEqual(setup.move_matrix, matrix)

    def test_update_position_vertical_valid(self):
        game = GameSetup()
        game.direction = "vertical"
        game.update_position([1, 2], True, 2)
        self.assertEqual(game.current_pos, [1, 2])
        game.changed_direction = True
        self.assertEqual(game.direction, "vertical")
        matrix = utilities.create_matrix()
        matrix[1][2] = 3
        matrix[2][2] = 3
        self.assertEqual(game.move_matrix, matrix)

    def setUp(self):
        self.setup = GameSetup()

    def test_change_value_returns_false_if_boat_overlap(self):
        # Set up
        self.setup.value_matrix[1][1] = 1
        self.setup.current_pos = [1, 1]
        self.setup.direction = "horizontal"
        # Test
        self.assertFalse(self.setup.change_value(3, "horizontal"))

    def test_change_value_updates_value_matrix_and_returns_true(self):
        # Set up
        self.setup.current_pos = [1, 1]
        self.setup.direction = "horizontal"
        # Test
        self.assertTrue(self.setup.change_value(3, "horizontal"))
        expected_value_matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.setup.value_matrix, expected_value_matrix)

    def test_reset_boat_setup(self):
        game_setup = GameSetup()
        game_setup.move_matrix[3][3] = 1
        game_setup.value_matrix[3][3] = 2
        game_setup.all_boats_placed = True
        game_setup.direction = "vertical"

        game_setup.reset_boat_setup()
        matrix1 = utilities.create_matrix()
        for i in range(5):
            matrix1[1][1+i] = 3

        matrix2 = utilities.create_matrix()
        self.assertEqual(game_setup.move_matrix, matrix1)
        self.assertEqual(game_setup.value_matrix, matrix2)
        self.assertEqual(game_setup.all_boats_placed, False)
        self.assertEqual(game_setup.direction, "horizontal")


if __name__ == '__main__':
    unittest.main()
