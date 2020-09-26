"""
file created to store settings
"""
import platform


class Settings:
    def __init__(self):
        self.board_height = 20
        self.board_width = 45
        self.game_speed = 0.25
        self.clear_console = self.system_check()

    def system_check(self):
        system = platform.system()
        if system == "Linux":
            return "clear"
        if system == "Windows":
            return "cls"
