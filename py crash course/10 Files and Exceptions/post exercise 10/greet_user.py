
import json

filename = 'username.json' #get the file we are reading from

def get_stored_username():
    try:
        with open(filename) as f_obj:
            name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return name

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Hello " + username)
    else:
        # ask for name
        get_username()

greet_user()
