
import pygame, sys
from bulletClass import Bullet

def createBullet(ship, bullets, screen):
    # make and add bullet at ship pos to group
    new_bullet = Bullet(ship, screen)
    bullets.add(new_bullet)

def on_keyDown(event,ship, bullets, screen):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_UP:
        ship.moveUp = True
    if event.key == pygame.K_DOWN:
        ship.moveDown = True
    if event.key == pygame.K_SPACE:
        createBullet(ship, bullets, screen)

def on_keyUp(event, ship):
    if event.key == pygame.K_UP:
        ship.moveUp = False
    if event.key == pygame.K_DOWN:
        ship.moveDown = False

def get_events(ship, bullets, screen):
    # KeyMoveUp = pygame.K_UP
    # KeyMoveDown = pygame.K_DOWN

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            on_keyDown(event, ship, bullets, screen)
        if event.type == pygame.KEYUP:
            on_keyUp(event, ship)

def update_screen(bullets):
    for bullet in bullets.sprites():
        bullet.blit_me()


