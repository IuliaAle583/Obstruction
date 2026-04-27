import unittest

from src.cell import Cell, State


class TestCell(unittest.TestCase):

    def test_before_any_move(self):
        cell = Cell()
        self.assertEqual(cell.state, State.empty_cell)

    def test_move_X(self):
        cell = Cell()
        cell.move_X()
        self.assertEqual(cell.state, State.occupied_x)

    def test_move_O(self):
        cell = Cell()
        cell.move_O()
        self.assertEqual(cell.state, State.occupied_o)

    def test_empty(self):
        cell = Cell(State.occupied_x)
        cell.empty()
        self.assertEqual(cell.state, State.empty_cell)

    def test_block(self):
        cell = Cell()
        cell.block()
        self.assertEqual(cell.state, State.blocked)

    def test_str(self):
        cell_empty = Cell(State.empty_cell)
        self.assertEqual(str(cell_empty), " ")

        cell_blocked = Cell(State.blocked)
        self.assertEqual(str(cell_blocked), ".")
        cell_x = Cell(State.occupied_x)
        self.assertEqual(str(cell_x), "X")
        cell_o = Cell(State.occupied_o)
        self.assertEqual(str(cell_o), "O")

    def test_more_moves(self):
        cell = Cell()
        cell.move_X()
        self.assertEqual(str(cell), "X")
        cell.move_O()
        self.assertEqual(str(cell), "O")
        cell.empty()
        self.assertEqual(str(cell), " ")


if __name__ == "__main__":
    unittest.main()
