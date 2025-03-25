
from pathlib import Path
import json

fileName = 'favouriteNumber.json'

try:
    with open(fileName) as f_obj:
        favNum = json.load(f_obj)
        print(f"Your favourite number was stored as: {favNum}")
except FileNotFoundError:
    while True:
        try:
            favNum = input("What is your favourite number: ")
            favNum = int(favNum)
        except ValueError:
            print("Only numbers please!")
        else:
            with open(fileName,'w') as f_obj:
                json.dump(favNum, f_obj)
            print("Your number has been saved!")
            break



