
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
            print(f"We have found a name: {name}")
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
    answer = ''
    prompt = "Is this you (y)es or (n)o: "
    while answer.lower() not in ['y','n']: 
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
    if name:
        sameUser = isItSameUser()
        if not sameUser:
            name = get_name()
    else:
        name = get_name()
        
    print(f"Hi {name} lovely to see you today!")

verify_user()    




























