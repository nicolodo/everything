
import sys

import pygame
import game_functions as gf

from ship import Ship
from settings import Settings

def run_game():
    # Initialize pygame, settings,and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen) 

    # Start the main loop for the game.
    while True:
        gf.check_events(ship) # setup ship move flags
        ship.update() # update ship var values

        # Draw background and ship to screen
        gf.update_screen(ai_settings, screen, ship)


run_game()






