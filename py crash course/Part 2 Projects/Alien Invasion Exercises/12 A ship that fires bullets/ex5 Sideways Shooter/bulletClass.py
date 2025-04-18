
import pygame
from pygame.sprite import Sprite
from SettingsClass import Settings

class Bullet(Sprite):
    """This models a bullet shot from the rocket"""

    def __init__(self, ship, screen):
        """A class to manage bullets fired from the ship"""
        # this lets you use Sprite functions I think
        super(Bullet, self).__init__()

        self.screen = screen
        self.screenRect = screen.get_rect()
        # give it a shape and location, color

        self.width = 9
        self.height = 3
        self.color = ( 0, 0, 0)

        # shape
        self.rect = pygame.Rect(0, 0, self.width,self.height)
        # position at ship
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right

    def update(self):
        self.rect.x += 5

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # self.screen.blit(self.image, self.rect)
        pygame.display.flip()

