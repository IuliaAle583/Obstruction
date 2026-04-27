from src.board import Board
from src.game import Game

class ErrorUI(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

class UI:
    def __init__(self):
        self.game = None
        self.player_symbol = 'X'
        self.computer_symbol = 'O'

    @staticmethod
    def print_welcome():
        print()
        print("WELCOME TO OBSTRUCTION!")

    def display_game_board(self):
        print(self.game.board.pretty())

    @staticmethod
    def get_player_move():
        try:
            row = int(input("line: ")) - 1
            col = int(input("column: ")) - 1
            return row, col
        except ValueError:
            print("input is invalid")
            return None, None

    def set_up(self):
        self.print_welcome()
        print("player is X and computer is O")
        #so the player has more chances to win :)
        board = Board(6, 6)
        self.game = Game(board)

    def player_turn(self):
        move_done = False
        while not move_done:
            try:
                row, col = self.get_player_move()
                if row is not None and col is not None:
                    if not self.game.board.is_valid_move(row, col):
                        print("invalid move, the cell is not empty")
                        continue
                    move_done = True
                    if self.game.player_move(row, col):
                        print("player moved")
                        return self.game.game_over
            except ErrorUI as inputError:
                print(inputError)
                move_done = False

    def computer_turn(self):
        if self.game.computer_move():
            print("computer moved")
        return self.game.game_over

    def play_game(self):
        self.set_up()
        game_over = False
        turns = {
            self.player_symbol: self.player_turn,
            self.computer_symbol: self.computer_turn
        }
        current_symbol = self.player_symbol
        while not game_over:
            self.display_game_board()
            game_over = turns[current_symbol]()
            if game_over:
                self.display_game_board()
                print("GAME OVER!")
                if self.game.last_move==1:
                    print("PLAYER WINS!")
                elif self.game.last_move==2:
                    print("COMPUTER WINS!")
                break

            if current_symbol == self.player_symbol:
                current_symbol = self.computer_symbol
            else:
                current_symbol = self.player_symbol

    def start(self):
        self.play_game()

