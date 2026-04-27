import unittest
from src.cell import State
from src.board import Board


class TestBoard(unittest.TestCase):

    def test_initialization(self):
        board = Board(6, 6)
        self.assertEqual(board.rows, 6)
        self.assertEqual(board.cols, 6)
        self.assertTrue(all(cell.state == State.empty_cell for row in board.board for cell in row))

    def test_get_item(self):
        board = Board(6, 6)
        cell = board[2][3]
        self.assertEqual(cell.state, State.empty_cell)


    def test_block_nearby_cells(self):
        board = Board(6, 6)
        board[2][2].move_X()
        board.block_nearby_cells(2, 2)
        blocked_cells = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]
        for r, c in blocked_cells:
            self.assertEqual(board[r][c].state, State.blocked)

    def test_is_full(self):
        board = Board(6, 6)
        for row in board.board:
            for cell in row:
                cell.move_X()
        self.assertTrue(board.is_full())
        board[0][0].empty()
        self.assertFalse(board.is_full())

    def test_is_valid_move(self):
        board = Board(6, 6)
        self.assertTrue(board.is_valid_move(2, 2))
        board[2][2].move_X()
        self.assertFalse(board.is_valid_move(2, 2))
        self.assertFalse(board.is_valid_move(6, 6))


if __name__ == "__main__":
    unittest.main()
