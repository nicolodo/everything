
import json

filename = 'username.json' #get the file we are reading from

try:
    with open(filename) as f_obj:
        name = json.load(f_obj)
except FileNotFoundError:
    print("please make the file first!")
else:
    print(f"Hello {name.capitalize()}!")

