"""
The concept of this project is creating a classic snake game in powershell.
Assumptions:
- snake react to players keypress
- snake can eat apples and save it as a score
- snake grow when eat apple
"""
import time
from board import Board

class Game:

    def __init__(self):
        self.game_on = True
        self.board = Board()

    def run_game(self,game_on):
        pass


if __name__ == "__main__":

    snk_game = Game()
    snk_game.board.show_board()
