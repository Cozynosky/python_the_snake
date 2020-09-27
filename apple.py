"""
file with apple class
"""

import random


class Apple:
    def __init__(self, settings, snake):
        self.settings = settings
        self.apple_coords = ()
        self.spawn_apple(snake)

    def spawn_apple(self, snake):
        new_apple = (
            random.randint(1, self.settings.board_height - 2),
            random.randrange(2, self.settings.board_width - 2, 2),
        )
        self.apple_coords = new_apple
        if self.apple_coords in snake.body:
            self.spawn_apple(snake)
