
# start with some models that need to be printed
unprinted = ['dog','car','bus','rain','slime','hat']
printed = []

# simulate printing
def printModels(unprinted,printed)
    while unprinted:
        current = unprinted.pop()
        print(f"currently printing {current}")
        printed.append(current)

# display all completed modules
def showCompletedModels(completed):
    print("The following models have been printed")
    for model in printed:
        print(f"\t{model}")