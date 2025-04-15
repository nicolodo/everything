
# make a pygame instance
# make an event loop that checks what key is pressed
# print that key to the user

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,600))
BLUE = (0,128, 128)
RED =  (128,  0,0)

iskeypressed = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            iskeypressed = True
            screen.fill(RED)
            print(event)
        if event.type == pygame.KEYUP:
            iskeypressed = False

        if not iskeypressed:
            screen.fill(BLUE)

        pygame.display.flip()






