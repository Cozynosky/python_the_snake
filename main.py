"""
The concept of this project is creating a classic snake game in powershell.
Assumptions:
- snake react to players keypress
- snake can eat apples and save it as a score
- snake grow when eat apple
"""
import time, os, pickle
from pynput import keyboard
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
            self.high_scores = [(0, 0, 0, 0) for x in range(10)]

    def run(self):
        """Runs infinite game loop."""
        listener = keyboard.Listener(on_press=self.keyboard_event_reader)
        listener.start()
        while self.game_on:
            self.update_screen()

    def keyboard_event_reader(self, key):
        try:
            if key.char == "s":
                self.board.snake.go_down()
            elif key.char == "w":
                self.board.snake.go_up()
            elif key.char == "a":
                self.board.snake.go_left()
            elif key.char == "d":
                self.board.snake.go_right()
        except AttributeError:
            if key == keyboard.Key.esc:
                self.game_on = False

    def update_screen(self):
        self.board.update_board()
        self.board.show_board()
        self.game_on = not self.board.snake.self_eat_detect()
        if not self.game_on:
            self.snake_eaten()
        time.sleep(self.settings.game_speed)
        os.system(self.settings.clear_console)

    def snake_eaten(self):
        input("GAME OVER! YOU'VE ATE YOURSELF. \nPRESS 'ENTER' TO SEE HIGHSCORES")
        os.system(self.settings.clear_console)
        self.show_high_scores()
        record, index = self.check_scores()
        if record:
            choice = input(
                f"You have new RECORD!! {self.board.score}!! Would you like to save it? [y/n]"
            )
            if choice == "y":
                os.system(self.settings.clear_console)
                name = input("Write your name please: ")
                mins = self.board.playtime_ended // 60
                secs = self.board.playtime_ended - (mins * 60)
                self.save_scores(name, self.board.score, mins, secs, index)
                os.system(self.settings.clear_console)
                self.show_high_scores()
                input("PRESS 'ENTER' TO CONTINUE")

    def save_scores(self, name, score, mins, secs, index):
        self.high_scores.insert(index, (name, score, mins, secs))
        del self.high_scores[-1]
        pickle.dump(self.high_scores, open("highscores.pickle", "wb"))

    def load_scores(self):
        return pickle.load(open("highscores.pickle", "rb"))

    def check_scores(self):
        for i in range(len(self.high_scores)):
            if self.board.score > self.high_scores[i][1]:
                return True, i
        return False, 0

    def show_high_scores(self):
        print("  NAME  |   SCORE   |  TIME")
        for i in range(len(self.high_scores)):
            print(
                f"{self.high_scores[i][0]}      {self.high_scores[i][1]}        {self.high_scores[i][2]}:{self.high_scores[i][3]}"
            )


if __name__ == "__main__":
    snk_game = Game()
    snk_game.run()
