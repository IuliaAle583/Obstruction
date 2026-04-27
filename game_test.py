import unittest
from src.cell import State
from src.board import Board
from src.game import Game

class TestGame(unittest.TestCase):

    def test_player_move(self):
        board = Board(6, 6)
        game = Game(board)
        game.player_move(2, 2)
        self.assertEqual(board[2][2].state, State.occupied_x)
        self.assertFalse(all(
            cell.state == State.blocked or cell.state == State.empty_cell
            for row in board.board for cell in row
        ))
        self.assertFalse(game.game_over)

    def test_computer_move(self):
        board = Board(6, 6)
        game = Game(board)
        game.player_move(2, 2)
        game.computer_move()
        self.assertTrue(any(
            cell.state == State.occupied_o for row in board.board for cell in row
        ))
        self.assertFalse(game.game_over)

    def test_game_over_check(self):
        board = Board(6, 6)
        game = Game(board)
        for row in range(board.rows):
            for col in range(board.cols):
                if (row + col) % 2 == 0:
                    board[row][col].move_X()
                else:
                    board[row][col].move_O()
        game.is_game_over()
        self.assertTrue(game.game_over, "The game should be over when the board is full")

    def test_player_wins(self):
        board = Board(6, 6)
        game = Game(board)
        game.player_move(0, 0)
        game.player_move(1, 1)
        game.player_move(2, 2)
        self.assertEqual(game.last_move, 1)

    def test_computer_wins(self):
        board = Board(6, 6)
        game = Game(board)
        game.player_move(0, 0)
        game.player_move(1, 1)
        game.computer_move()
        game.computer_move()
        self.assertEqual(game.last_move, 2)


if __name__ == "__main__":
    unittest.main()
