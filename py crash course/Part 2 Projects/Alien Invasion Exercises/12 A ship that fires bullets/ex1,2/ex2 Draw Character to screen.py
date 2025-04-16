
# Make a pygame window with a blue background

import sys, pygame
from character import Character
BLUE = (0  ,  0, 255)

def run():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    name = "Sonic fever"
    pygame.display.set_caption(name)

    # import sonic
    sonic = Character(screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BLUE)

        sonic.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run()



