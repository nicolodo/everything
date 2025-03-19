
# ex 12 Sandwiches
def makeSandwich(*toppings):
    print("this sandwich contains")
    for topping in toppings:
        print(f"\t-{topping}")
    print()

def ex12():
    makeSandwich('cheese','tomato','pickles','sausage')
    makeSandwich('egg','cress')
    makeSandwich('ham','cheese')

