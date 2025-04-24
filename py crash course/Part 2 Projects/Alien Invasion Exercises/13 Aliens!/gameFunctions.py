
import pygame
import sys
import Settings
settings = Settings.Settings()

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

def updateScreen(star, screen):
    screen.fill(settings.bgColor)
    star.blit_me()

    pygame.display.flip()