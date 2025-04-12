
# move rocket game via keyinput

import sys, pygame
from SettingsClass import Settings
from RocketClass import Rocket

def run():
    # setup pygame, screen, name
    # setup event loop
    # setup draw to screen loop
    # setup rocket class
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Rockets of the empire")
    BLUE = (  0, 128, 128)
    ai_settings = Settings

    rocket = Rocket(screen, ai_settings)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # handle keyboard events
            if event.type == pygame.KEYDOWN:
                # easy quit with q
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_UP:
                    rocket.moveUp = True
                if event.key == pygame.K_DOWN:
                    rocket.moveDown = True
                if event.key == pygame.K_RIGHT:
                    rocket.moveRight = True
                if event.key == pygame.K_LEFT:
                    rocket.moveLeft = True 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rocket.moveUp = False
                if event.key == pygame.K_DOWN:
                    rocket.moveDown = False
                if event.key == pygame.K_RIGHT:
                    rocket.moveRight = False
                if event.key == pygame.K_LEFT:
                    rocket.moveLeft = False 
                

        screen.fill(BLUE)
        rocket.updatePosition()
        rocket.blit_me()

        pygame.display.flip()

run()




