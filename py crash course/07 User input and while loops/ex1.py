
def ex1():
    prompt = "what car would you like? : "
    choice = input(prompt)
    print(f"I see you would like a {choice} how nice!")

def ex2():
    # how many are dining today?
    prompt = "How many are dining today?"
    request = input(prompt)
    request = int(request)

    if request > 8:
        print("sorry as you are more than 8 you will have to wait for a table")
    else:
        print(f"table for {request} right this way!")

# multiples of 10
def ex3():
    prompt = "please enter a number"
    prompt += "\n we will let you know if its a multiple of 10:"

    isaTen = int(input(prompt))
    if isaTen % 10 == 0:
        print("your number is a multiple of ten!")

ex3()
