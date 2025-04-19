
import sys
from BulletClass import Bullet
import pygame
from settings import Settings

ai_settings = Settings()

def check_keydown_events(event, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(screen, ship, bullets)

def fire_bullet(screen, ship, bullets):
    # create a new bullet
    if len(bullets) < ai_settings.bullet.numAllowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """move bullets and rm offscreen bullets"""
    bullets.update()

    # check if bullet is still on screen
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # print('bullets: ' + str(len(bullets)))

def update_screen(ai_settings, screen, ship, alien, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw screen
    screen.fill(ai_settings.COLOR.WHITE)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    # mk the most recently drawn screen visible
    pygame.display.flip()



