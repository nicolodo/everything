
import random

# print(len(winningSequence))

# my pick
myPick = list("8B4E")
print(myPick)
inloop = True
x = 1
y = input("lets start the lottery")
while inloop:
    winningSequence = list("1234567890ABCDE")
    selects = []
    for pick in range(4):
        selection = winningSequence.pop(random.randint(0, 14 - pick))
        selects.append(selection)

    # print(selects)
    if myPick == selects:
        break
    x += 1

print(myPick)
print(x)