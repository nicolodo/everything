
import random

class die:
    """Simulation of a dice"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_Dice(self):
        numberRolled = random.randint(1,self.sides)
        # print(numberRolled)
        return numberRolled

sides = [6,10,20]
throwRecord = {
    6:[],
    10:[],
    20:[]
}
for n in range(3):
    myDice = die(sides[n])
    print()
    for x in range(20):
        throwRecord[sides[n]].append(myDice.roll_Dice())
    print(throwRecord[sides[n]])
