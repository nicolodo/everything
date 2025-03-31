
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

    # Set the backgrouned color.
    bg_color = (230,230,230)

    ship = Ship(screen) 

    # Start the main loop for the game.
    while True:
        gf.check_events()

        # Redraw the screen during each pass through the loop.                  

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()






