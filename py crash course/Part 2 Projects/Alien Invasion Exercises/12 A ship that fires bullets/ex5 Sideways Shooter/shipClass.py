
import pygame

class Ship:
    """This is the player's ship"""

    def __init__(self, screen):
        # store link to the screen passed
        self.screen = screen
        self.screenRect = screen.get_rect()

        # setup the ships img
        pathToImage = 'images/spaceship.bmp'
        self.image = pygame.image.load(pathToImage)
        self.rect = self.image.get_rect()
        # setup ship position on screen
        self.rect.left = 0
        self.rect.centery = self.screenRect.centery

        # setup ship movement flags
        self.moveUp = False
        self.moveDown = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
