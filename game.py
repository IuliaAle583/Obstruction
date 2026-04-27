from src.ai import AI
from src.cell import State

class Game:
    def __init__(self, board):
        self.board = board
        self.player_symbol = 'X'
        self.computer_symbol = 'O'
        self.game_over = False
        self.winner = 0
        self.last_move = 0       #used to determine the winner; 1-Player, 2-Computer
        self.__strategy = AI()

    def player_move(self, row, col):
        """
        makes the players move if it is valid
        :param row: the row on which the player wants to move
        :param col: the column on which the player wants to move
        :return: True if the game is over, False otherwise
        """
        if self.board.is_valid_move(row, col):
            self.board[row][col].move_X()
            self.board.block_nearby_cells(row, col)
            self.last_move = 1
            self.__check_game_over()

            return self.game_over

    def computer_move(self):
        """
        does the computers move if it is valid
        :return: true if the game is over, False otherwise
        """
        """
        valid_moves = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.is_valid_move(row, col):
                    valid_moves.append((row, col))

        if valid_moves:
            row, col = random.choice(valid_moves) 
            self.board[row][col].move_O()
            self.board.block_nearby_cells(row, col)
            self.last_move = 2
            self.__check_game_over()"""
        x,y = self.__strategy.move(self.board)
        self.board[x][y].move_O()
        self.board.block_nearby_cells(x, y)
        self.last_move = 2
        self.__check_game_over()
        return self.game_over

    def __check_game_over(self):
        """
        verifies if the game is over = if there are no empty cells
        :return: True if the game is over, False otherwise
        """
        if not any(
                cell.state == State.empty_cell
                for row in range(self.board.rows)
                for cell in self.board[row]
        ):
            self.game_over = True
            self.winner = self.last_move
            return True
        return False

    def is_game_over(self):
        """
        method to access the result of the __check_game_over() method
        :return: the same result as before
        """
        return self.__check_game_over()
