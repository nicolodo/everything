
active = True

prompt = "tell me something I will repeat it back to you\n"
prompt += "type 'quit' to quit: "   
message = input(prompt)
print(message)
print()

while active: 
    message = input(prompt)
    if message == 'quit':
        print("Thank you so much for running my program!")
        active = False
        break
    print(message)
    print()