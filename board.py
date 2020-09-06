"""
board class should make board and store objects on it
"""
from snake import Snake

class Board:

    def __init__(self,settings):
        self.width = settings.board_width
        self.height = settings.board_height
        self.board = self.make_board()
        self.snake = Snake(settings)
    
    def make_board(self):
        board = [[" " for y in range(self.width)] for x in range(self.height)]
        for i in range(self.width):
            board[0][i] = "X"
            board[-1][i] = "X"
        for i in range(self.height):
            board[i][-1] = "X"
            board[i][0] = "X"
        return board

    def show_board(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[i][j], end="")
            print("")
    
    def update_board(self):
        self.board = self.make_board()
        self.snake.move()
        self.snake.wall_detect()
        for el in self.snake.body:
            self.board[el[0]][el[1]] = "O"
            