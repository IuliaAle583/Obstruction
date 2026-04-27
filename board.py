from src.cell import Cell, State
from texttable import Texttable


class Board:
    def __init__(self, rows=6, columns=6):
        self.rows = rows
        self.cols = columns
        self.board = self.create_board()

    def create_board(self):
        """
        function that creates the board
        :return: the modified board
        """
        return [[Cell(State.empty_cell) for _ in range(self.cols)] for _ in range(self.rows)]

    def __getitem__(self, index):
        """used to access the board by using [row, column] syntax"""
        return self.board[index]

    def block_nearby_cells(self, row, col):
        """block all the cells next to a new move by putting a dot in them
            no new move can be done there
        """
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.rows and 0 <= j < self.cols and self.board[i][j].state == State.empty_cell:
                    self.board[i][j].block()

    def is_full(self):
        """
        verify if the board is full
        :return: True if the board is full, False otherwise
        """
        for row in self.board:
            for cell in row:
                if cell.state == State.empty_cell:
                    return False
        return True

    def is_valid_move(self, row, col):
        """
        verify if the move is valid
        :param row:  the row of the board on which the move is made
        :param col: the column of the board on which the move is made
        :return: True if the move is valid, False otherwise
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return False
        return self.board[row][col].state == State.empty_cell

    def get_free_cells(self):
        """
        gets all the free cells in the table
        :return: the free cells
        """
        return list(filter(lambda r: self.board[r[0]][r[1]].state == State.empty_cell, [(r, c) for r in range(self.rows) for c in range(self.cols)]))


    def pretty(self):
        """make the board pretty"""
        table = Texttable()
        table.add_row([""] + [str(i + 1) for i in range(self.cols)])
        for i in range(self.rows):
            table.add_row([str(i + 1)] + [str(self.board[i][j]) for j in range(self.cols)])
        return table.draw()


