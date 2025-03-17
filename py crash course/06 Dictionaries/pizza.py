# store information about a pizza being ordered
pizza  = {
    'crust':'thin',
    'toppings':['tomato','basil','anchovies','garlic']
}

print(f"the pizza crust is {pizza['crust']}")
for topping in pizza['toppings']:
    print(f"the pizza has {topping}")

