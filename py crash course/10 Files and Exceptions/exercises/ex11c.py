
import json

filename = 'favouriteNumber2.json'

def retrieveFavNum():
    try:
        with open(filename) as f_obj:
            favNum = json.load(f_obj)
            print(f"Your favourite number was stored as: {favNum}")
    except FileNotFoundError:
        print("You have to store your number first!")

retrieveFavNum()
