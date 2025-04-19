
import sys
from BulletClass import Bullet
from alien import Alien
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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw screen
    screen.fill(ai_settings.COLOR.WHITE)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # mk the most recently drawn screen visible
    pygame.display.flip()

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width -2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    return

def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)

