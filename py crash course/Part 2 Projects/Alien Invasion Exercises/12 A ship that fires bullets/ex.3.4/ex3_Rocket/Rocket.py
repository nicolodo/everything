# move rocket game via keyinput

import sys, pygame
from SettingsClass import Settings
from RocketClass import Rocket
import gameFunctions as gf

def run():
    # setup pygame, screen, name
    # setup event loop
    # setup draw to screen loop
    # setup rocket class
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Rockets of the empire")
    BLUE = (  0, 128, 128)
    ai_settings = Settings

    rocket = Rocket(screen, ai_settings)

    while True:
        
        # handle keyinput and flag handling
        gf.eventHandling(rocket)

        screen.fill(BLUE)

        # run ship position and draw functions
        rocket.updatePosition()
        rocket.blit_me()

        pygame.display.flip()

run()




