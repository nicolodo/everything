
# import libraries
import pygame 

from settings import Settings
from pygame.sprite import Group
from ship import Ship
from alien import Alien
import game_functions as gf

def run():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_SIZE)
    # choose a name for the window
    NAME = "Alien Invasion"
    pygame.display.set_caption(NAME)

    # Make a ship and bullet group
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # Make an alien.
    alien = Alien(ai_settings, screen)

    # setup the event loop
    while True:
        # watch for events
        gf.check_events(screen,ship, bullets)
        ship.update() # update the ships position based on flag
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run()


