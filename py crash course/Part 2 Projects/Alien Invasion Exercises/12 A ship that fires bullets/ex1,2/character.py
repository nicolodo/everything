
class Character():
    """Make a pygame img class which contains sonic"""

    def __init__(self, picture, screen):
        """Takes in the img shown and the screen used"""
        path = 'images/sanic2.png'
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.screen = screen

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)




