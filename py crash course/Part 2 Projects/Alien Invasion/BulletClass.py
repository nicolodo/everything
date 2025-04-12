
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ships current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet obj at (0,0) then set correct position
        self.rect = pygame.rect(0,0,ai_settings.bullet.width,
                                ai_settings.bullet.height)
        self.rect.centerx = ship.centerx
        self.rect.top = ship.rect.top

        # store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet.color
        self.speedFactor = ai_settings.bullet.speedFactor

    



