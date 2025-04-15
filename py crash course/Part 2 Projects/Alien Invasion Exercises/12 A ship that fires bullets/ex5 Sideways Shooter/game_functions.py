
def get_events(ship):
    KeyMoveUp = pygame.K_UP
    KeyMoveDown = pygame.K_DOWN

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_q:
                    sys.exit()
                case pygame.K_UP:
                    ship.moveUp = True
                case pygame.K_DOWN:
                    ship.moveDown = True
                case _:
                    continue
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_UP:
                    ship.moveUp = False
                case pygame.K_DOWN:
                    ship.moveDown = False
                case _:
                    continue