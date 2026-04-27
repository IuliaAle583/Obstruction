import unittest
from unittest.mock import MagicMock
from src.board import Board
from src.ai import AI


class TestAI(unittest.TestCase):

    def setUp(self):
        self.board = MagicMock(spec=Board)
        self.ai = AI()

    def test_random_move(self):
        self.board.get_free_cells.return_value = [(0, 0), (1, 1), (2, 2)]
        random_move = self.ai.random_move(self.board, [(0, 0), (1, 1), (2, 2)])
        self.assertIn(random_move, [(0, 0), (1, 1), (2, 2)])

    def test_winning_move(self):
        self.ai.try_winning_move = MagicMock(return_value=(0, 1))
        winning_move = self.ai.move(self.board)
        self.assertEqual(winning_move, (0, 1))

    def test_try_block_move(self):
        self.board.get_free_cells.return_value = [(1, 1), (2, 2)]
        self.ai.try_winning_move = MagicMock(return_value=None)
        self.ai.try_block_move = MagicMock(return_value=[(1, 1)])
        block_move = self.ai.try_block_move(self.board)
        self.assertIn((1, 1), block_move)

    def test_move_temporary(self):
        self.ai.try_this_move = MagicMock(return_value=None)
        self.ai.try_this_move(self.board, [(0, 0)])
        self.ai.try_this_move.assert_called_with(self.board, [(0, 0)])


if __name__ == '__main__':
    unittest.main()
