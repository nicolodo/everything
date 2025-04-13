
import pygame, sys
from SettingsClass import Settings
from shipClass import Ship

def run():
    # Setup window
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen.size)
    pygame.display.set_caption(settings.screen.caption)
    
    ship = Ship(screen)

    while True:
        # event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        # draw to screen
        screen.fill(settings.bgColor)
        ship.blit_me()

        pygame.display.flip()


run()
