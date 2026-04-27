from enum import Enum


class State(Enum):
    empty_cell = 0
    blocked = 1
    occupied_x = 2
    occupied_o = 3
    try_this_move = 4


class Cell:
    def __init__(self, state=State.empty_cell):
        self.state = state

    def move_X(self):
        """set the state of the cell to 'X' """
        self.state = State.occupied_x

    def move_O(self):
        """set the state of the cell to 'O' """
        self.state = State.occupied_o

    def empty(self):
        """set the state of the cell to empty"""
        self.state = State.empty_cell

    def block(self):
        """block the cell (in game it is seen as '.')"""
        self.state = State.blocked

    def __str__(self):
        """representation to better see the cells"""
        return {State.empty_cell: " ", State.blocked: ".", State.occupied_x: "X", State.occupied_o: "O"}.get(self.state, "?")
