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
        try:
            self.high_scores = self.load_scores()
        except:
            self.high_scores = [(0,0,0,0) for x in range(10)]
    
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
            self.snake_eaten()
        time.sleep(self.settings.game_speed)
        os.system('clear')
    
    def snake_eaten(self):
        input("GAME OVER! YOU'VE ATE YOURSELF. \nPRESS 'ENTER' TO SEE HIGHSCORES")
        os.system('clear')
        self.show_high_scores()
        record,index = self.check_scores()
        if record:
            choice = input(f"You have new RECORD!! {self.board.score}!! Would you like to save it? [y/n]")
            if choice == "y":
                os.system('clear')
                name = input("Write your name please: ")
                mins = self.board.playtime_ended // 60
                secs = self.board.playtime_ended - (mins * 60)
                self.save_scores(name,self.board.score,mins,secs,index)
                os.system('clear')
                self.show_high_scores()
                input("PRESS 'ENTER' TO CONTINUE")

    def save_scores(self,name,score,mins,secs,index):
        self.high_scores.insert(index,(name,score,mins,secs))
        del self.high_scores[-1]
        pickle.dump(self.high_scores,open("highscores.pickle","wb"))
    
    def load_scores(self):
        return pickle.load(open("highscores.pickle","rb"))
    
    def check_scores(self):
        for i in range(len(self.high_scores)):
            if self.board.score > self.high_scores[i][1]:
                return True,i
        return False,0
    
    def show_high_scores(self):
        print("  NAME  |   SCORE   |  TIME")
        for i in range(len(self.high_scores)):
            print(f"{self.high_scores[i][0]}      {self.high_scores[i][1]}        {self.high_scores[i][2]}:{self.high_scores[i][3]}")

if __name__ == "__main__":
    snk_game = Game()
    while(snk_game.game_on):
        snk_game.update_screen()
    
