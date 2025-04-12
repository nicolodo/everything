
class Settings:

    def __init__(self):
        self.width = 400
        self.height = 300
        self.caption = 'Rockets of the empire'
        self.colors = {
            'BLUE': (   0,   0, 128),
            'RED' : ( 128,   0,   0)
        }

        # rocket stuff
        self.rocketSpeed = 1