
import sys
import pygame
import Settings

# make a window in pygame
def run():
    def quitGame():
        print("Thanks for playing!")
        sys.exit()
    pygame.init()
    settings = Settings.Settings()
    screen = pygame.display.set_mode((settings.screenSize))
    pygame.display.set_caption("Wake up Super Star!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitGame()

        screen.fill(settings.bgColor)

        pygame.display.flip()
run()
# make a star.bmp, import it to pygame

# using the height and width of screen and star
# find out how many fit in each row and column

# draw that to the screen and we are done
