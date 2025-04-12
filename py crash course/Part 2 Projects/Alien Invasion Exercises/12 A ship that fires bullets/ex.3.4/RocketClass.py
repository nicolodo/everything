
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

        # setup movement flags
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

    def updatePosition(self):
        if self.moveLeft and self.rect.left > 0:
            self.rect.right -= 1
        if self.moveRight and self.rect.right < self.screenRect.right:
            self.rect.right += 1
        if self.moveUp and self.rect.top < 0:
            self.rect.top -= 1
        if self.moveDown and self.rect.bottom < self.screenRect.bottom:
            self.rect.right += 1
        

    def blit_me(self):
        self.screen.blit(self.img, self.rect)

