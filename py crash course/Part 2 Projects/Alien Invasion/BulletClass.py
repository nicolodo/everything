
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ships current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet obj at (0,0) then set correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet.width,ai_settings.bullet.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet.color
        self.speedFactor = ai_settings.bullet.speedFactor

    def update_position(self):
        """Move the bullet up the screen"""
        # change y float value
        self.y -= self.speedFactor
        # set float y to rect.y
        self.rect.y = self.y    

    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        # draw.rect draws to the part of the screen defined
        # by the rect provided

