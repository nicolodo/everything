
import pygame, sys

def createBullet(ship):
    print("gun jammed")

def on_keyDown(event,ship):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_UP:
        ship.moveUp = True
    if event.key == pygame.K_DOWN:
        ship.moveDown = True
    if event.key == pygame.K_SPACE:
        createBullet(ship)

def on_keyUp(event, ship):
    if event.key == pygame.K_UP:
        ship.moveUp = False
    if event.key == pygame.K_DOWN:
        ship.moveDown = False

def get_events(ship):
    # KeyMoveUp = pygame.K_UP
    # KeyMoveDown = pygame.K_DOWN

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            on_keyDown(event, ship)
        if event.type == pygame.KEYUP:
            on_keyUp(event, ship)

