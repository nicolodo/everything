
import json

filename = 'favourite number'

def get_user_favNum():
    while True:
        prompt = "Please enter your favourite number: "
        try:
            favNum = input(prompt)
            favNum = int(favNum)
            with open(filename,'w') as f_obj:
                json.dump(favNum,f_obj)
                return None
        except ValueError:
            continue
        except FileNotFoundError:
            return

def retrieve_favNum():
    try:
        with open(filename) as f_obj:
            favNum = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favNum

def greet_user():
    favNum = retrieve_favNum()
    if favNum:
        print(favNum)
    else:
        get_user_favNum()

greet_user()
