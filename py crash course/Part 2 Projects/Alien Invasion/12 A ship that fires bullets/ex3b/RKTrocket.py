
import pygame

class RocketClass:
    """Model of a rocket"""
    def __init__(self, screen):
        # import the image and get the rect
            
        path = "image/guy.bmp"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.screen = screen

    def blitme(self):
        

