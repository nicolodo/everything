
# import libraries
import pygame, sys

from settings import Settings
from ship import Ship

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

    ACTIVE = True

    # setup the event loop
    while ACTIVE:
        # watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # close if x clicked
                sys.exit()

        # Redraw screen
        SCREEN.fill(ai_settings.COLOR.WHITE)
        ship.blitme()

        # mk the most recently drawn screen visible
        pygame.display.flip()

run()


