
import pygame
import sys
import Settings
settings = Settings.Settings()
from pygame.sprite import Sprite
from starClass import Star

from random import randint

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

def makeStars(screen, stars, wobbliness):
    star = Star(screen)
    # horizontal line of stars placement
    starsPerWidth = int(settings.screenWidth/star.rect.width)
    starsPerHeight = int(settings.screenHeight/star.rect.height)
    for x in range(int(starsPerWidth/2)):
        newStar = Star(screen)
        for y in range(int(starsPerHeight/2)):
        # vertical line of stars 
            newStar = Star(screen)
            newStar.rect.y = 2*y*star.height + star.height/2 + randint(0, wobbliness)
            newStar.rect.x = 2*x*star.width + star.width/2 + randint(0, wobbliness)
            stars.add(newStar)
            
def justMakeStars(screen, stars, wobbliness):
    star = Star(screen)
    # horizontal line of stars placement
    starsPerWidth = int(settings.screenWidth/star.width)
    starsPerHeight = int(settings.screenHeight/star.height)
    for x in range(int(starsPerWidth/2)):
        print(len(stars))
        for y in range(int(starsPerHeight/2)):
        # vertical line of stars 
            newStar = Star(screen)
            newStar.rect.y = 2*y*star.height + star.height/2 
            newStar.rect.x = 2*x*star.width + star.width/2 
            stars.add(newStar)

def updateStarLocation(screen, stars, wobbliness):
    star = Star(screen)
    # horizontal line of stars placement
    starsPerWidth = int(settings.screenWidth/star.width)
    starsPerHeight = int(settings.screenHeight/star.height)
    for currentStar in stars.copy():
        star0 = currentStar
        for x in range(int(starsPerWidth/2)):
            for y in range(int(starsPerHeight/2)):
                # vertical line of stars 
                currentStar.rect.y = 2*y*star.height + star.height/2 + randint(0, wobbliness)
                currentStar.rect.x = 2*x*star.width + star.width/2 + randint(0, wobbliness)
        stars.remove(star0)
        stars.add(currentStar)

def updateScreen(screen, stars, wobbliness):
    screen.fill(settings.bgColor)
    updateStarLocation(screen, stars, wobbliness)
    stars.draw(screen)
    # star.blit_me()

    pygame.display.flip()


