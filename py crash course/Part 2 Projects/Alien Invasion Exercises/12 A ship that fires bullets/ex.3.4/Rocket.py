
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
                if event.key == pygame.K_UP:
                    rocket.rect.top -= 1
                if event.key == pygame.K_DOWN:
                    rocket.rect.top += 1
                if event.key == pygame.K_RIGHT:
                    rocket.rect.right += 1
                if event.key == pygame.K_LEFT:
                    rocket.rect.right -= 1


        screen.fill(BLUE)
        rocket.blit_me()

        pygame.display.flip()

run()




