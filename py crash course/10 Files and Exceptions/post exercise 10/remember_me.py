
import json

# saves a users name to a json and says goodbye

filename = 'username.json'
prompt = "Please enter your name: "
name = input(prompt)
with open(filename,'w') as f_obj:
    json.dump(name,f_obj)
    print("thank you " + name + " we will be in touch!")