
import pygame, sys
from SettingsClass import Settings
from shipClass import Ship
import game_functions as gf

def run():
    # Setup window
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen.size)
    pygame.display.set_caption(settings.screen.caption)
    
    ship = Ship(screen)

    while True:
        # event handling loop
        
        # set movement keys
        gf.get_events(ship) 
        ship.update()

            

        # draw to screen
        screen.fill(settings.bgColor)
        ship.blit_me()

        pygame.display.flip()


run()
