
# import libraries
import pygame, sys

from settings import Settings
from ship import Ship
import game_functions as gf

def run():

    pygame.init()
    ai_settings = Settings()
    SCREEN = pygame.display.set_mode(ai_settings.SCREEN_SIZE)
    COLOR = (200,200,200)
    # choose a name for the window
    NAME = "Alien Invasion"
    pygame.display.set_caption(NAME)

    # Make a ship
    ship = Ship(SCREEN)

    # setup the event loop
    while True:
        # watch for events
        gf.check_events(ship)
        ship.update() # update the ships position based on flag
        gf.update_screen(ai_settings, SCREEN, ship)

run()


