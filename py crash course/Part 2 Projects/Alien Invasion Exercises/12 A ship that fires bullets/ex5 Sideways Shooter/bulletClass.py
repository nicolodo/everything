
import pygame

class Bullet:
    """This models a bullet shot from the rocket"""

    def __init__(self, ship, screen):
        self.screen = screen
        self.screenRect = screen.get_rect()
        # give it a shape and location

        self.width = 9
        self.height = 3

        # shape
        self.rect = pygame.Rect(0,0,self.width,self.height)

        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right

    def blit_me(self, screen):
        continue

