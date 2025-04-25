
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """This is the star we draw to the screen"""

    def __init__(self, screen):
        
        # inherit sprite class
        super(Star, self).__init__() 

        self.screen = screen
        self.screenRect = screen.get_rect()

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.height = self.rect.height
        self.width = self.rect.width

    def blit_me(self):
        self.screen.blit(self.image, self.screenRect)

