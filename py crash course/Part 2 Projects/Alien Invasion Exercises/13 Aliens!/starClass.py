
import pygame
from pygame.sprite import Sprite

class star(Sprite):
    """This is the star we draw to the screen"""

    def __init__(self, screen):

        super(star, self).__init__()
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

    def blit_me(self):
        self.screen.blit(self.image, self.screenRect)

