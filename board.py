"""
board class should make board and store objects on it
"""
from snake import Snake
from apple import Apple

class Board:

    def __init__(self,settings):
        self.width = settings.board_width
        self.height = settings.board_height
        self.board = self.make_board()
        self.snake = Snake(settings)
        self.apple = Apple(settings,self.snake)
        self.score = 0
    
    def make_board(self):
        board = [[" " for y in range(self.width)] for x in range(self.height)]
        for i in range(self.width):
            board[0][i] = "-"
            board[-1][i] = "-"
        for i in range(self.height):
            board[i][-1] = "|"
            board[i][0] = "|"
        board[0][0] = "+"
        board[0][-1] = "+"
        board[-1][0] = "+"
        board[-1][-1] = "+"
        return board

    def show_board(self):
        print(f"""
+-------------------------------------------+
|SCORE:{self.score}                                    |""")
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[i][j], end="")
            print("")
        print("""             PRESS 'esc' TO QUIT             """)

    
    def update_board(self):
        self.board = self.make_board()
        self.snake.move()
        self.snake.wall_detect()
        self.board[self.apple.apple_coords[0]][self.apple.apple_coords[1]] = "@"
        for el in self.snake.body:
            self.board[el[0]][el[1]] = "o"
        self.board[self.snake.body[0][0]][self.snake.body[0][1]] = "O"
        if self.snake.body[0] == self.apple.apple_coords:
            self.score += 1
            self.snake.grow = True
            self.apple.spawn_apple(self.snake)
        
        
            