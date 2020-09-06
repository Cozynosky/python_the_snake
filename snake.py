"""
Snake class with his body length, positions and some methods
"""

class Snake:

    def __init__(self,settings):
        self.settings = settings
        self.x_step = 0
        self.y_step = -1
        self.body = [(settings.board_height//2,settings.board_width//2)]
    
    def go_up(self):
        if len(self.body)>1 and self.y_step == 1:
            pass
        else: 
            self.y_step = -1
            self.x_step = 0

    def go_down(self):
        if len(self.body)>1 and self.y_step == -1:
            pass
        else: 
            self.y_step = 1
            self.x_step = 0

    def go_left(self):
        if len(self.body)>1 and self.x_step == 2:
            pass
        else: 
            self.y_step = 0
            self.x_step = -2

    def go_right(self):
        if len(self.body)>1 and self.x_step == -2:
            pass
        else: 
            self.y_step = 0
            self.x_step = 2
    
    def move(self):
        if len(self.body) > 1:
            pass
        self.body[0] = (self.body[0][0]+self.y_step, self.body[0][1]+self.x_step)

    def wall_detect(self):
        for i in range(len(self.body)):
            if self.body[i][0] <= 0:
                self.body[i] = (self.settings.board_height - 2,self.body[i][1])
            if self.body[i][0] >= self.settings.board_height - 1:
                self.body[i] = (1,self.body[i][1])
            if self.body[i][1] <= 0:
                self.body[i] = (self.body[i][0],self.settings.board_width-3)
            if self.body[i][1] >= self.settings.board_width-1:
                self.body[i] = (self.body[i][0],2)

    def self_detect(self):
        pass

    def apple_collision(self,apple):
        if apple in self.body:
            return True
    