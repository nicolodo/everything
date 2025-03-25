
import json

filename = 'username.json' #get the file we are reading from

with open(filename) as f_obj:
    name = json.load(f_obj)
    print(f"Hello {name.capitalize()}!")

