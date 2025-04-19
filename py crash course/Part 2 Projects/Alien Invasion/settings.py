
class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialise the games settings"""
        # screen settings
        self.screen_SIZE = (600,600)
        self.BG_COLOR = (200,200,200)
        self.COLOR = Color()

        # Ship settings
        self.ship_speed_factor = 1.5
        
        # Bullet settings
        self.bullet = Bullet()

class Bullet:
    """Holds settings particular to bullets"""

    def __init__(self):
        self.speedFactor = 1
        self.width = 3
        self.height = 10
        self.color = ( 60, 60, 60)
        self.numAllowed = 3

class Color:
    """A class to store colours"""
    def __init__(self):
        self.RED   = (255,  0,  0)
        self.GREEN = (  0,255,  0)
        self.BLUE  = (  0,  0,255)

        self.BLACK = (  0,  0,  0)
        self.WHITE = (255,255,255)


