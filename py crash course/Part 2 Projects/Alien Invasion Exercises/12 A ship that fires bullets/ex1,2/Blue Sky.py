
# Make a pygame window with a blue background

import sys, pygame

BLUE = (0  ,  0, 255)

def run():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Blue Sky")

    while True:

        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        screen.fill(BLUE)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run()



