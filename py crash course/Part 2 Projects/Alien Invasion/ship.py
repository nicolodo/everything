
import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen 

        # Load the ship img and get its rect. 
        self.img = pygame.image.load('images/ship.bmp')
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.img, self.rect)

