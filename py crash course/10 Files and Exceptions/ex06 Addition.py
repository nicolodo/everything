

prompt = "please enter number"

while True:
    try:
        n1 = input(prompt + '1: ')
        n1 = int(n1)
        n2 = input(prompt + '2: ')
        n2 = int(n2)
    except ValueError:
        print("please enter integer")
    else:
        print(n1 + n2)

