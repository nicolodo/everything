
# mountain poll

active = True
responses = {}

while active:
    # get the name and the mountain they want to climb
    name = input('whats your name son?: ')
    mountain = input('what mountain do you wanna climb?: ')

    # add it to the list
    responses[name] = mountain

    # check if anyone else wants to add to the poll
    again = input('another? (type no to break)')
    if again == 'no':
        active = False

# print each person and where they want to climb
for person, mountain in responses.items():
    print(f"{person} wants to climb {mountain} good luck!")