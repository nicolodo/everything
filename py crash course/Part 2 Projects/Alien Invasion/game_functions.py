
import sys

import pygame

def check_events(ship):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
                # easy quit game
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True 
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False 

def update_screen(ai_settings, screen, ship):
    # update images on the screen and flip to new screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # make the most recently drawn frame visible
    pygame.display.flip()






