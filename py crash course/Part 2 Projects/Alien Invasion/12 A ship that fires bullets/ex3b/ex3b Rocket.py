
import pygame, sys
from settings import Settings


def run():
    pygame.init()
    ACTIVE = True
    ai_settings = Settings()

    SCREEN = pygame.display.set_mode(ai_settings.SCREEN_SIZE)
    pygame.display.set_caption(ai_settings.TITLE)

    while ACTIVE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
    pygame.display.flip()

run()
