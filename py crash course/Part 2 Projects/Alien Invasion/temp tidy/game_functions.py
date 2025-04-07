
import sys

import pygame


def check_keydown_events(events, ship):
    """Respond to keypresses."""
    if events.key == pygame.K_q:
        sys.exit()
        # easy quit game
    if events.key == pygame.K_RIGHT:
        ship.moving_right = True
    if events.key == pygame.K_LEFT:
        ship.moving_left = True 

def check_keyup_events(events, ship):
    """Respond to key releases."""
    if events.key == pygame.K_RIGHT:
        ship.moving_right = False
    if events.key == pygame.K_LEFT:
        ship.moving_left = False 

def check_events(ship):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship):
    # update images on the screen and flip to new screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # make the most recently drawn frame visible
    pygame.display.flip()






