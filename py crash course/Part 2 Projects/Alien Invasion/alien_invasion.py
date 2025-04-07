
# import libraries
import pygame, sys

def run():

    pygame.init()
    SIZE = (400, 300)
    SCREEN = pygame.display.set_mode(SIZE)
    COLOR = (200,200,200)
    # choose a name for the window
    NAME = "Alien Invasion"
    pygame.display.set_caption(NAME)
    ACTIVE = True


    # setup the event loop
    while ACTIVE:
        # watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # close if x clicked
                sys.exit()

        # Redraw screen
        SCREEN.fill(COLOR)

        # mk the most recently drawn screen visible
        pygame.display.flip()


run()


