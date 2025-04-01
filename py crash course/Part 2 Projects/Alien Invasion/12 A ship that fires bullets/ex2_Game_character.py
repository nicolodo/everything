
import sys, pygame
import character

# setup screen, SIZE
# blue color variable
# make a quit event


# Initialize pygame and make a screen object
def Run():
    SIZE = (400,300)
    BLUE = (50, 50, 168)
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    NAME = 'Blue Sky'
    pygame.display.set_caption(NAME)
    ACTIVE = True

    Jim = character.Character(SCREEN)

    # Start the main loop
    while ACTIVE:

        # Watch for close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    sys.exit()

        # Fill screen with Blue background
        SCREEN.fill(BLUE)

        # Draw character onto the screen
        Jim.blitme()

        # Draw to screen
        pygame.display.flip()

Run()   







