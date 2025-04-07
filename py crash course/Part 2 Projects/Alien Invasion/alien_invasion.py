
# import libraries
import pygame, sys

def run():

    pygame.init()
    SIZE = (400, 300)
    SCREEN = pygame.display.set_mode(SIZE)
    COLOR = (200,200,200)
    # choose a name for the window
    NAME = "Alien Invasion"
    ACTIVE = True


    # setup the event loop
    while ACTIVE:
        for event in pygame.event.get():
            if event == pygame.QUIT: # close if x clicked
                sys.exit()

run()


