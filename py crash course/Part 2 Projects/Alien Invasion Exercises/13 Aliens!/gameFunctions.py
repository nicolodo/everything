
import pygame
import sys
import Settings
settings = Settings.Settings()
from pygame.sprite import Sprite
from starClass import Star

def makeStars(screen, stars):
    star = Star(screen)
    # horizontal line of stars placement
    starsPerWidth = int(settings.screenWidth/star.rect.width)
    for x in range(int(starsPerWidth/2)):
        newStar = Star(screen)
        newStar.rect.x = 2*x*newStar.rect.width + newStar.rect.width/2
        stars.add(newStar)
    # vertical line of stars 
    starsPerHeight = int(settings.screenHeight/star.rect.height)
    for y in range(int(starsPerHeight/2)):
        newStar = Star(screen)
        newStar.rect.y = 2*y*newStar.rect.height
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

def updateScreen(screen, stars):
    screen.fill(settings.bgColor)
    makeStars(screen, stars)
    # star.blit_me()

    pygame.display.flip()


