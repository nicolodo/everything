
class Settings:
    """holds the settings values"""
    def __init__(self):
        self.screen = screen()
        self.bgColor = (200,   0,   100)

class screen:
    """settings particular to the screen"""
    def __init__(self):
        self.width = 500
        self.height = 400
        self.size = (self.width, self.height)
        self.caption = 'Sideways Shooter'

