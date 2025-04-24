
import pygame
import sys
import Settings
settings = Settings.Settings()
from pygame.sprite import Sprite
from starClass import Star

def makeStars(screen, stars):
    star = Star(screen)
    starsPerWidth = int(settings.screenWidth/star.rect.width)
    print(starsPerWidth)
    for x in range(starsPerWidth):
        newStar = Star(screen)
        newStar.rect.x = x*newStar.rect.width
        stars.add(newStar)
    stars.draw(screen)

def quitGame():
    print("Thanks for playing!")
    sys.exit()

def eventHandling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quitGame()

def updateScreen(star, screen, stars):
    screen.fill(settings.bgColor)
    makeStars(screen, stars)
    # star.blit_me()

    pygame.display.flip()