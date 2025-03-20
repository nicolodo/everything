
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

def ex1and2():    
    lucianos = restaurant()
    lucianos.describeRestaurant()
    lucianos.openRestaurant()

    # ex2 multiple restaurants
    pinguino = restaurant('pinguino','penguins')
    pinguino.describeRestaurant()

restaurant = restaurant()
print(restaurant.numberServed)
restaurant.numberServed += 5
print(restaurant.numberServed)

restaurant.setNumberServed(500)
print(restaurant.numberServed)

restaurant.incrementNumberServed(20) 
print(restaurant.numberServed)




