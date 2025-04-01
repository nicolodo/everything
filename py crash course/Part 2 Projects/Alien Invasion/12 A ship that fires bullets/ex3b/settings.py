
import pygame

class Settings:
    """Put all the major settings here"""

    def __init__(self):
        self.SCREEN_SIZE = (400,300)
        self.TITLE = "Rocket game"
        self.BG_COLOR = (0,0,0)

        # pygame.display.set_mode(self.SCREEN_SIZE)
        # pygame.display.fill(self.BG_COLOR)
        # pygame.display.set_caption(self.TITLE)