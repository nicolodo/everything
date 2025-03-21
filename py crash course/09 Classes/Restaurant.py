
# restaurant ex 1

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
