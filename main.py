"""
The concept of this project is creating a classic snake game in powershell.
Assumptions:
- snake react to players keypress
- snake can eat apples and save it as a score
- snake grow when eat apple
"""
import time,os,keyboard,pickle
from board import Board
from settings import Settings

class Game:

    def __init__(self):
        self.game_on = True
        self.settings = Settings()
        self.board = Board(self.settings)
        self.high_scores = []
    
    def read_keyboard(self,key):
        if key.name == "esc":
            self.game_on = False
        if key.name == "s":
            self.board.snake.go_down()
        if key.name == "w":
            self.board.snake.go_up()
        if key.name == "a":
            self.board.snake.go_left()
        if key.name == "d":
            self.board.snake.go_right()
        keyboard.unhook_all()
            
    def update_screen(self):
        self.board.update_board()
        self.board.show_board()
        keyboard.on_press(self.read_keyboard)
        self.game_on = not self.board.snake.self_eat_detect()
        if not self.game_on:
            self.show_scores = input("GAME OVER! YOU'VE ATE YOURSELF. \nPRESS 'ENTER' TO SEE HIGHSCORES")
        time.sleep(self.settings.game_speed)
        os.system('clear')
    
    def save_game(self,name,score,mins,secs):
        self.high_scores.append((name,score,mins,secs))
        pickle.dump(self.high_scores,open("highscores.pickle","wb"))
    
    def load_game(self):
        self.high_scores = pickle.load(open("highscores.pickle","rb"))
    
    def show_high_scores(self):
        pass

if __name__ == "__main__":
    snk_game = Game()
    while(snk_game.game_on):
        snk_game.update_screen()
    
