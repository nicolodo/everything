
import pygame, sys
from SettingsClass import Settings

def run():
    # Setup window
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen.size)
    pygame.display.set_caption(settings.screen.caption)
    

    while True:
        
        screen.fill(settings.bgColor)

        pygame.display.flip()


run()
