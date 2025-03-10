# requested_toppings = 'mushrooms'

requested_toppings = ['mushrooms', 'cheese', 'tomatoes', 'anchovies']
# if requested_toppings != 'anchovies':
#     print("hold the anchovies")
available_toppings = ['mushrooms', 'bacon', 'tomatoes', 'bagels']
#empty check
if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            print(f"We have added {topping} to your pizza!")
        else:
            print(f"sorry we dont have that available")
    print(f"We finished making your pizza")  
else:
    print(f"Are you sure you want a plain pizza?")