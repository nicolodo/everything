
import pygame, sys

# event handling logic 

def eventHandling(rocket):
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










