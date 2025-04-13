
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
        
        # set movement keys
        KeyMoveUp = pygame.K_UP
        KeyMoveDown = pygame.K_DOWN

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        sys.exit()
                    case pygame.K_UP:
                        ship.moveUp = True
                    case pygame.K_DOWN:
                        ship.moveDown = True
                    case _:
                        continue
            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_UP:
                        ship.moveUp = False
                    case pygame.K_DOWN:
                        ship.moveDown = False
                    case _:
                        continue
            
        ship.update()

            

        # draw to screen
        screen.fill(settings.bgColor)
        ship.blit_me()

        pygame.display.flip()


run()
