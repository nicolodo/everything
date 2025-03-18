
def ex4():
    # this exercise is about pizza toppings

    ordering = True
    prompt = "what would you like on your pizza"
    prompt += "\n please type quit to quit: "
    while ordering:
        request = input(prompt)
        if request == 'quit':
            break
        print(f"we will add {request} to your pizza")
    
def ex5():
    # cinema tickets
    price = [0,10,12]
    ages = [3,12,13]
    
    prompt = "please enter your age: "
    customerAge = int(input(prompt))

    if customerAge < 3:
        print(price[0])
    if customerAge <= 12:
        print(price[1])
    if customerAge > 12:
        print(price[2])

ex5()