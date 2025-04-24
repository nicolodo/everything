
import pygame

class star:
    """This is the star we draw to the screen"""

    def __init__(self, screen):
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

    def blit_me():
        self.screen.blit(self.image, self.screenRect)

