
# move rocket game via keyinput

import sys, pygame

def run():
    # setup pygame, screen, name
    # setup event loop
    # setup draw to screen loop
    # setup rocket class
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Rockets of the empire")
    BLUE = (  0,  0, 128)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BLUE)

        pygame.display.flip()

run()




