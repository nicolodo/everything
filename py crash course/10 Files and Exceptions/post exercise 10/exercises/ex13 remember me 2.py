
# remember me for multiple users
# ex13

import json

# get the name of whoever and store it
prompt = "please write your name: "
name = input(prompt)
try:
    with open(filename,'w') as f_obj:
        json.dump(name, f_obj)
except FileNotFoundError:
    print("Oh no the file wasn't found oh no")

# retrieve the name from json
try:
    with open(filename) as f_obj:
        name = json.load(f_obj)
        print(name)
except FileNotFoundError:
    print("File not found oh no oh dear")

