
# import libraries
import pygame 

from settings import Settings
from pygame.sprite import Group
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

    # Make a ship and bullet group
    ship = Ship(ai_settings, SCREEN)
    bullets = Group()

    # setup the event loop
    while True:
        # watch for events
        gf.check_events(SCREEN,ship, bullets)
        ship.update() # update the ships position based on flag
        bullets.update()
        gf.update_screen(ai_settings, SCREEN, ship, bullets)

run()


