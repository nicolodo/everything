
import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen 
        self.ai_settings = ai_settings

        # Load the ship img and get its rect. 
        self.img = pygame.image.load('image/ship.bmp')
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's center value, not the rect.
        # & limit ship range to screen width
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.img, self.rect)

