
import pygame

# make a rocket class

class Rocket:
    """This is a moving rocket rect thing"""

    def __init__(self, screen, settings):
        
        # keeping the screen and settings available
        self.settings = settings
        self.screen = screen
        self.screenRect = self.screen.get_rect()

        # setup the rockets attributes
        path = 'images/rocket.bmp'
        self.img = pygame.image.load(
            'images/rocket.bmp'
        )
        self.rect = self.img.get_rect()
        
        # position the rocket
        self.rect.bottom = self.screenRect.bottom
        self.rect.centerx = self.screenRect.centerx

    def blit_me(self):
        self.screen.blit(self.img, self.rect)

