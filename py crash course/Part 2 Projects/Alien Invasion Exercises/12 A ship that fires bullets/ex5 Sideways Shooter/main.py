
import pygame, sys
from SettingsClass import Settings
from shipClass import Ship
import game_functions as gf
from pygame.sprite import Group

def run():
    # Setup window
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen.size)
    pygame.display.set_caption(settings.screen.caption)
    
    ship = Ship(screen)
    # Make a group to store bullets in
    bullets = Group()

    while True:
        # main game handling loop

        # handle key events
        gf.get_events(ship, bullets, screen)
        ship.update() # update ship pos
        # run the update function on every bullet in group
        bullets.update() 

        # draw to screen
        screen.fill(settings.bgColor)
        ship.blit_me()
        # bullets.blit_me()
        pygame.display.flip()
        print(len(bullets))

run()
