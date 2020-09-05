"""
The concept of this project is creating a classic snake game in powershell.
Assumptions:
- snake react to players keypress
- snake can eat apples and save it as a score
- snake grow when eat apple
"""
import time,os,keyboard
from board import Board

class Game:

    def __init__(self):
        self.game_on = True
        self.board = Board()
    
    def read_keyboard(self,key):
        if key.name == "esc":
            self.game_on = False
        keyboard.unhook_all()
            
    def update_screen(self):
        print("-------------PRESS 'esc' TO QUIT-------------")
        self.board.show_board()
        keyboard.on_press(self.read_keyboard)
        time.sleep(0.5)
        os.system('clear')


if __name__ == "__main__":
    snk_game = Game()
    while(snk_game.game_on):
        snk_game.update_screen()
    print("Thanks for playing")
