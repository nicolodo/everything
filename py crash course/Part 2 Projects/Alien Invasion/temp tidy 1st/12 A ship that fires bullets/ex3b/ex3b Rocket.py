
import pygame, sys
from RKTsettings import RKTSettings


def run():
    # Setup
    pygame.init()
    ACTIVE = True
    RKT_settings = RKTSettings()

    SCREEN = pygame.display.set_mode(RKT_settings.SCREEN_SIZE)
    pygame.display.set_caption(RKT_settings.TITLE)

    # init Rocket
    rocket = Rocket()
    while ACTIVE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event == pygame.K_RIGHT:
                    rocket.x += 1
        
        # Draw background to the screen
        SCREEN.fill(RKT_settings.BG_COLOR)
        pygame.display.flip()

run()










