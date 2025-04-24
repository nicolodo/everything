
import sys
import pygame
from pygame.sprite import Group
import Settings
from starClass import Star 
import gameFunctions as gf

# make a window in pygame
def run():
    pygame.init()
    settings = Settings.Settings()
    screen = pygame.display.set_mode((settings.screenSize))
    pygame.display.set_caption("Wake up Super Star!")

    star = Star(screen)
    stars = Group()

    while True:
        gf.eventHandling()
        gf.updateScreen(star, screen, stars)

run()
# make a star.bmp, import it to pygame

# using the height and width of screen and star
# find out how many fit in each row and column

# draw that to the screen and we are done
