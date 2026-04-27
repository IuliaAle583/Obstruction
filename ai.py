from random import randint

from src.cell import State

class AI:
    @staticmethod
    def _get_empty_cells(board):
        return [(x, y) for x in range(board.rows) for y in range(board.cols)
                if board[x][y].state == State.empty_cell]

    def move(self, board):
        """
        makes the move
        :param board: the board
        :return: the move
        """
        winning_move = self.try_winning_move(board)
        if winning_move:
            return winning_move
        possible_moves = self.try_block_move(board)
        if possible_moves:
            return self.random_move(board, possible_moves)
        return self.random_move(board, self._get_empty_cells(board))

    @staticmethod
    def random_move( board, possible_moves):
        """
        makes a random move on the board (on empty cells)
        :param board: the board
        :param possible_moves: the empty cells on which moves are possible
        :return: the move (its coordinates)
        """
        random_cell = possible_moves[randint(0, len(possible_moves) - 1)]
        x, y = random_cell
        return (x, y)

    def try_winning_move(self, board, default_moves=[]):
        """
        tries to make a winning move by using temporarily occupied cells
        :param board: the board
        :param default_moves: already done moves
        :return: cell of the winning move (tuple), None if it doesn't exist
        """
        for x, y in self._get_empty_cells(board):
            if board[x][y].state == State.empty_cell:
                self.try_this_move(board, [(x, y)] + default_moves)
                if not len(self._get_empty_cells(board)):
                    self.delete_these_moves(board)
                    return (x, y)
                self.delete_these_moves(board)
        return None

    @staticmethod
    def try_this_move( board, points):
        """
        tries to do moves to win
        :param board: the board
        :param points: moves coordinates
        """
        directie = [-1, 0, 1]
        for x, y in points:
            for row_dir in directie:
                for column_dir in directie:
                    if 0 <= x + row_dir < board.rows and 0 <= y + column_dir < board.cols:
                        if board[x + row_dir][y + column_dir].state == State.empty_cell:
                            board[x + row_dir][y + column_dir].state = State.try_this_move

    @staticmethod
    def delete_these_moves( board):
        """
        makes the cell empty again
        :param board: the board
        """
        for row in range(board.rows):
            for column in range(board.cols):
                if board[row][column].state == State.try_this_move:
                    board[row][column].state = State.empty_cell

    def try_block_move(self, board):
        """
        tries to block the players move if it will gain a victory
        :param board: the board
        :return: the list of players future moves, None if it doesn't exist
        """
        try_move = []
        for x, y in self._get_empty_cells(board):
            if not self.try_winning_move(board, [(x, y)]):
                try_move.append((x, y))
            self.delete_these_moves(board)
        return try_move if try_move else None

