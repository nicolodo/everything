
# remember me for multiple users
# ex13

import json

def get_name():
    name = ""
    while name == "":
        # get the name of whoever and store it

        filename = 'username.json'

        prompt = "please write your name: "
        name = input(prompt)
        if name == "":
            continue
        try:
            with open(filename,'w') as f_obj:
                json.dump(name, f_obj)
        except FileNotFoundError:
            print("Oh no the file wasn't found oh no")
        else:
            return name

def retrieve_name():
    # retrieve the name from json
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            name = json.load(f_obj)
            print(name)
    except FileNotFoundError:
        print("File not found oh no oh dear")                            
        return None
    else:
        return name

def greet_user():
    # Start the greet user-remember me program
    name = get_name()
    if name:
        print(f"great thanks we've saved your name {name}")
    else:
        name = retrieve_name()
        print(f"Hi {name} nice to see you again")

def isItSameUser():
    answer = None
    prompt = "Is this you yes or no: "
    while answer.lower() not in ['yes','no','y','n']:
        answer = input(prompt)
    if 'y' in answer:
        return True
    else:
        return False

def verify_user():
    # check if the user is the same as last time
    # before welcome back message we check if its the same user
    # Ask if this is the correct username
    # if not thencall get_new_username()
    name = retrieve_name()
    if not name:
        name == get_name()
    else:
        sameUser = isItSameUser()

    




























