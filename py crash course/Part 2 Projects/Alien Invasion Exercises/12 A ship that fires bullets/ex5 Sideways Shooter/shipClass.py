
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

        self.moveUp = False
        self.moveDown = False

    def update(self):
        if self.moveUp and self.rect.top > 0:
            self.rect.top -= 1
        if self.moveDown and self.rect.bottom < self.screenRect.bottom:
            self.rect.bottom += 1

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
