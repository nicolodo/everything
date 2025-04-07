
import pygame

class Character():
    """character for screen"""

    def __init__(self, screen):
        """setup character values"""
        self.screen = screen

        # load the guy image and get its rect value
        path = 'images/Guy.bmp'
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # position guy rect at bottom, middle of screen
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)
































































