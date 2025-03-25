
import json

# We are asking the user for a number

filename = 'favouriteNumber2.json'
while True:
    try:
        favNum = input("please enter a number: ")
        favNum = int(favNum)
    except ValueError:
        print("please only enter numbers")
    else:
        with open(filename,'w') as f_obj:
            json.dump(favNum,f_obj) 
            print("Your number has been saved!")
            break