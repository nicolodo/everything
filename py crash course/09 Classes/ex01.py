
# restaurant ex 1

class restaurant:
    """Simulation of a restaurant"""
    def __init__(self,name='lucianos',cuisine='machiatto'):
        self.name = name
        self.cuisine = cuisine
    
    def describeRestaurant(self):
        print(f"{self.name} serves {self.cuisine}")

    def openRestaurant(self):
        print(f"{self.name} is open!")

lucianos = restaurant()
lucianos.describeRestaurant()
lucianos.openRestaurant()

# ex2 multiple restaurants
pinguino = restaurant('pinguino','penguins')
pinguino.describeRestaurant()