"""
board class should make board and store objects on it
"""

class Board:

    def __init__(self):
        self.width = 45
        self.height = 20
        self.board = self.make_board()
    
    def make_board(self):
        board = [[" " for y in range(self.width)] for x in range(self.height)]
        for i in range(self.width):
            board[0][i] = 0
            board[-1][i] = 0
        for i in range(self.height):
            board[i][-1] = 0
            board[i][0] = 0
        return board

    def show_board(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[i][j], end="")
            print("")
            