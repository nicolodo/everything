
import json

filename = 'favourite_number2.json'

try:
    with open(filename,'w') as f_obj:
        favNum = json.load(f_obj)
        print(f"Your favourite number was stored as: {favNum}")
except FileNotFoundError:
    print("You have to store your number first!")
