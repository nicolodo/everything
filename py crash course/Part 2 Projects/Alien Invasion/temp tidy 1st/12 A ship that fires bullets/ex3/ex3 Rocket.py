

# make a game which has a character I can move up/down/left/right
import pygame, sys
from settings import Settings
from rocket import Rocket

def run():
    pygame.init()
    SCREEN = pygame.display.set_mode(settings.SREEN_SIZE)
    settings = Settings()

    while ACTIVE:
        # get events
        game_functions.get_events()

        # update the rocket
        rocket.update(SCREEN)

        # draw to the screen
        game_functions.update_screen(SCREEN,rocket,settings)

















