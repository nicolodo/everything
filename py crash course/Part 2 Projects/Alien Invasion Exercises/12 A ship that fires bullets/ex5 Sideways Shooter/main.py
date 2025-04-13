
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
                match event.key:
                    case pygame.K_q:
                        sys.exit()
                    case pygame.K_w:
                        ship.moveUp = True
                    case pygame.K_s:
                        ship.moveDown = True
                    case _:
                        continue
            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_w:
                        ship.moveUp = False
                    case pygame.K_s:
                        ship.moveDown = False
                    case _:
                        continue

            

        # draw to screen
        screen.fill(settings.bgColor)
        ship.blit_me()

        pygame.display.flip()


run()
