
# restaurant ex 1,2,4,6

class restaurant:
    """Simulation of a restaurant"""
    def __init__(self,name='lucianos',cuisine='machiatto'):
        self.name = name
        self.cuisine = cuisine
        self.numberServed = 0
    
    def setNumberServed(self, served):
        self.numberServed = served
    
    def incrementNumberServed(self, servedSince):
        self.numberServed += servedSince

    def describeRestaurant(self):
        print(f"{self.name} serves {self.cuisine}")

    def openRestaurant(self):
        print(f"{self.name} is open!")

class iceCreamStand(restaurant):
    """Simulation of an ice cream stand"""
    def __init__(self,name,flavours):
        """initialise parent class attributes
        then initialise ice cream class attributes"""
        super().__init__(name,'ice cream')
        flavours = list(flavours)
        initalFlavours = ['vanilla','chocolate']
        self.flavours = initalFlavours + flavours
    
    def displayIceCreams(self):
        print("This ice cream store sells ice cream of")
        for flavour in self.flavours:
            print(f"\t{flavour}")
    
butterbys = iceCreamStand(
    'Butterbys',
    ['butter']
)
butterbys.displayIceCreams()