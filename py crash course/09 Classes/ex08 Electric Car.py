
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attiributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odomoter += miles

class Battery:
    """Simulation of a battery"""
    def __init__(self,battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def getRange(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize the attributes of the parent class
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()
    

myLeaf = ElectricCar('Nissan', 'Leaf', 2024)
print(myLeaf.get_descriptive_name())
myLeaf.battery.describe_battery()
myLeaf.battery.getRange()

myLeaf.battery.upgrade_battery()
myLeaf.battery.()
