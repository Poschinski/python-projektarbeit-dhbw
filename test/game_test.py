"""""
    Testing game.py
    /check for destroyed boats gramma
    pylint:
        disabling undefined-variable, wildcard-import, import-error
        because imports work fine, but python doesn't recognise that.
        Because imports are seen as wrong, functions of the import are also seen as undefined
        disabling too-many-public-methods
        because can't have too many methods in a TestCase
"""""
# pylint: disable=C
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=import-error
# pylint: disable=too-many-public-methods
import unittest
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from game import *
from utilities import *


class GameSetupTestCase(unittest.TestCase):
    """""
        Testing various functions of GameSetup class
    """""

    def test_update_position_horizontal_valid(self):
        """""
            Asserting if the new position is correct after moving to a new pos
            using update_position, having a horizontal direction
        """""
        setup = GameSetup()
        setup.update_position([2, 1], False, 2, "player1")
        self.assertEqual(setup.current_pos, [2, 1])
        self.assertEqual(setup.direction, "horizontal")
        matrix = create_matrix()
        matrix[2][1] = 3
        matrix[2][2] = 3
        self.assertEqual(setup.move_matrix, matrix)

    def test_update_position_vertical_valid(self):
        """""
            Asserting if the new position is correct after moving to a new pos
            using update_position, having a vertical direction
        """""
        game = GameSetup()
        game.direction = "vertical"
        game.update_position([1, 2], False, 2, "player1")
        self.assertEqual(game.current_pos, [1, 2])
        self.assertEqual(game.direction, "vertical")
        matrix = create_matrix()
        matrix[1][2] = 3
        matrix[2][2] = 3
        self.assertEqual(game.move_matrix, matrix)

    def test_update_position_with_changed_direction_vertical(self):
        """""
            Asserting if the update_position change the direction if changed_direction == True
            from horizontal to vertical
        """""
        game = GameSetup()
        game.direction = "horizontal"
        game.changed_direction = True
        game.update_position((1, 9), game.changed_direction, 3, "player1")
        self.assertEqual(game.direction, "vertical")

    def test_update_position_with_changed_direction_horizontal(self):
        """""
            Asserting if the update_position change the direction if changed_direction == True
            from vertical to horizontal
        """""
        game = GameSetup()
        game.direction = "vertical"
        game.changed_direction = True
        game.update_position((9, 1), game.changed_direction, 3, "player1")
        self.assertEqual(game.direction, "horizontal")

    def test_add_boat_surrounding_horizontal(self):
        """""
            Asserting if the surrounding of a horizontally placed boat gets marked correctly
            using add_boat_surrounding_horizontal
        """""
        game = GameSetup()
        game.value_matrix = create_matrix()
        game.add_boat_surrounding_horizontal(5, 5, 3, 0)
        expected_matrix = create_matrix()
        expected_matrix[6][4] = 1  # bottom line
        expected_matrix[4][4] = 1  # top line
        expected_matrix[4][5] = 1  # top left
        expected_matrix[6][5] = 1  # bottom left
        expected_matrix[5][4] = 1  # left
        expected_matrix[5][8] = 1  # right
        expected_matrix[4][8] = 1  # top right
        expected_matrix[6][8] = 1  # bottom right
        self.assertEqual(game.value_matrix, expected_matrix)

    def test_add_boat_surrounding_vertical(self):
        """""
            Asserting if the surrounding of a horizontally placed boat gets marked correctly
            using add_boat_surrounding_vertical
        """""
        game = GameSetup()
        game.value_matrix = create_matrix()
        game.add_boat_surrounding_vertical(3, 7, 4, 2)
        expected_matrix = create_matrix()
        expected_matrix[5][6] = 1  # left line
        expected_matrix[5][8] = 1  # right line
        expected_matrix[2][6] = 1  # top left
        expected_matrix[2][8] = 1  # top right
        expected_matrix[2][7] = 1  # top
        expected_matrix[7][7] = 1  # bottom
        expected_matrix[7][6] = 1  # bottom left
        expected_matrix[7][8] = 1  # bottom right
        self.assertEqual(game.value_matrix, expected_matrix)

    def test_change_value_returns_false_if_boat_overlap_horizontal(self):
        """""
            Tries to place a horizontal boat onto another boat, should not allow to overlap
        """""
        setup = GameSetup()
        setup.value_matrix[1][1] = 1
        setup.current_pos = [1, 1]
        setup.direction = "horizontal"
        self.assertFalse(setup.change_value(3, "horizontal", "player1"))

    def test_change_value_returns_false_if_boat_overlap_vertical(self):
        """""
            Tries to place a vertical boat onto another boat, should not allow to overlap
        """""
        setup = GameSetup()
        setup.value_matrix[1][1] = 1
        setup.current_pos = [1, 1]
        setup.direction = "vertical"
        self.assertFalse(setup.change_value(3, "vertical", "player1"))

    def test_change_value_updates_value_matrix_horizontal(self):
        """""
            Tries to place a horizontal boat, check if the values get updated correctly
        """""
        setup = GameSetup()
        setup.current_pos = [1, 1]
        setup.direction = "horizontal"
        self.assertTrue(setup.change_value(3, "horizontal", "player1"))
        expected_value_matrix = create_matrix()
        expected_value_matrix[1][1] = 2
        expected_value_matrix[1][2] = 2
        expected_value_matrix[1][3] = 2
        expected_value_matrix[1][4] = 1
        expected_value_matrix[2][1] = 1
        expected_value_matrix[2][2] = 1
        expected_value_matrix[2][3] = 1
        expected_value_matrix[2][4] = 1
        self.assertEqual(setup.value_matrix, expected_value_matrix)

    def test_change_value_updates_value_matrix_vertical(self):
        """""
            Tries to place a vertical boat, check if the values get updated correctly
        """""
        setup = GameSetup()
        setup.current_pos = [1, 1]
        setup.direction = "vertical"
        self.assertTrue(setup.change_value(3, "vertical", "player1"))
        expected_value_matrix = create_matrix()
        expected_value_matrix[1][1] = 2
        expected_value_matrix[1][2] = 1
        expected_value_matrix[2][1] = 2
        expected_value_matrix[2][2] = 1
        expected_value_matrix[3][1] = 2
        expected_value_matrix[3][2] = 1
        expected_value_matrix[4][1] = 1
        expected_value_matrix[4][2] = 1
        self.assertEqual(setup.value_matrix, expected_value_matrix)

    def test_reset_boat_setup(self):
        """""
            Checks if the GameSetup resets correctly using reset_boat_setup()
        """""
        game_setup = GameSetup()
        game_setup.move_matrix[3][3] = 1
        game_setup.value_matrix[3][3] = 2
        game_setup.ammount = [0, 0, 0, 0]
        game_setup.direction = "vertical"

        game_setup.reset_boat_setup("player1")
        matrix1 = create_matrix()
        for i in range(5):
            matrix1[1][1 + i] = 3

        matrix2 = create_matrix()
        self.assertEqual(game_setup.move_matrix, matrix1)
        self.assertEqual(game_setup.value_matrix, matrix2)
        self.assertEqual(game_setup.ammount, [1, 2, 3, 4])
        self.assertEqual(game_setup.direction, "horizontal")

    def test_change_direction(self):
        """""
            Asserts the correct change of the boat direction
        """""
        game = GameSetup()
        game.change_direction(3, "player1")
        self.assertEqual(game.direction, "vertical")
        game.change_direction(3, "player1")
        self.assertEqual(game.direction, "horizontal")

    def test_handle_key_event_before_placement_enter(self):
        """""
            Tests the change of values upon using the enter key
        """""
        game = GameSetup()
        game.ammount = [1, 0, 0, 0]
        game.value_matrix = create_matrix()
        game.move_matrix = create_matrix()
        event = MagicMock()
        event.name = "enter"
        result = game.handle_key_event_before_placement(event, 5, 0, "player1")
        matrix = create_matrix()
        for i in range(5):
            matrix[1][1 + i] = 2
        for i in range(6):
            matrix[2][1 + i] = 1
        matrix[1][6] = 1
        self.assertEqual(game.ammount, [0, 0, 0, 0])
        self.assertEqual(matrix, game.value_matrix)
        self.assertEqual(result, (True, False))

    def test_handle_key_event_before_placement_up(self):
        """""
            Tests the change of position upon using the up key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "up"
        game.current_pos = [2, 1]
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, (1, 1))

    def test_handle_key_event_before_placement_up_boarder(self):
        """""
            Tests the not changing of position upon using the up key while at the boarder
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "up"
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, [1, 1])

    def test_handle_key_event_before_placement_down(self):
        """""
            Tests the change of position upon using the down key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "down"
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, (2, 1))

    def test_handle_key_event_before_placement_down_boarder(self):
        """""
            Tests the not changing of position upon using the down key while at the boarder
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "down"
        game.current_pos = [9, 9]
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, [9, 9])

    def test_handle_key_event_before_placement_left(self):
        """""
            Tests the change of position upon using the left key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "left"
        game.current_pos = [1, 2]
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, (1, 1))

    def test_handle_key_event_before_placement_left_boarder(self):
        """""
            Tests the not changing of position upon using the left key while at the boarder
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "left"
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, [1, 1])

    def test_handle_key_event_before_placement_right(self):
        """""
            Tests the change of position upon using the right key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "right"
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, (1, 2))

    def test_handle_key_event_before_placement_right_boarder(self):
        """""
            Tests the not changing of position upon using the right key while at the boarder
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "right"
        game.current_pos = [1, 9]
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.current_pos, [1, 9])

    def test_handle_key_event_before_placement_shift(self):
        """""
            Tests the rotation of a boat upon using the shift key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "shift"
        # game.current_pos = [9, 9]
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.direction, "vertical")

    def test_handle_key_event_before_placement_r(self):
        """""
            Tests the random boat setup upon using the r key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "r"
        game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(game.ammount, [0, 0, 0, 0])

    def test_handle_key_event_before_placement_esc(self):
        """""
            Tests the reset of the board upon using the esc key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "esc"
        result = game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(result, (False, True))

    def test_handle_key_event_before_placement_s(self):
        """""
            Tests the s key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "s"
        with patch("builtins.print") as mock_print:
            game.handle_key_event_before_placement(event, 3, 0, "player1")
            mock_print.assert_called_with("you still have boats to be placed!")

    def test_handle_key_event_before_placement_b(self):
        """""
            Tests the b key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "b"
        result = game.handle_key_event_before_placement(event, 3, 0, "player1")
        self.assertEqual(result, (False, False))

    def test_handle_key_event_after_placement_esc(self):
        """""
            Tests the esc key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "esc"
        result = game.handle_key_event_after_placement(event, "player1")
        self.assertEqual(result, (False, True))

    def test_handle_key_event_after_placement_s(self):
        """""
            Tests the s key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "s"
        result = game.handle_key_event_after_placement(event, "player1")
        self.assertEqual(result, (True, True))

    def test_handle_key_event_after_placement_b(self):
        """""
            Tests the b key
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "b"
        result = game.handle_key_event_after_placement(event, "player1")
        self.assertEqual(result, (False, False))

    def test_handle_key_event_after_placement_other(self):
        """""
            Tests other keys
        """""
        game = GameSetup()
        event = MagicMock()
        event.name = "other"
        result = game.handle_key_event_after_placement(event, "player1")
        self.assertEqual(result, (True, False))


class GameTestCase(unittest.TestCase):
    """""
        Testing various functions of Game class
    """""

    @patch('game.clear_terminal')
    def test_update_board(self, mock_clear):
        """""
            Tests the update_board function with is_bot = false
        """""
        game = Game()
        move_matrix = create_matrix()
        move_matrix[1][2] = 1
        move_matrix[2][1] = 1
        matrix_one = create_matrix()
        matrix_two = create_matrix()
        matrix_two[1][1] = 1
        matrix_two[1][2] = 1
        matrix_two[2][1] = 1
        with patch.object(game.board, 'color_matrix_positions_board_one', return_value=None) as mock_color_one, \
                patch.object(game.board, 'color_matrix_positions_board_two', return_value=None) as mock_color_two, \
                patch.object(game.board, 'print_double_board', return_value=None) as mock_print:
            game.update_board(move_matrix, matrix_one, matrix_two, {"name_one": "player1", "name_two": "player2"})
            mock_clear.assert_called()
            mock_color_one.assert_called_with(move_matrix, matrix_one)
            mock_color_two.assert_called_with(matrix_two)
            mock_print.assert_called()

    @patch('game.clear_terminal')
    def test_update_board_bot(self, mock_clear):
        """""
            Tests the update_board function with is_bot = true
        """""
        game = Game()
        move_matrix = create_matrix()
        move_matrix[1][2] = 1
        move_matrix[2][1] = 1
        matrix_one = create_matrix()
        matrix_two = create_matrix()
        matrix_two[1][1] = 1
        matrix_two[1][2] = 1
        matrix_two[2][1] = 1
        game.is_bot = True
        with patch.object(game.board, 'color_matrix_positions_board_one', return_value=None) as mock_color_one, \
                patch.object(game.board, 'color_matrix_positions_board_two', return_value=None) as mock_color_two, \
                patch.object(game.board, 'print_double_board', return_value=None) as mock_print:
            game.update_board(move_matrix, matrix_one, matrix_two, {"name_one": "player1", "name_two": "player2"})
            mock_clear.assert_called()
            mock_color_one.assert_called_with(move_matrix, matrix_two)
            mock_color_two.assert_called_with(matrix_one)
            mock_print.assert_called()

    def test_move_up(self):
        """""
            Tests the move function with direction = up
        """""
        game = Game()
        matrix_one = create_matrix()
        matrix_two = create_matrix()
        game.current_pos = (2, 5)
        game.move_matrix = create_matrix()
        game.move(matrix_one, matrix_two, "up", {"name_one": "player1", "name_two": "player2"})
        self.assertEqual(game.current_pos, (1, 5))
        self.assertEqual(game.move_matrix[1][5], 3)

    def test_move_down(self):
        """""
            Tests the move function with direction = down
        """""
        game = Game()
        matrix_one = create_matrix()
        matrix_two = create_matrix()
        game.current_pos = (9, 5)
        game.move_matrix = create_matrix()
        game.move(matrix_one, matrix_two, "down", {"name_one": "player1", "name_two": "player2"})
        self.assertEqual(game.current_pos, (10, 5))
        self.assertEqual(game.move_matrix[10][5], 3)

    def test_move_left(self):
        """""
            Tests the move function with direction = left
        """""
        game = Game()
        matrix_one = create_matrix()
        matrix_two = create_matrix()
        game.current_pos = (5, 2)
        game.move_matrix = create_matrix()
        game.move(matrix_one, matrix_two, "left", {"name_one": "player1", "name_two": "player2"})
        self.assertEqual(game.current_pos, (5, 1))
        self.assertEqual(game.move_matrix[5][1], 3)

    def test_move_right(self):
        """""
            Tests the move function with direction = right
        """""
        game = Game()
        matrix_one = create_matrix()
        matrix_two = create_matrix()
        game.current_pos = (5, 9)
        game.move_matrix = create_matrix()
        game.move(matrix_one, matrix_two, "right", {"name_one": "player1", "name_two": "player2"})
        self.assertEqual(game.current_pos, (5, 10))
        self.assertEqual(game.move_matrix[5][10], 3)

    def test_mark_destroyed_boat_vertical_boat(self):
        """""
            Tests the mark_destroyed_boat function for marking a destroyed vertical boat
        """""
        game = Game()
        matrix = create_matrix()
        matrix[2][4] = 6  # mark a vertical boat of size 3
        matrix[3][4] = 7
        matrix[4][4] = 6
        game.mark_destroyed_boat(matrix, 3, 4)
        expected_matrix = create_matrix()
        expected_matrix[2][4] = 7  # mark all positions of the boat as destroyed
        expected_matrix[3][4] = 7
        expected_matrix[4][4] = 7
        self.assertEqual(matrix, expected_matrix)

    def test_mark_destroyed_boat_horizontal_boat(self):
        """""
            Tests the mark_destroyed_boat function for marking a destroyed horizontal boat
        """""
        game = Game()
        matrix = create_matrix()
        matrix[5][6] = 6  # mark a horizontal boat of size 4
        matrix[5][7] = 7
        matrix[5][8] = 6
        matrix[5][9] = 6
        game.mark_destroyed_boat(matrix, 5, 7)
        expected_matrix = create_matrix()
        expected_matrix[5][6] = 7  # mark all positions of the boat as destroyed
        expected_matrix[5][7] = 7
        expected_matrix[5][8] = 7
        expected_matrix[5][9] = 7
        self.assertEqual(matrix, expected_matrix)

    def test_game_not_ended(self):
        """""
            Tests if the game hasn't ended yet
        """""
        # Create a value matrix with at least one 2 value
        value_matrix = create_matrix()
        value_matrix[3][4] = 2
        game = Game()
        self.assertFalse(game.check_for_game_ending(value_matrix))

    def test_game_ended(self):
        """""
            Tests if the game ended yet
        """""
        # Create a value matrix with no 2 values
        value_matrix = create_matrix()
        game = Game()
        self.assertTrue(game.check_for_game_ending(value_matrix))
        self.assertTrue(game.win)

    def test_mark_destroyed_boat_surrounding(self):
        """""
            Tests the marking of the surrounding of a destroyed boat
        """""
        value_matrix = create_matrix()
        value_matrix[5][5] = 7
        game = Game()
        game.mark_destroyed_boat_surrounding(value_matrix)
        expected_matrix = create_matrix()
        expected_matrix[5][5] = 7
        expected_matrix[4][5] = 5
        expected_matrix[4][4] = 5
        expected_matrix[4][6] = 5
        expected_matrix[5][4] = 5
        expected_matrix[5][6] = 5
        expected_matrix[6][6] = 5
        expected_matrix[6][5] = 5
        expected_matrix[6][4] = 5
        self.assertEqual(value_matrix, expected_matrix)

    def test_attack_miss(self):
        """""
            Tests the miss of an attack
        """""
        game = Game()
        value_matrix = create_matrix()
        matrix_two = create_matrix()
        game.current_pos = [0, 0]
        self.assertFalse(game.attack(value_matrix, matrix_two, {"name_one": "player1", "name_two": "player2"}))
        self.assertTrue(game.miss)

    def test_attack_hit(self):
        """""
            Tests the hit of an attack
        """""
        game = Game()
        value_matrix = create_matrix()
        matrix_two = create_matrix()
        value_matrix[0][0] = 2
        game.current_pos = [0, 0]
        self.assertTrue(game.attack(value_matrix, matrix_two, {"name_one": "player1", "name_two": "player2"}))
        self.assertFalse(game.miss)

    def test_attack_already_attacked(self):
        """""
            Tests if one has already attacked
        """""
        game = Game()
        value_matrix = create_matrix()
        matrix_two = create_matrix()
        value_matrix[0][0] = 5
        game.current_pos = [0, 0]
        self.assertFalse(game.attack(value_matrix, matrix_two, {"name_one": "player1", "name_two": "player2"}))
        self.assertFalse(game.miss)


if __name__ == '__main__':
    unittest.main()
