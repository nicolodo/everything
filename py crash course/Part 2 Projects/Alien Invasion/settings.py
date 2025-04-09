
class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialise the games settings"""
        # Screen settings
        self.SCREEN_SIZE = (400,300)
        self.BG_COLOR = (200,200,200)
        self.COLOR = Color()
        
class Color:
    """A class to store colours"""

    def __init__(self):
        """Initialise colours"""
        
        self.RED   = (255,  0,  0)
        self.GREEN = (  0,255,  0)
        self.BLUE  = (  0,  0,255)

        self.BLACK = (  0,  0,  0)
        self.WHITE = (255,255,255)


