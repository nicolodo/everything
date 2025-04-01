
import pygame, sys



def run():
    pygame.init()
    SCREEN = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Rocket Game")
    ACTIVE = True

    while ACTIVE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
    pygame.display.flip()

run()
